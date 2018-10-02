---
title: ReactNative Silder Gesture
date: 2018-10-02 09:09:09
categories: ReactNative
---
Navigator关闭侧滑手势

```
configureScene={(rount)=>{
    var conf=Navigator.SceneConfigs.HorizontalSwipeJump;
    conf.gestures=null;
    return conf;
}}
```



