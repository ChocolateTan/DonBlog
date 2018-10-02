---
title: ReactNative UI
date: 2018-10-02 09:09:09
categories: ReactNative
---
#### 关于尺寸单位

React Native中的尺寸都是无单位的，表示的是与设备像素密度无关的逻辑像素点。（讲甘多就系dp pt）

```js
<View style={{width:100,height:100,margin:40,backgroundColor:'gray'}}>
        <Text style={{fontSize:16,margin:20}}>尺寸</Text>
</View>
```

上述代码，运行在Android上时，View的长和宽被解释成：100dp 100dp单位是dp，字体被解释成16sp 单位是sp，运行在iOS上时尺寸单位被解释称了pt，这些单位确保了在任何不同dpi的手机屏幕上显示不会发生改变；

#### 指定宽高

dp设置尺寸

```js
<View>
    <View style={{width: 50, height: 50, backgroundColor: 'powderblue'}} />
    <View style={{width: 100, height: 100, backgroundColor: 'skyblue'}} />
    <View style={{width: 150, height: 150, backgroundColor: 'steelblue'}} />
</View>
```

#### 弹性（Flex）宽高

就是比例分配

```js
<Text style={[styles.text, styles.header]}>
    根节点上放一个元素，不设置宽度
</Text>

<View style={{height: 20, backgroundColor: '#333333'}} />

<Text style={[styles.text, styles.header]}>
    固定宽度的元素上放一个View，不设置宽度
</Text>

<View style={{width: 100}}>
    <View style={{height: 20, backgroundColor: '#333333'}} />
</View>

<Text style={[styles.text, styles.header]}>
    flex的元素上放一个View，不设置宽度
</Text>
<View style={{flexDirection: 'row'}}>
    <View style={{flex: 3}}>
        <View style={{height: 20, backgroundColor: '#333333'}} />
    </View>
    <View style={{flex: 1}}/>
</View>
```

#### 获取设备屏幕信息

```js
//获取pixel，通过设备密度获取，可以该size获取图片适合的尺寸
//dp to px
PixelRatio.getPixelSizeForLayoutSize(200)

//获取屏幕dp
import Dimensions
<Text style={styles.welcome}>
 屏幕信息如下:
</Text>
<Text style={styles.instructions}>
  当前屏幕宽度:+{Dimensions.get('window').width};
</Text>
<Text style={styles.instructions}>
  当前屏幕高度:'+{Dimensions.get('window').height};
</Text>
```

```js
//返回设备pixel
//Returns the device pixel density. Some examples:
PixelRatio.get() === 1
//mdpi Android devices (160 dpi)
PixelRatio.get() === 1.5
//hdpi Android devices (240 dpi)
PixelRatio.get() === 2
//iPhone 4, 4S
//iPhone 5, 5c, 5s
//iPhone 6
//xhdpi Android devices (320 dpi)
PixelRatio.get() === 3
//iPhone 6 plus
//xxhdpi Android devices (480 dpi)
PixelRatio.get() === 3.5
//Nexus 6
```

#### 返回字体大小

```
//如果没有设置字体大小
//按照顺序
//Android Settings > Display > Font size
//iOS返回默认大小
getFontScale(0)
```

#### 布局

使用flexDirection、alignItems和 justifyContent三个样式属性就已经能满足大多数布局需求

在组件的style中指定flexDirection可以决定布局的主轴。子元素是应该沿着水平轴\(row\)方向排列，还是沿着竖直轴\(column\)方向

```js
//Flex Direction
//线性布局1
//Flex Direction
//在组件的style中指定flexDirection可以决定布局的主轴。子元素是应该沿着水平轴(row)方向排列，
//还是沿着竖直轴(column)方向排列呢？默认值是竖直轴(column)方向。
//水平
<View>
    <View style={{flex: 1, flexDirection: 'row'}}>
        <View style={{flex: 1, height: 50, backgroundColor: 'powderblue'}} />
        <View style={{flex: 2, height: 50, backgroundColor: 'skyblue'}} />
        <View style={{flex: 1, height: 50, backgroundColor: 'steelblue'}} />
    </View>
</View>
//垂直
<View style={{flex: 1, flexDirection: 'column'}}>
    <View style={{width: 100, height: 50, backgroundColor: 'powderblue'}} />
    <View style={{width: 100, height: 50, backgroundColor: 'skyblue'}} />
    <View style={{width: 100, height: 50, backgroundColor: 'steelblue'}} />
</View>

//Justify Content
//在组件的style中指定justifyContent可以决定其子元素沿着主轴的排列方式。
//子元素是应该靠近主轴的起始端还是末尾段分布呢？亦或应该均匀分布？
//对应的这些可选项有：flex-start、center、flex-end、space-around以及space-between。
//垂直上中下平分布局->justifyContent center（居中）
<View style={{
    flex: 1,
    flexDirection: 'column',
    justifyContent: 'space-between',
}}>
    <View style={{width: 50, height: 50, backgroundColor: 'powderblue'}} />
    <View style={{width: 50, height: 50, backgroundColor: 'skyblue'}} />
    <View style={{width: 50, height: 50, backgroundColor: 'steelblue'}} />
</View>
//水平左中右平方布局
<View style={{
    flex: 1,
    flexDirection: 'row',
    justifyContent: 'space-between',
}}>
    <View style={{width: 50, height: 50, backgroundColor: 'powderblue'}} />
    <View style={{width: 50, height: 50, backgroundColor: 'skyblue'}} />
    <View style={{width: 50, height: 50, backgroundColor: 'steelblue'}} />
</View>

//Align Items
//在组件的style中指定alignItems可以决定其子元素沿着次轴（
//与主轴垂直的轴，比如若主轴方向为row，则次轴方向为column）的排列方式。
//子元素是应该靠近次轴的起始端还是末尾段分布呢？亦或应该均匀分布？
//对应的这些可选项有：flex-start、center、flex-end以及stretch。
// 尝试把`alignItems`改为`flex-start`看看
// 尝试把`justifyContent`改为`flex-end`看看
// 尝试把`flexDirection`改为`row`看看
<View style={{
flex: 1,
flexDirection: 'column',
justifyContent: 'center',
alignItems: 'center',
}}>
    <View style={{width: 50, height: 50, backgroundColor: 'powderblue'}} />
    <View style={{width: 50, height: 50, backgroundColor: 'skyblue'}} />
    <View style={{width: 50, height: 50, backgroundColor: 'steelblue'}} />
</View>
```



