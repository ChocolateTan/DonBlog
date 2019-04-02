---
title: iOS版本控制
date: 2018-10-02 09:09:09
categories: iOS
---
1.在 user defined 設置自定義變量，在 info.plist 添加變量 如：$\(SERVER\_ADDRESS\) 對應 user-defined，通過該方法獲取

```swift
let env = Bundle.main.infoDictionary!["SERVER_ADDRESS"] as! String
```

2.建立 多個對應的 plist 文件，packing 裡設置相應

3.在 other Swift Flags 設置 -D 開頭的變量 如：-DDEV -DPRO

```swift
#if DEV
    let SERVER_URL = "http://dev.server.com/api/"
#elseif PRE
    let SERVER_URL = "http://pre/api/"
#elseif PRO
    let SERVER_URL = "http://pro.server.com/api/"
#else
    let SERVER_URL = "http://prod.server.com/api/"
#endif
```

4.object-c 通過宏定義

![](import.png)

```object-c
#if DEV

#define IS_PRODUCTON NO

#elif PRE

#define IS_PRODUCTON  NO

#else

#define IS_PRODUCTON YES

#endif

#ifdef DEBUG
#else
#define NSLog(format, ...)
#endif
```

> [https://juejin.im/entry/59cc826bf265da064c387e24](https://juejin.im/entry/59cc826bf265da064c387e24)
>
> [http://www.jianshu.com/p/d74e3756e4e6](http://www.jianshu.com/p/d74e3756e4e6)



