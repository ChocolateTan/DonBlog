---
title: ReactNative Touch Event
date: 2018-10-02 09:09:09
categories: ReactNative
---
#### 参考：[http://www.jianshu.com/p/99cd45336849](http://www.jianshu.com/p/99cd45336849)

#### TouchableHighlight

制作按钮或者链接，此组件的背景会在用户手指按下时变暗

```js
class MyButton extends Component {
  _onPressButton() {
    console.log("You tapped the button!");
  }

  render() {
    return (
      <TouchableHighlight onPress={this._onPressButton}>
        <Text>Button</Text>
      </TouchableHighlight>
    );
  }
}
```

#### TouchableNativeFeedback（Android）

用户手指按下时形成类似墨水涟漪的视觉效果。在Android设备上，这个组件利用原生状态来渲染触摸的反馈。目前它只支持一个单独的View实例作为子节点。在底层实现上，实际会创建一个新的RCTView结点替换当前的子View，并附带一些额外的属性。而且原生触摸操作反馈的背景可以使用background属性来自定义。

TouchableNativeFeedback继承于TouchableWithoutFeedback，所以TouchableWithoutFeedback得属性

background 决定在触摸反馈的时候显示什么类型的背景。它接受一个有着type属性和一些基于type属性的额外数据的对象。我们推荐使用以下的静态方法之一来创建这个对象：

* TouchableNativeFeedback.SelectableBackground\(\) - 会创建一个对象，表示安卓主题默认的对于被选中对象的背景。\(?android:attr/selectableItemBackground\)
* TouchableNativeFeedback.SelectableBackgroundBorderless\(\) - 会创建一个对象，表示安卓主题默认的对于被选中的无边框对象的背景。\(?android:attr/selectableItemBackgroundBorderless\)。只在Android API level 21+适用。
* TouchableNativeFeedback.Ripple\(color, borderless\) - 会创建一个对象，当按钮被按下时产生一个涟漪状的背景，你可以通过color参数来指定颜色，如果参数borderless是true，那么涟漪还会渲染到视图的范围之外。（参见原生的actionbar buttons作为该效果的一个例子）。这个背景类型只在Android API level 21+适用。

#### TouchableOpacity

按下时降低按钮的透明度，而不会改变背景的颜色

```js
<TouchableOpacity onPress={this._onPressButton}>
  <Image
    style={styles.button}
    source={require('image!myButton')}
  />
</TouchableOpacity>
```

#### TouchableWithoutFeedback

只支持一个子节点如果你希望包含多个子组件，用一个View来包装它们

