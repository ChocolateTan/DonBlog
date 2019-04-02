---
title: jQuery Note
date: 2018-10-02 09:09:09
categories: jQuery
---
# Jquery Note


---

##jQuery 语法
jQuery 语法是为 HTML 元素的选取编制的，可以对元素执行某些操作。

基础语法是：$(selector).action()

美元符号定义 jQuery

选择符（selector）“查询”和“查找” HTML 元素

jQuery 的 action() 执行对元素的操作

示例

$(this).hide() - 隐藏当前元素

$("p").hide() - 隐藏所有段落

$(".test").hide() - 隐藏所有 class="test" 的所有元素

$("#test").hide() - 隐藏所有 id="test" 的元素



---

##文档就绪函数
您也许已经注意到在我们的实例中的所有 jQuery 函数位于一个 document ready 函数中：
```javascript
$(document).ready(function(){

--- jQuery functions go here ----

});
```
这是为了防止文档在完全加载（就绪）之前运行 jQuery 代码。


---


##jQuery 事件

下面是 jQuery 中事件方法的一些例子：

| Event 函数 | 绑定函数至 |
|--|--|
|$(document).ready(function)	|将函数绑定到文档的就绪事件（当文档完成加载时）|
|$(selector).click(function)	|触发或将函数绑定到被选元素的点击事件|
|$(selector).dblclick(function)	|触发或将函数绑定到被选元素的双击事件|
|$(selector).focus(function)	|触发或将函数绑定到被选元素的获得焦点事件|
|$(selector).mouseover(function)	|触发或将函数绑定到被选元素的鼠标悬停事件|