---
title: Android CMake
date: 2018-10-02 09:09:09
categories: Android
---
> ##### 参考：[http://wl9739.github.io/2016/09/21/%E5%9C%A8-Android-Studio-2-2-%E4%B8%AD%E6%84%89%E5%BF%AB%E5%9C%B0%E4%BD%BF%E7%94%A8-C-C-md/](http://wl9739.github.io/2016/09/21/%E5%9C%A8-Android-Studio-2-2-%E4%B8%AD%E6%84%89%E5%BF%AB%E5%9C%B0%E4%BD%BF%E7%94%A8-C-C-md/)

#### 简介

> 注意：要在 Android Studio 中使用 CMake 或者 ndk-build，需要使用 Android Studio 2.2 或更高的版本，同时需要配合使用 Android Plugin for Gradle 2.2.0 及以上的版本。

`The Android Native Development Kit (NDK)`

* : 让你能在 Android 上面使用 C 和 C++ 代码的工具集。
* `CMake`: 外部构建工具。如果你准备只使用 ndk-build 的话，可以不使用它。
* `LLDB`: Android Studio 上面调试本地代码的工具。

> 注意：**Instant Run**并不兼容使用了 native code 的项目。Android Studio 会自动禁止**Instant Run**功能。

#### 编译过程

1. Gradle 调用外部构建脚本，也就是**CMakeLists.txt**。
2. CMake 会根据构建脚本的指令去编译一个 C++ 源文件，也就是`native-lib.cpp`，并将编译后的产物扔进共享对象库中，并将其命名为**libnative-lib.so**，然后 Gradle 将其打包到 APK 中。
3. 在运行期间，APP 的 MainActivity 会调用`System.loadLibrary()`方法，加载 native library。而这个库的原生函数，`stringFromJNI()`，就可以为 APP 所用了。
4. MainActivity.onCreate\(\) 方法会调用`stringFromJNI()`，然后返回 “Hello from C++”，并更新 TextView 的显示。

#### 将 C/C++ 代码添加到现有的项目中

如果你想将 native code 添加到一个现有的项目中，请按照下面的步骤操作：

1. 创建新的 native source 文件，并将其添加到你的 Android Studio 项目中。如果你已经有了 native code，也可以跳过这一步。
2. 创建一个 CMake 构建脚本。如果你已经有了一个 CMakeLists.txt 构建脚本，或者你想使用 ndk-build 然后有一个 Android.mk 构建脚本，也可以跳过这一步。
3. 将你的 native library 与 Gradle 关联起来。Gradle 使用构建脚本将源码导入到你的 Android Studio 项目中，并且将你的 native library （也就是 .so 文件）打包到 APK 中。

一旦你配置好了项目，你就可以在 Java 代码中，使用 JNI 框架开调用原生函数（native functions）。只需要点击**Run**按钮，就可以编译运行你的 APP 了。

