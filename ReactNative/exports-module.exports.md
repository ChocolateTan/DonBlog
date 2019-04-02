---
title: ReactNative 通訊 Android
date: 2018-10-02 09:09:09
categories: ReactNative
---
var a = {name: 1}; var b = a;

console.log\(a\); console.log\(b\);

[b.name](http://b.name/) = 2; console.log\(a\); console.log\(b\);

var b = {name: 3}; console.log\(a\); console.log\(b\);

运行 test.js 结果为：

{ name: 1 } { name: 1 } { name: 2 } { name: 2 } { name: 2 } { name: 3 }

**解释**：a 是一个对象，b 是对 a 的引用，即 a 和 b 指向同一块内存，所以前两个输出一样。当对 b 作修改时，即 a 和 b 指向同一块内存地址的内容发生了改变，所以 a 也会体现出来，所以第三四个输出一样。当 b 被覆盖时，b 指向了一块新的内存，a 还是指向原来的内存，所以最后两个输出不一样。

明白了上述例子后，我们只需知道三点就知道 exports 和 module.exports 的区别了：

1. module.exports 初始值为一个空对象 {}
2. exports 是指向的 module.exports 的引用
3. require\(\) 返回的是 module.exports 而不是 exports



