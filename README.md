# 捷途旅行者车机安装第三方软件教程

**在线访问**: https://jyz0501.github.io/jetour-adbtool-usage/

## 1. 教程前言

### 安装风险
- **本教程是在不破坏、不修改官方车机系统固件的基础上进行的操作，不影响车辆质保**
- **请全程按照教程所示步骤操作，禁止修改车机其他内容**
- **因自行操作而导致的车辆故障，所有后果自行负责**
- **系统稳定性风险**：安装第三方软件可能导致车机系统不稳定，出现卡顿、黑屏等问题
- **功能冲突**：部分未经测试的第三方软件可能与原厂功能产生冲突，影响行车安全（请注意分辨）

### 适用车型
- **捷途旅行者**
- **捷途山海T2**
- **捷途旅行者CDM**
- **适用系统版本**：00.04.07～00.04.12 版本所有车型

### 系统更新建议
- <font color="red"><strong>强烈不建议更新车机新系统</strong></font>：新版本系统可能会封堵第三方软件安装通道
- <font color="red"><strong>保持现有系统版本</strong></font>：如果当前系统可以正常安装第三方软件，建议保持现状


## 2. 安装方式

- 支持安卓手机安装
- 支持 Windows 电脑安装
- 支持 Mac 电脑安装

## 3. 所需工具

