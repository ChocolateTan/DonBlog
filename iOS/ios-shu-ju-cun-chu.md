---
title: NSUserDefaults存储数据
date: 2018-10-02 09:09:09
categories: iOS
---
### NSUserDefaults存储数据

一般我们拿它用来保存应用程序设置和属性、用户保存的数据,用户的手机不管是关机or开机时候都会保存在本地\(除非你把他删除了\),它一般可以存储类型包括:字符,数组,字典,NSData,NSNumber以及基本数据类型都可.

### write写入方式存储为plist属性列表

write写入方式也是一种把数据永久保存在磁盘中储存方式,一般步骤:1\)获取路径\(一般有两种方式:使用NSSearchPathForDirectoriesInDomains或URLsForDirectory;使用NSHomeDirectory➕相应的路径\);2\)向文件中写入数据;3\)从文件中读取数据.

### NSKeyedArchiver采用归档的形式来保存数据

NSKeyedArchiver保存数据对象需要遵守NSCoding协议，并且该对象对应的类必须提供encodeWithCoder:和initWithCoder:方法,简单的说就是告诉系统怎么对对象进行编码，怎么对对象进行解码.

