# adb 命令

### 推送文件

adb -s D1CGAPE740200856 push 1.jpg /sdcard/DCIM/Camera/a1.jpg

### 刷新文件

adb shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/DCIM/Camera/a1.jpg