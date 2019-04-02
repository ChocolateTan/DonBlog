---
title: ReactNative UI Size
date: 2018-10-02 09:09:09
categories: ReactNative
---
#### 指定宽高（dp pt）

最简单的给组件设定尺寸的方式就是在样式中指定固定的`width`和`height`。React Native中的尺寸都是无单位的，表示的是与设备像素密度无关的逻辑像素点

```js
import React, { Component } from 'react';
import { AppRegistry, View } from 'react-native';

class FixedDimensionsBasics extends Component {
  render() {
    return (
      <View>
        <View style={{width: 50, height: 50, backgroundColor: 'powderblue'}} />
        <View style={{width: 100, height: 100, backgroundColor: 'skyblue'}} />
        <View style={{width: 150, height: 150, backgroundColor: 'steelblue'}} />
      </View>
    );
  }
};
// 注册应用(registerComponent)后才能正确渲染
// 注意：只把应用作为一个整体注册一次，而不是每个组件/模块都注册
AppRegistry.registerComponent('AwesomeProject', () => FixedDimensionsBasics);
```

#### 弹性（Flex）宽高

在组件样式中使用`flex`可以使其在可利用的空间中动态地扩张或收缩。一般而言我们会使用`flex:1`来指定某个组件扩张以撑满所有剩余的空间。如果有多个并列的子组件使用了`flex:1`，则这些子组件会平分父容器中剩余的空间。如果这些并列的子组件的`flex`值不一样，则谁的值更大，谁占据剩余空间的比例就更大（即占据剩余空间的比等于并列组件间`flex`值的比）。

> 组件能够撑满剩余空间的前提是其父容器的尺寸不为零。如果父容器既没有固定的`width`和`height`，也没有设定`flex`，则父容器的尺寸为零。其子组件如果使用了`flex`，也是无法显示的。

```js
import React, { Component } from 'react';
import { AppRegistry, View } from 'react-native';

class FlexDimensionsBasics extends Component {
  render() {
    return (
      // 试试去掉父View中的`flex: 1`。
      // 则父View不再具有尺寸，因此子组件也无法再撑开。
      // 然后再用`height: 300`来代替父View的`flex: 1`试试看？
      <View style={{flex: 1}}>
        <View style={{flex: 1, backgroundColor: 'powderblue'}} />
        <View style={{flex: 2, backgroundColor: 'skyblue'}} />
        <View style={{flex: 3, backgroundColor: 'steelblue'}} />
      </View>
    );
  }
};

AppRegistry.registerComponent('AwesomeProject', () => FlexDimensionsBasics);
```

#### Flex Direction

```js
//水平轴(row)
//竖直轴(column)
import React, { Component } from 'react';
import { AppRegistry, View } from 'react-native';

class FlexDirectionBasics extends Component {
  render() {
    return (
      // 尝试把`flexDirection`改为`column`看看
      <View style={{flex: 1, flexDirection: 'row'}}>
        <View style={{width: 50, height: 50, backgroundColor: 'powderblue'}} />
        <View style={{width: 50, height: 50, backgroundColor: 'skyblue'}} />
        <View style={{width: 50, height: 50, backgroundColor: 'steelblue'}} />
      </View>
    );
  }
};

AppRegistry.registerComponent('AwesomeProject', () => FlexDirectionBasics);
```

#### Justify Content

主轴的排列方式\(`flex-start`、`center`、`flex-end`、`space-around`以及`space-between`\)

```js
import React, { Component } from 'react';
import { AppRegistry, View } from 'react-native';

class JustifyContentBasics extends Component {
  render() {
    return (
      // 尝试把`justifyContent`改为`center`看看
      // 尝试把`flexDirection`改为`row`看看
      <View style={{
        flex: 1,
        flexDirection: 'column',
        justifyContent: 'space-between',
      }}>
        <View style={{width: 50, height: 50, backgroundColor: 'powderblue'}} />
        <View style={{width: 50, height: 50, backgroundColor: 'skyblue'}} />
        <View style={{width: 50, height: 50, backgroundColor: 'steelblue'}} />
      </View>
    );
  }
};

AppRegistry.registerComponent('AwesomeProject', () => JustifyContentBasics);
```

#### Align Items

子元素沿着次轴