### 3.1 前置准备
- **车机系统**：参见 适用车型
- **数据线**：OTG功能线、手机/电脑数据线
- **第三方软件APK文件**：tools 文件夹内所用软件请提前下载到设备上
- **浏览器**：电脑/手机需要安装 EDGE 或 Chrome 浏览器
  - EDGE 浏览器：[下载链接](https://www.microsoft.com/zh-cn/microsoft-edge/download)
  - Chrome 浏览器：[下载链接](https://www.google.com/chrome)


### 3.2 推荐工具及购买链接
![配件全家福](./img/p1.jpg)

| 工具名称 | 用途 | 购买链接 |
|---------|------|----------|
| USB-A双公头数据线 | 电脑连接车机 | [京东链接1](https://item.jd.com/100002277407.html) / [京东链接2](https://item.jd.com/100000896450.html) |
| OTG数据线 | 手机连接车机 | [京东链接1](https://item.jd.com/100095234799.html) / [京东链接2](https://item.jd.com/100022896053.html) |
| 套装(USB-A+OTG) | 电脑/手机连接车机 | [抖音商城](https://v.douyin.com/IsmYFCGid8g/) |
| 应用管家 | 底层管理工具 | [下载链接](https://wcnlnks8zauh.feishu.cn/file/DM3ebTxeGojMZmx1YumcP7konWh) |

## 4. 开启车机ADB权限

**在开始安装第三方软件之前，必须先开启车机的ADB权限，否则无法通过ADB安装软件。**

1. **查看车机密码**
   - 打开 [捷途旅行者车机密码查询网站](https://jyz0501.github.io/jetour_vehicle_password/) 查看当前密码

2. **打开车机工程模式**
   - 在车机应用中心打开「无人机APP」或「旅行精灵APP」
   - 再次打开应用中心的「蓝牙电话」
   ![adb1](img/adb1.png)
   - 输入密码，进入车机工程模式
   ![adb2](img/adb2.png)

3. **开启ADB权限**
   - 在工程模式下滑找到「加密设置」或「加密项」
   ![adb3](img/adb3.png)
   - 进入加密设置，输入ADB权限密码
   ![adb4](img/adb4.png)
   - 确认ADB权限为开启状态

4. **重启车机**
   - 强制重启车机，清理缓存
   ![other2](img/other2.jpg)
   - 完成以上步骤后，继续按照下方安装步骤进行软件安装

## 5. 安卓手机安装

1. **准备工作**
   - 手机下载需要安装的第三方软件APK文件
   - 手机打开 EDGE 或 Chrome 浏览器，打开 [Tango USB Connect](https://app.tangoapp.dev) 网站
   - 使用OTG数据线连接手机和车机
   ![android1](img/android1.jpg)

2. **在线连接**
   - 在网站点击「开始使用」按钮
   - 按照网站提示完成连接
   ![android2](img/android2.jpg)
   ![android3](img/android3.jpg)
   ![android4](img/android4.jpg)
   ![android5](img/android5.jpg)
   ![android6](img/android6.jpg)

3. **上传安装包**
   - 在网站界面上传APK文件到车机 `/storage/emulated/0/temp/` 目录
   ![android7](img/android7.jpg)
   ![android8](img/android8.jpg)

4. **执行安装命令**
   - 在网站终端执行以下命令安装软件：
   ```
   pm install -r /storage/emulated/0/temp/侧边栏_1.0.apk; pm install -r /storage/emulated/0/temp/氢桌面1.2.0.3.apk; pm install -r /storage/emulated/0/temp/沙发管家4.9.54.apk; pm install -r /storage/emulated/0/temp/应用管家1.8.3.apk; am start -n com.mcar.auto.uid/com.mcar.auto.activity.IndexActivity; am start -n com.yunpan.appmanage/.ui.ActivityHome
   ```

## 6. 苹果电脑安装

1. **准备工作**
   - Mac下载需要安装的第三方软件APK文件
   - Mac打开 EDGE 或 Chrome 浏览器，打开 [Tango USB Connect](https://app.tangoapp.dev) 网站
   - 使用USB-A双公头数据线连接Mac和车机
   ![tango1](img/tango1.png)

2. **在线连接**
   - 在网站点击「开始使用」按钮
   - 按照网站提示完成连接
   - 下滑点击「我已开启USB调试模式」
   ![tango2](img/tango2.png)
   - 「选择USB方式连接」按钮
   ![tango3](img/tango3.png)
   - 点击「连接」按钮，等待车机连接
   ![tango4](img/tango4.png)
   - 允许 USB 调试 选允许
   ![tango5](img/tango5.png)
   - 按照图片提示进行
   ![tango6](img/tango6.png)
   ![tango7](img/tango7.png)

3. **上传安装包**
   - 在网站界面上传APK文件到车机 `/storage/emulated/0/temp/` 目录
   ![tango8](img/tango8.png)
   - 点击「上传」按钮，等待上传完成，上传完成后，点击+号图标，打开终端
   ![tango9](img/tango9.png)

4. **执行安装命令**
   - 在复制粘贴以下命令回车执行：
   ```
   pm install -r /storage/emulated/0/temp/侧边栏_1.0.apk; pm install -r /storage/emulated/0/temp/氢桌面1.2.0.3.apk; pm install -r /storage/emulated/0/temp/沙发管家4.9.54.apk; pm install -r /storage/emulated/0/temp/应用管家1.8.3.apk; am start -n com.mcar.auto.uid/com.mcar.auto.activity.IndexActivity; am start -n com.yunpan.appmanage/.ui.ActivityHome
   ```
   ![tango9-1](img/tango9-1.png)
   ![tang9-2](img/tang9-2.png)

## 7. Windows电脑安装

安装步骤同苹果电脑一致，在首次用浏览器打开 Tango 网站时，需要允许网站读取本机设备（在浏览器弹窗时选择允许）。
![Win1](img/Win1.jpg)

执行安装命令：
```
pm install -r /storage/emulated/0/temp/侧边栏_1.0.apk; pm install -r /storage/emulated/0/temp/氢桌面1.2.0.3.apk; pm install -r /storage/emulated/0/temp/沙发管家4.9.54.apk; pm install -r /storage/emulated/0/temp/应用管家1.8.3.apk; am start -n com.mcar.auto.uid/com.mcar.auto.activity.IndexActivity; am start -n com.yunpan.appmanage/.ui.ActivityHome
```

## 8. 共同设置

安装完成后，需要进行以下共同设置，以确保第三方软件能够正常使用：

### 8.1 配置应用管家权限
![setting1](img/setting1.png)
![setting2](img/setting2.png)
![setting3](img/setting3.png)
![setting4](img/setting4.png)

- **沙发管家无障碍权限**：进入应用管家 → 设置 → 无障碍 → 开启沙发管家
- **应用管家自动化服务**：进入应用管家 → 设置 → 自动化服务 → 开启自动化服务
- **无障碍持久保持**：进入应用管家 → 设置 → 无障碍持久保持 → 开启

### 8.2 检查侧边栏状态
确认侧边栏应用已经处于开启状态，如未开启请手动开启。

### 8.3 蓝牙遥控APP（虚拟键盘）
使用 apps 文件夹中的「蓝牙遥控」APP 实现虚拟键盘操作车机功能。通过蓝牙连接手机与车机，手机即可作为遥控器控制车机界面。

### 8.4 Apps 应用介绍

| 应用名称 | 功能介绍 |
|---------|---------|
| 悬浮球 | 快捷操作工具，支持多种快捷手势 |
| 蓝牙遥控 | 手机蓝牙连接车机，实现虚拟键盘/遥控器功能 |
| 权限狗 | 应用权限管理工具 |
| 简悬浮 Pro | 悬浮窗增强工具 |
| 易控车机版 | 车机控制工具，支持远程控制等功能 |
| Wakey | 保持屏幕常亮工具 |
| Tasker | 自动化任务工具 |
| 小横条 | 底部导航栏增强工具 |
| 百度CarLife | 手机互联映射工具 |
| Shizuku | ADB权限管理工具 |
| 旋转控制 | 屏幕旋转控制工具 |
| 甲壳虫助手 | 车机辅助工具 |
| Gesture | 手势操作工具 |
| 侧边栏Plus | 侧边栏增强工具 |

## 9. 问题解答

### 9.1 常见问题

**Q1: 手机连接不上车机是什么情况？**
A: 检查车机是否开启了「ADB」权限；必须使用 EDGE 、Chrome 浏览器或者车机助手APP连接

**Q2: ADB连接车机失败怎么办？**
A: 检查OTG线是否正常；强制重启车机后重新连接

**Q3: 执行ADB命令时出现错误怎么办？**
A: 检查APK文件是否完整，尝试重新下载；检查车机存储空间是否充足

**Q4: 安装的软件无法打开怎么办？**
A: 可能是软件与车机系统不兼容，建议尝试其他版本或类似功能的软件

**Q5: 安装后车机变得卡顿怎么办？**
A: 卸载不必要的第三方软件，清理车机缓存；实在无法解决，恢复出厂设置（谨慎操作）

**Q6: 如何卸载已安装的软件？**
A: 车机端打开「应用管家」→ 选择需要卸载的软件 → 点击「卸载」

### 9.2 进阶问题

**Q1: 是否会影响车机系统正常运行？是否影响保修？**
A: 不会，需要时可恢复出厂设置，一切重回原点。

### 免责声明

本教程是在不破坏、不修改官方车机系统固件的基础上进行的操作，不影响车辆质保。但如果因自行修改车机系统导致的问题，可能会影响保修

---

**教程版本**：v1.0
**更新时间**：2024年12月
**适用系统**：捷途旅行者、捷途山海T2、捷途旅行者CDM的00.04.07～00.04.12版本车机系统
