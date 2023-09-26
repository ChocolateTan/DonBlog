# Android 命令行创建 Emulator

```shell
// 命令行创建模拟器
sdkmanager --install "system-images;android-33;google_apis;x86_64"

avdmanager create avd -n Pixel_API_33 -k "system-images;android-33;google_apis;x86_64" -d 23

// 命令行运行模拟器
emulator @Pixel_API_33
```