---
title: Java反射
date: 2018-10-02 09:09:09
categories: Java
---
\/\*\*

\* 获取操作实体的类型

\*\/

Class&lt;? extends Object&gt; clazz = entity.getClass\(\);

\/\*\*

\* 获取传入实体的所有公开的方法;

\*\/

Method\[\] methods = clazz.getDeclaredMethods\(\);

\/\*\*

\* 获取传入实体中的所有公开的的属性

\*\/

Field\[\] fields = clazz.getDeclaredFields\(\);

fields\[i\].setAccessible\(true\);\/\/取消private

如果没有在获取Field之前调用setAccessible\(true\)方法，异常:

1. java.lang.IllegalAccessException:
2. Class com.test.accessible.Main
3. can not access
4. a member of **class** com.test.accessible.AccessibleTest
5. with modifiers "private"

