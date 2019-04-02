---
title: ReactNative 通訊 Android
date: 2018-10-02 09:09:09
categories: ReactNative
---
#### Headless JS

Headless JS是一种使用js在后台执行任务的方法。它可以用来在后台同步数据、处理推送通知或是播放音乐等等。

#### JS端的API

首先我们要通过`AppRegistry`来注册一个async函数，这个函数我们称之为“任务”。注册方式类似在index.js中注册RN应用：

```js
AppRegistry.registerHeadlessTask('SomeTaskName', () => require('SomeTaskName'));
```

然后创建require对应的`SomeTaskName.js`文件:

```js
module.exports = async (taskData) => {
  // 要做的事情
}
```

可以在任务中处理任何事情（网络请求、定时器等等），但唯独不要涉及用户界面！在任务完成后（例如在promise中调用resolve），RN会进入一个“暂停”模式，直到有新任务需要执行或者是应用回到前台。



#### Java端的API

继承`HeadlessJsTaskService`，然后覆盖`getTaskConfig`方法的实现：

```js
public class MyTaskService extends HeadlessJsTaskService {

  @Override
  protected @Nullable HeadlessJsTaskConfig getTaskConfig(Intent intent) {
    Bundle extras = intent.getExtras();
    if (extras != null) {
      return new HeadlessJsTaskConfig(
          "SomeTaskName",
          Arguments.fromBundle(extras),
          5000);
    }
    return null;
  }
}
```



