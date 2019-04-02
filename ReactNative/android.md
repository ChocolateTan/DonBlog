---
title: ReactNative 通訊 Android
date: 2018-10-02 09:09:09
categories: ReactNative
---
继承ReactContextBaseJavaModule，要求派生类实现`getName`方法

模块名前的RCT前缀会被自动移除。所以如果返回的字符串为"RCTToastAndroid"，在JavaScript端依然通过`React.NativeModules.ToastAndroid`访问到这个模块

```java
public class ToastModule extends ReactContextBaseJavaModule {

  private static final String DURATION_SHORT_KEY = "SHORT";
  private static final String DURATION_LONG_KEY = "LONG";

  public ToastModule(ReactApplicationContext reactContext) {
    super(reactContext);
  }
}
```

添加被JavaScript同步访问到的预定义的值

```java
@Override
  public Map<String, Object> getConstants() {
    final Map<String, Object> constants = new HashMap<>();
    constants.put(DURATION_SHORT_KEY, Toast.LENGTH_SHORT);
    constants.put(DURATION_LONG_KEY, Toast.LENGTH_LONG);
    return constants;
  }
```

要导出一个方法给JavaScript使用，Java方法需要使用注解`@ReactMethod`。方法的返回类型必须为`void`。React Native的跨语言访问是异步进行的，所以想要给JavaScript返回一个值的唯一办法是使用回调函数或者发送事件

```java
@ReactMethod
  public void show(String message, int duration) {
    Toast.makeText(getReactApplicationContext(), message, duration).show();
  }
```



