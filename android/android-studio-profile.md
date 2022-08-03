# Android Studio Profile

## 1、Call Chart
提供函数跟踪数据的图形表示形式。

水平轴：表示调用的时间段和时间。 垂直轴：显示被调用方。 橙色：系统API。 绿色：应用自有方法 蓝色：第三方API（包括Java API） 提示：右键点击Jump to source跳转至指定函数。

> https://juejin.cn/post/6844904035615506440


ANR超时
* Service Timeout:比如前台服务在20s内未执行完成；
* BroadcastQueue Timeout：比如前台广播在10s内未执行完成
* ContentProvider Timeout：内容提供者,在publish过超时10s;
* InputDispatching Timeout: 输入事件分发超时5s，包括按键和触摸事件。

对于Service有两类:
* 对于前台服务，则超时为SERVICE_TIMEOUT = 20s；
* 对于后台服务，则超时为SERVICE_BACKGROUND_TIMEOUT = 200s
