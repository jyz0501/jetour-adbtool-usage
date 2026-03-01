#!/bin/bash

COMMIT_COUNT=$(git rev-list --count HEAD)

VERSION="v1.${COMMIT_COUNT}.0"

sed -i '' "s/<span id=\"app-version\" style=\"font-size: 12px; color: #999;\">.*<\/span>/<span id=\"app-version\" style=\"font-size: 12px; color: #999;\">${VERSION}<\/span>/" index.html

echo "版本号已更新为: ${VERSION}"
