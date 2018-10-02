---
title: Xamarin笔记
date: 2018-10-02 09:09:09
categories: xamarin
---
# 項目結構

建立 Forms 應用之後，能創建 android 和 iOS 的應用項目，下圖解決方案裡有三個項目第一個是 Forms，是共用與 android 和 iOS 兩個平台的源碼；.Droid 是 android 項目，單獨對 android 項目使用的源碼，是 C\# 編程，可以使用 xml 佈局文件，樣式資源文件等；.iOS 是 iOS 項目，同樣使用 C\# 編程，可以通過 storyboard 構建頁面邏輯。

![](/assets/xamarin_project_structure.png)



