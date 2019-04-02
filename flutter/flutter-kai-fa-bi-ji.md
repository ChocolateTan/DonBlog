---
title: Flutter笔记
date: 2018-10-02 09:09:09
categories: flutter
---
在Flutter中您可以通过挂接到WidgetsBinding观察并监听didChangeAppLifecycleState更改事件来监听生命周期事件

您可以监听到的生命周期事件是

* resumed - 应用程序可见并响应用户输入。这是来自Android的onResume
* inactive - 应用程序处于非活动状态，并且未接收用户输入。此事件在Android上未使用，仅适用于iOS
* paused - 应用程序当前对用户不可见，不响应用户输入，并在后台运行。这是来自Android的暂停
* suspending - 该应用程序将暂时中止。这在iOS上未使用

![](flutter_app_tree.png)

