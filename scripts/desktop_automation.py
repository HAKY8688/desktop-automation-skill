#!/usr/bin/env python3
"""
Desktop Automation Script
提供鼠标、键盘、窗口管理等桌面自动化功能
"""

import argparse
import json
import sys
import time
import subprocess
import os

# 尝试导入依赖库
try:
    import pyautogui
    import pygetwindow
    import mss
    DEPENDENCIES_INSTALLED = True
except ImportError:
    DEPENDENCIES_INSTALLED = False


def check_dependencies():
    """检查依赖是否安装"""
    if not DEPENDENCIES_INSTALLED:
        return False
    
    # 检查是否有显示器
    try:
        import tkinter
        return True
    except:
        return False


def mouse_click(x, y, button='left', clicks=1, interval=0.0):
    """点击指定坐标"""
    pyautogui.click(x, y, clicks=clicks, interval=interval, button=button)
    return {"status": "ok", "action": "click", "x": x, "y": y}


def mouse_move(x, y, duration=0.5):
    """移动鼠标到指定坐标"""
    pyautogui.moveTo(x, y, duration=duration)
    return {"status": "ok", "action": "move", "x": x, "y": y}


def mouse_drag(x1, y1, x2, y2, duration=0.5, button='left'):
    """拖拽鼠标"""
    pyautogui.moveTo(x1, y1)
    pyautogui.dragTo(x2, y2, duration=duration, button=button)
    return {"status": "ok", "action": "drag", "from": (x1, y1), "to": (x2, y2)}


def mouse_position():
    """获取当前鼠标位置"""
    x, y = pyautogui.position()
    return {"status": "ok", "position": {"x": x, "y": y}}


def keyboard_type(text, interval=0.0):
    """输入文本"""
    pyautogui.write(text, interval=interval)
    return {"status": "ok", "action": "type", "text": text}


def keyboard_press(key):
    """按单个键"""
    pyautogui.press(key)
    return {"status": "ok", "action": "press", "key": key}


def keyboard_hotkey(*keys):
    """按组合键"""
    pyautogui.hotkey(*keys)
    return {"status": "ok", "action": "hotkey", "keys": list(keys)}


def window_list():
    """列出所有窗口"""
    windows = pygetwindow.getWindows()
    result = []
    for win in windows:
        result.append({
            "title": win.title,
            "left": win.left,
            "top": win.top,
            "width": win.width,
            "height": win.height,
            "is_active": win.isActive,
            "is_minimized": win.isMinimized
        })
    return {"status": "ok", "windows": result}


def window_get(title):
    """获取窗口信息"""
    try:
        wins = pygetwindow.getWindowsWithTitle(title)
        if wins:
            win = wins[0]
            return {
                "status": "ok",
                "window": {
                    "title": win.title,
                    "left": win.left,
                    "top": win.top,
                    "width": win.width,
                    "height": win.height,
                    "is_active": win.isActive,
                    "is_minimized": win.isMinimized
                }
            }
        return {"status": "error", "message": f"窗口未找到: {title}"}
    except Exception as e:
        return {"status": "error", "message": str(e)}


def window_activate(title):
    """激活窗口"""
    try:
        wins = pygetwindow.getWindowsWithTitle(title)
        if wins:
            wins[0].activate()
            return {"status": "ok", "action": "activate", "title": title}
        return {"status": "error", "message": f"窗口未找到: {title}"}
    except Exception as e:
        return {"status": "error", "message": str(e)}


def window_close(title):
    """关闭窗口"""
    try:
        wins = pygetwindow.getWindowsWithTitle(title)
        if wins:
            wins[0].close()
            return {"status": "ok", "action": "close", "title": title}
        return {"status": "error", "message": f"窗口未找到: {title}"}
    except Exception as e:
        return {"status": "error", "message": str(e)}


def window_move(title, x, y):
    """移动窗口"""
    try:
        wins = pygetwindow.getWindowsWithTitle(title)
        if wins:
            wins[0].move(x, y)
            return {"status": "ok", "action": "move", "title": title, "x": x, "y": y}
        return {"status": "error", "message": f"窗口未找到: {title}"}
    except Exception as e:
        return {"status": "error", "message": str(e)}


def window_resize(title, width, height):
    """调整窗口大小"""
    try:
        wins = pygetwindow.getWindowsWithTitle(title)
        if wins:
            wins[0].resize(width, height)
            return {"status": "ok", "action": "resize", "title": title, "width": width, "height": height}
        return {"status": "error", "message": f"窗口未找到: {title}"}
    except Exception as e:
        return {"status": "error", "message": str(e)}


def screenshot(output_path=None):
    """截图"""
    if output_path is None:
        output_path = f"/tmp/screenshot_{int(time.time())}.png"
    
    # 使用 mss 截图（更可靠）
    with mss.mss() as sct:
        sct.shot(output=output_path)
    
    return {"status": "ok", "path": output_path}


def screenshot_region(x, y, width, height, output_path=None):
    """截取屏幕区域"""
    if output_path is None:
        output_path = f"/tmp/screenshot_{int(time.time())}.png"
    
    monitor = {"top": y, "left": x, "width": width, "height": height}
    
    with mss.mss() as sct:
        sct_img = sct.grab(monitor)
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output_path)
    
    return {"status": "ok", "path": output_path}


def wait(seconds):
    """等待"""
    time.sleep(float(seconds))
    return {"status": "ok", "waited": seconds}


def get_screen_size():
    """获取屏幕尺寸"""
    width, height = pyautogui.size()
    return {"status": "ok", "width": width, "height": height}


