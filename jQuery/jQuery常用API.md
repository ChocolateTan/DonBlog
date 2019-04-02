---
title: jQuery常用API
date: 2018-10-02 09:09:09
categories: jQuery
---
# jQuery常用API


---

##hide() 和 show() 方法来隐藏和显示 HTML 元素
语法：

``$(selector).show(speed,callback);``

实例
```javascript
$("button").click(function(){
  $("p").hide(1000);
});
```

通过 jQuery，您可以使用 toggle() 方法来切换 hide() 和 show() 方法。
显示被隐藏的元素，并隐藏已显示的元素：

语法：

``$(selector).toggle(speed,callback);``
实例
```javascript
$("button").click(function(){
  $("p").toggle();
});
```