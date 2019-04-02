---
title: Ubuntu配置Tomcat
date: 2018-10-02 09:09:09
categories: Java
---
# Ubuntu配置Tomcat

> 参考：
>
> [http://blog.csdn.net/njchenyi/article/details/46641141](http://blog.csdn.net/njchenyi/article/details/46641141)
>
> [http://blog.csdn.net/upshi/article/details/54907464](http://blog.csdn.net/upshi/article/details/54907464)

近段时间入手了一部国外虚拟服务器，在配置Tomcat时，出现了个汇总BUG。每次启动Tomcat的startup.sh都正常，但是打开8080却不能访问，而且logs下文件没有报错。尝试过解压和APT安装都是同样结果，后来在其他大神帮助下终於解决了。

找到jdk1.x.x\_xx/jre/lib/security/java.security文件，在文件中找到securerandom.source这个设置项，将其改为：securerandom.source=file:/dev/./urandom这时候根据修改内容就可以查到因为此原因不仅可以造成tomcat卡住，也会造成weblogic启动缓慢，linux或者部分unix系统提供随机数设备是/dev/random 和/dev/urandom ，两个有区别，urandom安全性没有random高，但random需要时间间隔生成随机数。jdk默认调用random。

产生原因应该是：/dev/random是一个阻塞数字生成器，如果它没有足够的随机数据提供，它就一直等，这迫使JVM等待。

