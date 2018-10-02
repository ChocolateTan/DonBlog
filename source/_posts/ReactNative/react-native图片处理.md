---
title: ReactNative Static Image Source
date: 2018-10-02 09:09:09
categories: ReactNative
---
#### 静态图片资源

```
<Image source={require('./my-icon.png')} />
```

> 为了使新的图片资源机制正常工作，require中的图片名字必须是一个静态字符串

```js
// 正确
<Image source={require('./my-icon.png')} />

// 错误
var icon = this.props.active ? 'my-icon-active' : 'my-icon-inactive';
<Image source={require('./' + icon + '.png')} />

// 正确
var icon = this.props.active ? require('./my-icon-active.png') : require('./my-icon-inactive.png');
<Image source={icon} />
```

#### 混合App的图片资源

编写一个混合App（一部分UI使用React Native，而另一部分使用平台原生代码），也可以使用已经打包到App中的图片资源（通过Xcode的asset类目或者Android的drawable文件夹打包）

```js
<Image source={{uri: 'app_icon'}} style={{width: 40, height: 40}} />
```

> 注意：这一做法并没有任何安全检查。你需要自己确保图片在应用中确实存在，而且还需要指定尺寸。

#### 网络图片

需要手动指定图片的尺寸

```js
// 正确
<Image source={{uri: 'https://facebook.github.io/react/img/logo_og.png'}}
       style={{width: 400, height: 400}} />

// 错误
<Image source={{uri: 'https://facebook.github.io/react/img/logo_og.png'}} />
```



