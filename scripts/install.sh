#!/bin/bash
# 桌面自动化工具安装脚本

echo "正在安装桌面自动化依赖..."

# 检查系统
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    sudo apt-get update
    sudo apt-get install -y python3-tk python3-dev scrot
    pip3 install pyautogui pygetwindow mss
elif [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    pip3 install pyautogui pygetwindow mss
elif [[ "$OSTYPE" == "cygwin" ]] || [[ "$OSTYPE" == "msys" ]]; then
    # Windows
    pip install pyautogui pygetwindow mss
fi

echo "安装完成！"
echo ""
echo "测试运行:"
python3 /path/to/desktop_automation.py --help
