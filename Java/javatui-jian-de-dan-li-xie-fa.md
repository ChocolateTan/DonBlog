---
title: 饿汉式 static final field
date: 2018-10-02 09:09:09
categories: Java
---
## 饿汉式 static final field

这种方法非常简单，因为单例的实例被声明成 static 和 final 变量了，在第一次加载类到内存中时就会初始化，所以创建实例本身是线程安全的。

```java
publicclassSingleton{
//类加载时就初始化
privatestaticfinal Singleton instance = new Singleton();

privateSingleton(){}

publicstatic Singleton getInstance(){
return instance;
    }
}

```

这种写法如果完美的话，就没必要在啰嗦那么多双检锁的问题了。缺点是它不是一种懒加载模式（lazy initialization），单例会在加载类后一开始就被初始化，即使客户端没有调用 getInstance\(\)方法。饿汉式的创建方式在一些场景中将无法使用：譬如 Singleton 实例的创建是依赖参数或者配置文件的，在 getInstance\(\) 之前必须调用某个方法设置参数给它，那样这种单例写法就无法使用了。

## 静态内部类 static nested class

```java
publicclassSingleton{  
privatestaticclassSingletonHolder{  
privatestaticfinal Singleton INSTANCE = new Singleton();  
    }  
privateSingleton(){}  
publicstaticfinal Singleton getInstance(){  
return SingletonHolder.INSTANCE; 
    }  
}
```

我比较倾向于使用静态内部类的方法，这种方法也是《Effective Java》上所推荐的。

这种写法仍然使用JVM本身机制保证了线程安全问题；由于 SingletonHolder 是私有的，除了 getInstance\(\) 之外没有办法访问它，因此它是懒汉式的；同时读取实例的时候不会进行同步，没有性能缺陷；也不依赖 JDK 版本。