def main():
    parser = argparse.ArgumentParser(description='Desktop Automation Tool')
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # mouse click
    click_parser = subparsers.add_parser('mouse_click', help='点击鼠标')
    click_parser.add_argument('x', type=int, help='X坐标')
    click_parser.add_argument('y', type=int, help='Y坐标')
    click_parser.add_argument('--button', default='left', choices=['left', 'right', 'middle'])
    click_parser.add_argument('--clicks', type=int, default=1)
    
    # mouse move
    move_parser = subparsers.add_parser('mouse_move', help='移动鼠标')
    move_parser.add_argument('x', type=int, help='X坐标')
    move_parser.add_argument('y', type=int, help='Y坐标')
    move_parser.add_argument('--duration', type=float, default=0.5)
    
    # mouse drag
    drag_parser = subparsers.add_parser('mouse_drag', help='拖拽鼠标')
    drag_parser.add_argument('x1', type=int, help='起始X')
    drag_parser.add_argument('y1', type=int, help='起始Y')
    drag_parser.add_argument('x2', type=int, help='结束X')
    drag_parser.add_argument('y2', type=int, help='结束Y')
    
    # mouse position
    subparsers.add_parser('mouse_position', help='获取鼠标位置')
    
    # keyboard type
    type_parser = subparsers.add_parser('keyboard_type', help='输入文本')
    type_parser.add_argument('text', help='要输入的文本')
    
    # keyboard press
    press_parser = subparsers.add_parser('keyboard_press', help='按键')
    press_parser.add_argument('key', help='按键名称')
    
    # keyboard hotkey
    hotkey_parser = subparsers.add_parser('keyboard_hotkey', help='组合键')
    hotkey_parser.add_argument('keys', nargs='+', help='按键列表')
    
    # window list
    subparsers.add_parser('window_list', help='列出窗口')
    
    # window get
    window_get_parser = subparsers.add_parser('window_get', help='获取窗口')
    window_get_parser.add_argument('title', help='窗口标题')
    
    # window activate
    window_activate_parser = subparsers.add_parser('window_activate', help='激活窗口')
    window_activate_parser.add_argument('title', help='窗口标题')
    
    # window close
    window_close_parser = subparsers.add_parser('window_close', help='关闭窗口')
    window_close_parser.add_argument('title', help='窗口标题')
    
    # window move
    window_move_parser = subparsers.add_parser('window_move', help='移动窗口')
    window_move_parser.add_argument('title', help='窗口标题')
    window_move_parser.add_argument('x', type=int, help='X坐标')
    window_move_parser.add_argument('y', type=int, help='Y坐标')
    
    # window resize
    window_resize_parser = subparsers.add_parser('window_resize', help='调整窗口大小')
    window_resize_parser.add_argument('title', help='窗口标题')
    window_resize_parser.add_argument('width', type=int, help='宽度')
    window_resize_parser.add_argument('height', type=int, help='高度')
    
    # screenshot
    screenshot_parser = subparsers.add_parser('screenshot', help='截图')
    screenshot_parser.add_argument('--path', help='保存路径')
    
    # screenshot region
    region_parser = subparsers.add_parser('screenshot_region', help='区域截图')
    region_parser.add_argument('x', type=int, help='X坐标')
    region_parser.add_argument('y', type=int, help='Y坐标')
    region_parser.add_argument('width', type=int, help='宽度')
    region_parser.add_argument('height', type=int, help='高度')
    region_parser.add_argument('--path', help='保存路径')
    
    # wait
    wait_parser = subparsers.add_parser('wait', help='等待')
    wait_parser.add_argument('seconds', type=float, help='秒数')
    
    # screen size
    subparsers.add_parser('screen_size', help='获取屏幕尺寸')
    
    args = parser.parse_args()
    
    if not DEPENDENCIES_INSTALLED:
        print(json.dumps({
            "status": "error",
            "message": "依赖未安装，请运行: pip install pyautogui pygetwindow mss"
        }))
        sys.exit(1)
    
    result = None
    
    try:
        if args.command == 'mouse_click':
            result = mouse_click(args.x, args.y, args.button, args.clicks)
        elif args.command == 'mouse_move':
            result = mouse_move(args.x, args.y, args.duration)
        elif args.command == 'mouse_drag':
            result = mouse_drag(args.x1, args.y1, args.x2, args.y2)
        elif args.command == 'mouse_position':
            result = mouse_position()
        elif args.command == 'keyboard_type':
            result = keyboard_type(args.text)
        elif args.command == 'keyboard_press':
            result = keyboard_press(args.key)
        elif args.command == 'keyboard_hotkey':
            result = keyboard_hotkey(*args.keys)
        elif args.command == 'window_list':
            result = window_list()
        elif args.command == 'window_get':
            result = window_get(args.title)
        elif args.command == 'window_activate':
            result = window_activate(args.title)
        elif args.command == 'window_close':
            result = window_close(args.title)
        elif args.command == 'window_move':
            result = window_move(args.title, args.x, args.y)
        elif args.command == 'window_resize':
            result = window_resize(args.title, args.width, args.height)
        elif args.command == 'screenshot':
            result = screenshot(args.path)
        elif args.command == 'screenshot_region':
            result = screenshot_region(args.x, args.y, args.width, args.height, args.path)
        elif args.command == 'wait':
            result = wait(args.seconds)
        elif args.command == 'screen_size':
            result = get_screen_size()
        else:
            parser.print_help()
            sys.exit(1)
    except Exception as e:
        result = {"status": "error", "message": str(e)}
    
    print(json.dumps(result))


if __name__ == '__main__':
    main()
