---
title: MAC下Homebrew基本使用
date: 2018-10-02 09:09:09
categories: iOS
---
# MAC下Homebrew基本使用

---

简介

Mac OS X是基于Unix的操作系统，可以安装大部分为Unix\/Linux开发的软件。然而，如果只是以使用为目的，对每个软件都进行手工编译不是很方便，也不利于管理已安装的软件，于是出现了类似于Linux中APT、Yum等类似的软件包管理系统，其中最著名的有MacPorts、Fink、Homebrew等。  
我曾经是MacPorts的使用者，但了解Homebrew之后，立即“弃暗投明”了。其实MacPorts也是一个很不错的解决方案，除了一个实在让我头疼的特性。MacPorts有个原则，对于软件包之间的依赖，都在MacPorts内部解决（\/opt\/local），无论系统本身是否包含了需要的库，都不会加以利用。这使得MacPorts过分的庞大臃肿，导致系统出现大量软件包的冗余，占用不小的磁盘空间，同时稍大型一点的软件编译时间都会难以忍受。  
而Homebrew的原则恰恰相反，它尽可能地利用系统自带的各种库，使得软件包的编译时间大为缩短；同时由于几乎不会造成冗余，软件包的管理也清晰、灵活了许多。Homebrew的另一个特点是使用Ruby定义软件包安装配置（叫做formula），定制非常简单。

一些命令

## **Homebrew 基本使用**

安装一个包，可以简单的运行：

```
$ brew install <package_name>
```

更新 Homebrew 在服务器端上的包目录：

```
$ brew update
```

查看你的包是否需要更新：

```
$ brew outdated
```

更新包：

```
$ brew upgrade <package_name>
```

Homebrew 将会把老版本的包缓存下来，以便当你想回滚至旧版本时使用。但这是比较少使用的情况，当你想清理旧版本的包缓存时，可以运行：

```
$ brew cleanup
```

查看你安装过的包列表（包括版本号）：

```
$ brew list --versions
```

http:\/\/wiki.jikexueyuan.com\/project\/mac-dev-setup\/homebrew.html

