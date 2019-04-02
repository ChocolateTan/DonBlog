---
title: ReactNative Cancel Fourse
date: 2018-10-02 09:09:09
categories: ReactNative
---
http://react-china.org/t/touchablehighlight/3320

页面内有一个输入框和一个TouchableHighlight的按钮，当在输入框输入，直接点击该按钮时，第一次点击按钮总是执行取消TextInput的焦点回收键盘，第二次点击时按钮才会响应

```
keyboardShouldPersistTaps={true}
keyboardShouldPersistTaps enum('always', 'never', 'handled', false, true) #
```



