# Desktop Automation Skill

> OpenClaw / Claude Code 桌面自动化技能

[![GitHub stars](https://img.shields.io/github/stars/HAKY8688/desktop-automation-skill)](https://github.com/HAKY8688/desktop-automation-skill/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

AI 助手桌面自动化控制技能，支持鼠标、键盘、窗口管理等操作。

---

## ⚠️ 重要前提

**这个技能必须在有桌面的电脑上运行，不能在 Docker 容器中！**

### 架构说明

```
┌─────────────────────────────────────────────────────────────────┐
│                    正确使用架构                                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   飞书 / Discord / Telegram / WhatsApp                         │
│          ↓                                                       │
│   OpenClaw Gateway (服务器/Docker)                               │
│          ↓  配对后通过 WebSocket 通信                            │
│   OpenClaw Node (你的电脑，有桌面)                               │
│          ↓                                                       │
│   desktop-automation.py → 控制桌面                               │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**关键点：**
- Gateway 可以在服务器/Docker 上运行
- Node 必须在有桌面的电脑上运行（macOS/Windows/Linux）
- 两者通过 WebSocket 配对连接

---

## 📦 快速开始

### 步骤 1: 在有桌面的电脑上安装 OpenClaw Node

```bash
# 安装 Node.js（如果没有）
# macOS: brew install node
# Linux: apt install nodejs
# Windows: https://nodejs.org/

# 安装 OpenClaw
npm install -g openclaw

# 启动 Node（会显示配对码）
openclaw node start
```

启动后会显示一个配对码（如 `ABC-123`），记录下来。

### 步骤 2: 在 Gateway 端批准配对

在运行 Gateway 的服务器上：

```bash
# 查看待配对设备
openclaw devices list

# 批准配对
openclaw devices approve <配对码>
```

### 步骤 3: 安装桌面自动化脚本

在 Node 所在的电脑上：

```bash
# 克隆仓库
git clone https://github.com/HAKY8688/desktop-automation-skill.git
cd desktop-automation-skill

# 安装依赖
chmod +x scripts/install.sh
./scripts/install.sh
```

#### macOS 额外设置
- 首次使用需要在系统偏好设置 → 安全性与隐私 → 辅助功能 中允许 Python

#### Linux 额外设置
```bash
sudo apt-get install -y python3-tk python3-dev scrot xdotool wmctrl
```

#### Windows
- 需要安装 Python: https://www.python.org/
- 然后运行: `pip install pyautogui pygetwindow mss`

---

## 🔧 配置 Gateway 使用 Node

在 Gateway 配置文件中添加：

```json5
{
  "tools": {
    "exec": {
      "node": "你的电脑名称"
    }
  }
}
```

或通过命令行设置：
```bash
openclaw config set agents.defaults.tools.exec.node "你的电脑名称"
```

---

## 📖 使用示例

### 通过飞书/Discord/Telegram 发送指令

```
用户: 帮我打开记事本并输入 "Hello World"

AI → Gateway → Node → desktop-automation.py
                      ↓
              1. keyboard_press win
              2. keyboard_type notepad
              3. keyboard_press enter
              4. keyboard_type "Hello World"
```

### 直接命令行调用

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

## 📋 命令列表

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

## ❓ 常见问题

### Q: 为什么在 Docker 里不能用？
A: Docker 容器通常没有图形环境（X11/Wayland），无法控制桌面。必须在有桌面的电脑上运行 Node。

### Q: macOS 提示权限拒绝？
A: 需要在系统偏好设置 → 安全性与隐私 → 辅助功能 中允许 Python/自动化。

### Q: Linux 截图是黑屏？
A: 确保 DISPLAY 环境变量正确，或使用 xdotool。

### Q: 配对码在哪里输入？
A: 在运行 Gateway 的服务器上，使用 `openclaw devices approve <配对码>` 命令批准。

---

## 🔧 故障排除

### Node 无法连接 Gateway
1. 检查网络是否互通
2. 确认 Gateway 地址配置正确
3. 检查防火墙是否阻止 WebSocket 端口

### 权限问题
- macOS: 系统偏好设置 → 安全性与隐私 → 辅助功能
- Linux: 可能需要 sudo 或调整 X11 权限

### 依赖缺失
```bash
# 检查 Python 包
pip3 list | grep -E "pyautogui|pygetwindow|mss"
```

---

## 📁 文件结构

```
desktop-automation-skill/
├── README.md                    # 本文件
├── SKILL.md                     # OpenClaw Skill 定义
├── LICENSE                      # MIT 许可证
└── scripts/
    ├── desktop_automation.py    # 桌面自动化主程序
    ├── install.sh              # 依赖安装脚本
    └── install-node.sh         # Node 安装脚本
```

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

---

## License

MIT License
