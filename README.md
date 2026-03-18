# Desktop Automation Skill

> OpenClaw / Claude Code 桌面自动化技能

[![GitHub stars](https://img.shields.io/github/stars/HAKY8688/desktop-automation-skill)](https://github.com/HAKY8688/desktop-automation-skill/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

AI 助手桌面自动化控制技能，支持鼠标、键盘、窗口管理等操作。

---

## ⚠️ 重要前提

**这个技能不能直接在 Docker 容器中运行！**

Docker 容器没有图形环境（显示器），需要将脚本安装到有桌面的机器上。

### 架构说明

```
┌─────────────────────────────────────────────────────────┐
│  正确用法: OpenClaw Node + 本地脚本                      │
├─────────────────────────────────────────────────────────┤
│                                                         │
│   飞书/Discord/Telegram                                 │
│        ↓                                                │
│   OpenClaw Gateway (Docker/服务器)                       │
│        ↓  exec 调用                                      │
│   OpenClaw Node (你的电脑，有桌面)                       │
│        ↓                                                │
│   desktop-automation.py → 控制桌面                       │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## 安装

### 1. 安装依赖

```bash
# 克隆仓库
git clone https://github.com/HAKY8688/desktop-automation-skill.git
cd desktop-automation-skill

# 给脚本添加执行权限
chmod +x scripts/*.sh scripts/*.py
```

#### macOS
```bash
pip3 install pyautogui pygetwindow mss

# 首次使用需要在系统偏好设置中允许辅助功能权限
```

#### Ubuntu/Debian Linux
```bash
sudo apt-get update
sudo apt-get install -y python3-tk python3-dev scrot xdotool wmctrl
pip3 install pyautogui pygetwindow mss
```

#### Windows
```bash
pip install pyautogui pygetwindow mss
```

---

## 在 OpenClaw 中使用

### 方式1: 通过 Node 模式（推荐）

1. 在你的电脑上安装 OpenClaw Node
2. 将脚本放到 Node 能访问的目录
3. 通过 agent 调用 exec

### 方式2: 直接调用

```bash
# 鼠标操作
python3 scripts/desktop_automation.py mouse_click 100 200
python3 scripts/desktop_automation.py mouse_move 500 500

# 键盘操作  
python3 scripts/desktop_automation.py keyboard_type "Hello World"
python3 scripts/desktop_automation.py keyboard_press enter
python3 scripts/desktop_automation.py keyboard_hotkey ctrl c

# 窗口操作
python3 scripts/desktop_automation.py window_list
python3 scripts/desktop_automation.py window_activate "Notepad"

# 截图
python3 scripts/desktop_automation.py screenshot
```

---

## 命令列表

### 鼠标操作
| 命令 | 说明 |
|------|------|
| `mouse_click <x> <y>` | 点击指定坐标 |
| `mouse_move <x> <y>` | 移动到指定坐标 |
| `mouse_drag <x1> <y1> <x2> <y2>` | 拖拽 |
| `mouse_position` | 获取当前位置 |

### 键盘操作
| 命令 | 说明 |
|------|------|
| `keyboard_type <text>` | 输入文本 |
| `keyboard_press <key>` | 按键 |
| `keyboard_hotkey <key1> <key2>` | 组合键 |

### 窗口操作
| 命令 | 说明 |
|------|------|
| `window_list` | 列出所有窗口 |
| `window_activate <title>` | 激活窗口 |
| `window_close <title>` | 关闭窗口 |
| `window_move <title> <x> <y>` | 移动窗口 |

### 其他
| 命令 | 说明 |
|------|------|
| `screenshot` | 截图 |
| `wait <seconds>` | 等待 |
| `screen_size` | 获取屏幕尺寸 |

---

## 常见问题

### Q: 为什么在 Docker 里不能用？
A: Docker 容器通常没有图形环境。需要在有桌面的机器上运行。

### Q: macOS 提示权限拒绝？
A: 需要在系统偏好设置 → 安全性与隐私 → 辅助功能 中允许 Python。

### Q: Linux 截图是黑屏？
A: 需要安装 xdotool 或使用正确的 DISPLAY 环境变量。

---

## 技术栈

- [pyautogui](https://github.com/asweigart/pyautogui) - 鼠标/键盘控制
- [pygetwindow](https://github.com/asweigart/pygetwindow) - 窗口管理
- [mss](https://github.com/BoboTiG/python-mss) - 屏幕截图

---

## License

MIT License
