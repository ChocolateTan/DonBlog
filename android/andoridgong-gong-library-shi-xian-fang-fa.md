---
title: Android Library
date: 2018-10-02 09:09:09
categories: Android
---
[http://www.jianshu.com/p/f664ebc03d93](http://www.jianshu.com/p/f664ebc03d93)

[http://www.wxtlife.com/2015/12/17/Android-studio-quote-same-lib/](http://www.wxtlife.com/2015/12/17/Android-studio-quote-same-lib/)

第一种方法是对library向每个引用的项目建立软连接。这样修改就会对每个引用同步修改.这种方法就是看起来会很臃肿，如果要引用多个library就很痛苦。

第二种就是maven 仓库的方式，将所有的library都上传到maven仓库，然后在各个工程中进行引用，当然这种是对稳定的library来说是最好的一种方式，但对于library需要开发和修改的就不太适合了。



第三种就是将所以的library作为一个工程使用，然后将所有的library都放入此工程中，然后在其他引用library的工程中，引入新建的工程，这样看起来和eclipse 引用library的结构就很像了，且可以放入多个library都不影响。下面就来看看这种解决方法，该如何实现。

首先新建一个工程，注意是工程，不是Studio里面的Module，起一个容易理解的工程名称CommonLibrary

将需添加的library添加进CommonLibrary中，记得每个library也是需要有

1. `build.gradle`
   文件的，且配置项正确。
2. 在需要引用的的工程中，需要在`settings.gradle`文件中添加引用代码如下：

```
include ':CommonLibrary'
```

```
project (':CommonLibrary').projectDir = new File('../CommonLibrary/')
include ':CommonLibrary:CommonsA'
```

其中CommonsA为项目要使用的公共library名称

然后在我们项目实际的model中修改`build.gradle`文件，需要在`dependencies`中添加下面的代码。CommonsA和CommonsB都是要要引用的项目。

compile project (':CommonLibrary:CommonsA')

compile project (':CommonLibrary:CommonsB')

