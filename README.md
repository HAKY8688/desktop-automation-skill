# Desktop Automation Skill

> OpenClaw / Claude Code 桌面自动化技能

[![GitHub stars](https://img.shields.io/github/stars/HAKY8688/desktop-automation-skill)](https://github.com/HAKY8688/desktop-automation-skill/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

AI 助手桌面自动化控制技能，支持鼠标、键盘、窗口管理等操作。

## 功能特性

### 🖱️ 鼠标操作
- `mouse click <x> <y>` - 点击指定坐标
- `mouse move <x> <y>` - 移动到指定坐标
- `mouse drag <x1> <y1> <x2> <y2>` - 拖拽
- `mouse position` - 获取当前位置

### ⌨️ 键盘操作
- `keyboard type <text>` - 输入文本
- `keyboard press <key>` - 按键（如 Enter, Escape, Ctrl+C）
- `keyboard hotkey <key1> <key2> ...` - 组合键

### 🪟 窗口操作
- `window list` - 列出所有窗口
- `window get <title>` - 获取窗口信息
- `window activate <title>` - 激活窗口
- `window close <title>` - 关闭窗口
- `window move <title> <x> <y>` - 移动窗口
- `window size <title> <width> <height>` - 调整窗口大小

### 📸 截图
- `screenshot` - 截取整个屏幕
- `screenshot <x> <y> <width> <height>` - 截取区域

### ⏱️ 其他
- `wait <seconds>` - 等待秒数
- `screen_size` - 获取屏幕尺寸

## 安装

### 1. 安装依赖

```bash
# 克隆仓库
git clone https://github.com/HAKY8688/desktop-automation-skill.git
cd desktop-automation-skill

# 运行安装脚本
chmod +x scripts/install.sh
./scripts/install.sh
```

或手动安装：

```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install -y python3-tk python3-dev scrot
pip3 install pyautogui pygetwindow mss

# macOS
pip3 install pyautogui pygetwindow mss

# Windows
pip install pyautogui pygetwindow mss
```

### 2. 在 OpenClaw/Claude Code 中使用

将 `SKILL.md` 内容复制到你的 skill 目录即可使用。

## 使用示例

### 自动化任务示例

```python
# 通过 exec 调用
import subprocess

# 点击屏幕坐标 (100, 200)
subprocess.run(["python3", "scripts/desktop_automation.py", "mouse_click", "100", "200"])

# 输入文本 "Hello World"
subprocess.run(["python3", "scripts/desktop_automation.py", "keyboard_type", "Hello World"])

# 打开记事本并输入内容
subprocess.run(["python3", "scripts/desktop_automation.py", "keyboard_press", "win"])
subprocess.run(["python3", "scripts/desktop_automation.py", "keyboard_type", "notepad"])
subprocess.run(["python3", "scripts/desktop_automation.py", "keyboard_press", "enter"])
subprocess.run(["python3", "scripts/desktop_automation.py", "wait", "1"])
subprocess.run(["python3", "scripts/desktop_automation.py", "keyboard_type", "Hello from automation!"])
```

### 窗口管理

```python
# 列出所有窗口
subprocess.run(["python3", "scripts/desktop_automation.py", "window_list"])

# 激活特定窗口
subprocess.run(["python3", "scripts/desktop_automation.py", "window_activate", "Notepad"])

# 移动窗口
subprocess.run(["python3", "scripts/desktop_automation.py", "window_move", "Notepad", "0", "0"])
```

## 命令行用法

```bash
# 鼠标操作
python3 scripts/desktop_automation.py mouse_click 100 200
python3 scripts/desktop_automation.py mouse_move 500 500
python3 scripts/desktop_automation.py mouse_position
python3 scripts/desktop_automation.py mouse_drag 100 100 200 200

# 键盘操作
python3 scripts/desktop_automation.py keyboard_type "Hello World"
python3 scripts/desktop_automation.py keyboard_press enter
python3 scripts/desktop_automation.py keyboard_hotkey ctrl c

# 窗口操作
python3 scripts/desktop_automation.py window_list
python3 scripts/desktop_automation.py window_activate "Notepad"
python3 scripts/desktop_automation.py window_close "Notepad"

# 截图
python3 scripts/desktop_automation.py screenshot
python3 scripts/desktop_automation.py screenshot_region 0 0 800 600

# 其他
python3 scripts/desktop_automation.py wait 2
python3 scripts/desktop_automation.py screen_size
```

## 返回格式

所有命令返回 JSON 格式：

```json
{"status": "ok", "action": "click", "x": 100, "y": 200}
```

错误时：

```json
{"status": "error", "message": "窗口未找到: Notepad"}
```

## 注意事项

- Linux 系统需要安装 `scrot` 才能截图
- 部分功能需要管理员权限
- 窗口操作可能受杀毒软件影响

## 技术栈

- [pyautogui](https://github.com/asweigart/pyautogui) - 鼠标/键盘控制
- [pygetwindow](https://github.com/asweigart/pygetwindow) - 窗口管理
- [mss](https://github.com/BoboTiG/python-mss) - 屏幕截图

## License

MIT License - see [LICENSE](LICENSE) for details.

## Author

- GitHub: [@HAKY8688](https://github.com/HAKY8688)
