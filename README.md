# 捷途旅行者车机安装第三方软件教程

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

### 2.1 安卓手机安装
- **优势**：操作简单，无需额外设备

### 2.2 Windows电脑安装
- **优势**：传输速度快，支持批量安装

### 2.3 苹果电脑安装（无Windows电脑、安卓手机人群）
- **劣势**：需要安装额外工具，配置安装环境、操作相对复杂

## 3. 所需工具

### 3.1 前置准备
- **车机系统**：参见 适用车型
- **数据线**：OTG功能线、手机/电脑数据线
- **第三方软件APK文件**：《必备软件》文件夹内所用软件请提前下载到设备上


### 3.2 推荐工具及购买链接
![配件全家福](./img/p1.jpg)

| 工具名称 | 用途 | 购买链接 |
|---------|------|----------|
| USB-A双公头数据线 | 电脑连接车机 | [京东链接1](https://item.jd.com/100002277407.html) / [京东链接2](https://item.jd.com/100000896450.html) |
| OTG数据线 | 手机连接车机 | [京东链接1](https://item.jd.com/100095234799.html) / [京东链接2](https://item.jd.com/100022896053.html) |
| 套装(USB-A+OTG) | 电脑/手机连接车机 | [抖音商城](https://v.douyin.com/IsmYFCGid8g/) |
| 应用管家 | 底层管理工具 | [下载链接](https://file.vju.cc/%E5%BA%94%E7%94%A8%E7%AE%A1%E5%AE%B6/%E5%BA%94%E7%94%A8%E7%AE%A1%E5%AE%B61.8.0%E5%85%AC%E7%AD%BE%E7%89%88.apk) |

## 4. 安装步骤

### 4.0 开启车机ADB权限（必须步骤）

**在开始安装第三方软件之前，必须先开启车机的ADB权限，否则无法通过ADB安装软件。**

1. **查看车机密码**
   - 打开 [捷途旅行者车机密码查询网站](https://jyz0501.github.io/jetour_vehicle_password/) 查看当前密码

2. **打开车机工程模式**
   - 在车机应用中心打开「无人机APP」或「旅行精灵APP」
   - 再次打开应用中心的「蓝牙电话」
   - 输入密码，进入车机工程模式

3. **开启ADB权限**
   - 在工程模式下滑找到「加密设置」或「加密项」
   - 进入加密设置，输入ADB权限密码
   - 确认ADB权限为开启状态

4. **重启车机**
   - 强制重启车机
   - 完成以上步骤后，继续按照下方安装步骤进行软件安装

### 4.1 ADB 安装方式（推荐）
![使用建议图](./img/p2.jpg)

#### 4.1.1 安卓手机安装步骤
1. **准备工作**
   - 手机下载需要安装的第三方软件APK文件
   - 手机打开 EDGE 或 Chrome 浏览器，打开 [Tango USB Connect](https://app.tangoapp.dev/connect/usb) 网站
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
   pm install -r /storage/emulated/0/temp/侧边栏1.0.apk; pm install -r /storage/emulated/0/temp/氢桌面.apk; pm install -r /storage/emulated/0/temp/沙发管家4.9.54.apk; pm install -r /storage/emulated/0/temp/应用管家1.8.3.apk; am start -n com.mcar.auto.uid/com.mcar.auto.activity.IndexActivity; am start -n com.yunpan.appmanage/.ui.ActivityHome
   ```

#### 4.1.2 Windows电脑安装步骤
1. **准备工作**
   - 电脑下载需要安装的第三方软件APK文件
   - 电脑打开 EDGE 或 Chrome 浏览器，打开 [Tango USB Connect](https://app.tangoapp.dev/connect/usb) 网站
   - 使用USB-A双公头数据线连接电脑和车机

2. **在线连接**
   - 在网站点击「开始使用」按钮
   - 按照网站提示完成连接

3. **上传安装包**
   - 在网站界面上传APK文件到车机 `/storage/emulated/0/temp/` 目录

4. **执行安装命令**
   - 在网站终端执行以下命令安装软件：
   ```
   pm install -r /storage/emulated/0/temp/侧边栏1.0.apk; pm install -r /storage/emulated/0/temp/氢桌面.apk; pm install -r /storage/emulated/0/temp/沙发管家4.9.54.apk; pm install -r /storage/emulated/0/temp/应用管家1.8.3.apk; am start -n com.mcar.auto.uid/com.mcar.auto.activity.IndexActivity; am start -n com.yunpan.appmanage/.ui.ActivityHome
   ```

#### 4.1.3 苹果电脑安装步骤
1. **准备工作**
   - Mac下载需要安装的第三方软件APK文件
   - Mac打开 EDGE 或 Chrome 浏览器，打开 [Tango USB Connect](https://app.tangoapp.dev/connect/usb) 网站
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
   pm install -r /storage/emulated/0/temp/侧边栏1.0.apk; pm install -r /storage/emulated/0/temp/氢桌面.apk; pm install -r /storage/emulated/0/temp/沙发管家4.9.54.apk; pm install -r /storage/emulated/0/temp/应用管家1.8.3.apk; am start -n com.mcar.auto.uid/com.mcar.auto.activity.IndexActivity; am start -n com.yunpan.appmanage/.ui.ActivityHome
   ```
   ![tango9-1](img/tango9-1.png)
   ![tang9-2](img/tang9-2.png)

### 4.2 其他安装方式

#### 4.2.1 U盘安装方式
1. **准备工作**
   - 将需要安装的APK文件复制到U盘中

2. **连接车机**
   - 将U盘通过OTG线连接到车机

3. **安装软件**
   - 车机端打开文件管理器
   - 找到U盘中的APK文件并点击安装
   - 按照提示完成安装

#### 4.2.2 WiFi传输安装方式
1. **准备工作**
   - 安卓手机下载需要安装的APK文件

2. **连接车机**
   - 打开车机WiFi热点
   - 手机连接车机WiFi

3. **传输文件**
   - 使用手机文件管理器找到下载的APK文件
   - 通过WiFi传输功能将APK文件发送到车机

4. **安装软件**
   - 车机端打开文件管理器
   - 找到传输的APK文件并点击安装
   - 按照提示完成安装

## 5. 问题解答

### 5.1 常见问题

**Q1: 车机无法安装第三方软件怎么办？**
A: 检查车机是否开启了「未知来源应用安装」权限，路径：设置 → 安全与隐私 → 未知来源应用安装

**Q2: ADB连接车机失败怎么办？**
A: 检查USB数据线是否正常；重启车机和电脑后重新连接

**Q3: 执行ADB命令时出现错误怎么办？**
A: 检查ADB工具是否正确安装；确认设备已正确连接（`adb devices`命令应显示设备）；尝试使用管理员权限运行命令提示符/终端

**Q4: 安装过程中出现错误提示怎么办？**
A: 检查APK文件是否完整，尝试重新下载；检查车机存储空间是否充足

**Q5: 安装后软件无法运行怎么办？**
A: 可能是软件与车机系统不兼容，建议尝试其他版本或类似功能的软件

**Q6: 安装后车机变得卡顿怎么办？**
A: 卸载不必要的第三方软件，清理车机缓存；恢复出厂设置（谨慎操作）

**Q7: 如何卸载已安装的第三方软件？**
A: 车机端打开「设置」→「应用管理」→ 选择需要卸载的软件 → 点击「卸载」

### 5.2 高级问题

**Q1: 如何获取车机Root权限？**
A: 不建议获取Root权限，可能导致系统崩溃，影响车辆正常功能

**Q2: 如何备份车机系统？**
A: 可以使用ADB命令进行备份，具体命令：`adb backup -all -f backup.ab`

**Q3: 车机系统更新后无法安装第三方软件怎么办？**
A: 等待民间破解方法，或尝试降级系统（风险较高）

**Q4: 安装第三方软件会影响车辆保修吗？**
A: 本教程是在不破坏、不修改官方车机系统固件的基础上进行的操作，不影响车辆质保。但如果因自行修改车机系统导致的问题，可能会影响保修

**Q5: 如何解决软件分辨率不匹配的问题？**
A: 下载适配车机屏幕分辨率的软件版本，或使用屏幕适配工具

## 免责声明

本教程是在不破坏、不修改官方车机系统固件的基础上进行的操作，不影响车辆质保。请全程按照教程所示步骤操作，禁止修改车机其他内容。因自行操作而导致的车辆故障，所有后果自行负责。

本教程仅供参考，安装第三方软件存在一定风险。操作过程中如出现任何问题，与本教程作者无关。请谨慎操作，风险自担。

---

**教程版本**：v1.0
**更新时间**：2024年12月
**适用系统**：捷途旅行者、捷途山海T2、捷途旅行者CDM的00.04.07～00.04.12版本车机系统