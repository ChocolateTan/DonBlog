# Android Shot
使用这个安装包，可以用于检查 view 修改后是否和原来的页面正确，减少改动后未知的影响，避免人为错误和节省检查时间

> https://github.com/pedrovgs/Shot

## 模拟器参考配置
```
AvdId = Pixel_API_28
PlayStore.enabled = true
abi.type = x86
avd.ini.displayname = Pixel API 28
avd.ini.encoding = UTF-8
disk.dataPartition.size = 6442450944
fastboot.chosenSnapshotFile = 
fastboot.forceChosenSnapshotBoot = no
fastboot.forceColdBoot = yes
fastboot.forceFastBoot = no
hw.accelerometer = yes
hw.arc = false
hw.audioInput = yes
hw.battery = yes
hw.camera.back = virtualscene
hw.camera.front = emulated
hw.cpu.arch = x86
hw.cpu.ncore = 4
hw.dPad = no
hw.device.hash2 = MD5:55acbc835978f326788ed66a5cd4c9a7
hw.device.manufacturer = Google
hw.device.name = pixel
hw.gps = yes
hw.gpu.enabled = yes
hw.gpu.mode = auto
hw.initialOrientation = Portrait
hw.keyboard = yes
hw.lcd.density = 420
hw.lcd.height = 1920
hw.lcd.width = 1080
hw.mainKeys = no
hw.ramSize = 1536
hw.sdCard = yes
hw.sensors.orientation = yes
hw.sensors.proximity = yes
hw.trackBall = no
runtime.network.latency = none
runtime.network.speed = full
sdcard.size = 512M
showDeviceFrame = no
skin.dynamic = yes
skin.name = 1080x1920
skin.path = _no_skin
tag.display = Google Play
tag.id = google_apis_playstore
vm.heapSize = 228
```

## 执行命令
```shell
emulator @Pixel_API_28
./gradlew mobile-design:debugExecuteScreenshotTests -Precord
```