---
title: React Native Android Build Apk
date: 2018-10-02 09:09:09
categories: ReactNative
---
#### **发布更新**

发布更新之前，需要先把 js打包成 bundle，以下是anroid的做法：

**第一步** 在 工程目录里面新增 bundles文件：`mkdir bundles`

**第二步** 运行命令打包 `react-native bundle --platform 平台 --entry-file 启动文件 --bundle-output 打包js输出文件 --assets-dest 资源输出目录 --dev 是否调试`。

这是我的打包命名： `react-native bundle --platform android --entry-file index.android.js --bundle-output ./bundles/index.android.bundle --dev false`

