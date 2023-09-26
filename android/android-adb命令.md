# adb 命令

### 推送文件
```
adb -s D1CGAPE740200856 push 1.jpg /sdcard/DCIM/Camera/a1.jpg
```
### 刷新文件
```
adb shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/DCIM/Camera/a1.jpg
```
### 查看当前 Activity
```
adb shell "dumpsys activity top | grep ACTIVITY | tail -n 1"
```
### 查看当前界面Fragment
```
adb shell "dumpsys activity top | grep '#[0-9]: ' | tail -n 1"
```
### 截图并且下载到命令行当前目录
```
adb shell screencap -p /sdcard/screencap.png && adb pull /sdcard/screencap.png ./targetpath
```
### Android 清理缓存

#### 清理 main 缓存区域的日志
```
adb logcat -c
```

#### 