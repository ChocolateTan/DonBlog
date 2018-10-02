---
title: Android手势处理
date: 2018-10-02 09:09:09
categories: Android
---
### Android手势处理

> 参考：[https://my.oschina.net/gavinjin/blog/206509](#)

#### OnTouchListener与OnGestureListener的区别

两者之间的区别在于OnTouchListener获取Touch事件，通过MotionEvent处理事件（如监听到三种触摸事件，即按下，移动，松开）。OnGestureListener则能监听到双击、滑动、长按等复杂的手势操作。

