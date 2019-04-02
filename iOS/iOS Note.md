---
title: iOS Note
date: 2018-10-02 09:09:09
categories: iOS
---
## iOS Note

---

### 1.WebView加载本地html

```
        let htmlFile = NSBundle.mainBundle().pathForResource("BullsEye", ofType: "html")!;
        let htmlData = NSData(contentsOfFile: htmlFile)!;
        let baseURL = NSURL.fileURLWithPath(NSBundle.mainBundle().bundlePath);
        print("htmlData =\(htmlData)");
        print("baseURL =\(baseURL)");

        webView.loadData(htmlData, MIMEType: "text/html", textEncodingName: "UTF-8", baseURL: baseURL);
```

---

## 2.WebView加载网址

```
        let url = NSURL(string: "https://www.baidu.com");
        let request = NSURLRequest(URL: url!);
        webView.loadRequest(request);
```

在info.plist添加

App Transport Security Settings

－－Allow Arbitrary Loads  -&gt; YES

---

## 3.iOS库

1.AFNetworking

轻量级而又超级高效的iOS忘了编程框架，支持iOS5.0及以上版本

2.GPUImage

处理图片框架，实时照片和视频处理，使用gpu而不是cpu，从而大大提高呈现运行效率。比苹果官方的Core Image还要快，不过缺少一些先进的功能，比如Core Image的面部识别。

3.SocketRocket

在iOS开发中和Web sockets通讯。轻松实现单一TCP连接的双工交流。但只有部分浏览器支持。

4.HocketKit & Crashlity

崩溃报告

5.JSONKit & NSJSONSerialization

高速解析JSON

6.MagicalRecord

core data操作

7.RestKit

和REST远程API整合，可以出来网络事务，解析xml或JSON，并转换成自定义的类

## Optional

一个Optional值和非Optional值的区别就在于：Optional值未经初始化虽然为nil，但普通变量连nil都没有

```
//未被初始化，但是是一个Optional类型，为nil
var str: String?
str //输出nil
//未被初始化，也不是Optional类型
var str2: String
str2    //使用时出错
```

显式拆包

```
var str: String? = "Hello World!"
str     //{Some "Hello World!"}
str!    //Hello World!
```

隐式拆包

```
var str: String! = "Hello World!"
str //Hello World!
```

## 不带参数函数

```
func funcname() -> datatype {
   return datatype
}
```

## 元组作为函数返回值

```
func minMax(array: [Int]) -> (min: Int, max: Int) {
    var currentMin = array[0]
    var currentMax = array[0]
    for value in array[1..<array.count] {
        if value < currentMin {
            currentMin = value
        } else if value > currentMax {
            currentMax = value
        }
    }
    return (currentMin, currentMax)
}

let bounds = minMax(array: [8, -6, 2, 109, 3, 71])
print("最小值为 \(bounds.min) ，最大值为 \(bounds.max)")
```

```
func minMax(array: [Int]) -> (min: Int, max: Int)? {
    if array.isEmpty { return nil }
    var currentMin = array[0]
    var currentMax = array[0]
    for value in array[1..<array.count] {
        if value < currentMin {
            currentMin = value
        } else if value > currentMax {
            currentMax = value
        }
    }
    return (currentMin, currentMax)
}
if let bounds = minMax(array: [8, -6, 2, 109, 3, 71]) {
    print("最小值为 \(bounds.min)，组大值为 \(bounds.max)")
}
```

## 可变参数

```
func vari<N>(members: N...){
    for i in members {
        print(i)
    }
}
vari(members: 4,3,5)
vari(members: 4.5, 3.1, 5.6)
vari(members: "Google", "Baidu", "Runoob")
```

### 使用函数类型

```
func sum(a: Int, b: Int) -> Int {
   return a + b
}
var addition: (Int, Int) -> Int = sum
print("输出结果: \(addition(40, 89))")
```

## 函数类型作为参数类型、函数类型作为返回类型

```
func sum(a: Int, b: Int) -> Int {
    return a + b
}
var addition: (Int, Int) -> Int = sum
print("输出结果: \(addition(40, 89))")

func another(addition: (Int, Int) -> Int, a: Int, b: Int) {
    print("输出结果: \(addition(a, b))")
}
another(addition: sum, a: 10, b: 20)
```



