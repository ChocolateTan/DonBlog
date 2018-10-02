---
title: ReactNative ImageView
date: 2018-10-02 09:09:09
categories: ReactNative
---
创建一个ViewManager的子类。

实现createViewInstance方法。

导出视图的属性设置器：使用@ReactProp（或@ReactPropGroup）注解。

把这个视图管理类注册到应用程序包的createViewManagers里。

实现JavaScript模块。

```java
public class ReactImageManager extends SimpleViewManager<ReactImageView> {

  public static final String REACT_CLASS = "RCTImageView";

  @Override
  public String getName() {
    return REACT_CLASS;
  }
  @Override
  public ReactImageView createViewInstance(ThemedReactContext context) {
    return new ReactImageView(context, Fresco.newDraweeControllerBuilder(), mCallerContext);
  }
```

导出给JavaScript使用的属性，需要申明带有`@ReactProp`（或`@ReactPropGroup`）注解的设置方法.

方法的第一个参数是要修改属性的视图实例，第二个参数是要设置的属性值

方法的返回值类型必须为`void`

声明为`public`

