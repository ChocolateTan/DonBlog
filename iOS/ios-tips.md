---
title: iOS status bar
date: 2018-10-02 09:09:09
categories: iOS
---
### 在Info中将Status bar is initially hidden\(UIStatusBarHidden\)对应的Value设置为Yes，没有变化

设置statusBar的【前景部分】

简单来说，就是设置显示电池电量、时间、网络部分标示的颜色， 这里只能设置两种颜色：

默认的黑色（UIStatusBarStyleDefault）  
白色（UIStatusBarStyleLightContent）  
可以设置的地方有两个：plist设置里面 和 程序代码里  
初始化设置:导航栏设置为不透明并给了"标题"与状态栏文字作对比

改变状态栏的方法

方法一:

1、plist

View controller-based status bar appearance 设置为 NO

2、代码设置

```
[UIApplication sharedApplication].statusBarStyle = UIStatusBarStyleLightContent;
```

方法二:

1、plist

View controller-based status bar appearance 设置为 YES 或者默认\(不设置\)

注意:

如果View controller-based status bar appearance为YES。

则\[UIApplication sharedApplication\].statusBarStyle 无效。

2、代码设置

```
self.navigationController.navigationBar.barStyle = UIBarStyleBlack;
```

\(二\)设置statusBar的【背景部分】

1、系统提供的方法

navigationBar的setBarTintColor接口，用此接口可改变statusBar的背景色

```
self.navigationController.navigationBar.barTintColor = [UIColor greenColor];
```

### 使用ui preview功能

1.点开Main.storyboard；

2.点击view-》Assistant Editor-》Show Assistant Editor，编辑区分成两部分；

3.点击右半部分顶部导航栏Automatic，在弹出菜单最下面选择Preview-》Main.storyboard（Preview）。

Preview界面的左下角的+号可以添加不同尺寸的屏幕，鼠标移到视图上可以选择旋转。

### Aspect Ratio

添加约束，解决屏幕适配被拉伸等问题







