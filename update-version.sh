#!/bin/bash

# 获取 git 提交次数
COMMIT_COUNT=$(git rev-list --count HEAD)

# 生成版本号（基于提交次数）
VERSION="v1.$COMMIT_COUNT.0"

# 更新 index.html 中的版本号
sed -i.bak "s|<span id=\"app-version\"[^>]*>.*</span>|<span id=\"app-version\" style=\"font-size: 12px; color: #999;\">$VERSION</span>|" index.html

# 删除备份文件
rm -f index.html.bak

echo "版本号已更新为: $VERSION"
