# Desktop Automation Skill

AI 助手桌面自动化控制技能，支持鼠标、键盘、窗口管理等操作。

## 功能

当用户需要：
- 自动化操作桌面应用
- 模拟鼠标点击、移动、拖拽
- 模拟键盘输入
- 管理窗口（获取、切换、关闭）
- 截图
- 等待/延时

## 技能命令

### 鼠标操作
- `mouse click <x> <y>` - 点击指定坐标
- `mouse move <x> <y>` - 移动到指定坐标
- `mouse drag <x1> <y1> <x2> <y2>` - 拖拽
- `mouse position` - 获取当前位置

### 键盘操作
- `keyboard type <text>` - 输入文本
- `keyboard press <key>` - 按键（如 Enter, Escape, Ctrl+C）
- `keyboard hotkey <key1> <key2> ...` - 组合键

### 窗口操作
- `window list` - 列出所有窗口
- `window get <title>` - 获取窗口信息
- `window activate <title>` - 激活窗口
- `window close <title>` - 关闭窗口
- `window move <title> <x> <y>` - 移动窗口
- `window size <title> <width> <height>` - 调整窗口大小

### 截图
- `screenshot` - 截取整个屏幕
- `screenshot <x> <y> <width> <height>` - 截取区域

### 其他
- `wait <seconds>` - 等待秒数

## 使用示例

"帮我打开记事本并输入 hello"
"截个图"
"点击屏幕中央的按钮"
"打开微信"

## 依赖

需要在本地安装：
```bash
pip install pyautogui pygetwindow mss
```

注意：Linux 需要安装：
```bash
sudo apt-get install python3-tk python3-dev
```
