#!/bin/bash
# OpenClaw Node 安装脚本 - 在有桌面的电脑上运行

echo "=== OpenClaw Node 安装脚本 ==="
echo ""

# 检查系统
if [[ "$OSTYPE" == "darwin"* ]]; then
    echo "检测到 macOS"
    echo ""
    echo "安装方法："
    echo "1. 安装 Node.js: https://nodejs.org/"
    echo "2. 运行: npm install -g openclaw"
    echo "3. 运行: openclaw node start"
    
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "检测到 Linux"
    echo ""
    # 安装 Node.js
    curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
    sudo apt-get install -y nodejs
    sudo npm install -g openclaw
    
    echo ""
    echo "安装完成！运行以下命令启动 Node："
    echo "openclaw node start"
    
elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "cygwin" ]]; then
    echo "检测到 Windows"
    echo ""
    echo "安装方法："
    echo "1. 安装 Node.js: https://nodejs.org/"
    echo "2. 打开 PowerShell，运行: npm install -g openclaw"
    echo "3. 运行: openclaw node start"
fi

echo ""
echo "=== 启动 Node 后 ==="
echo "1. 会显示一个配对码"
echo "2. 告诉我配对码，我在 Gateway 端批准"
echo "3. 确认连接后，桌面自动化就能用了！"
