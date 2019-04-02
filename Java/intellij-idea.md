---
title: intellij idea
date: 2018-10-02 09:09:09
categories: Java
---
archetypeCatalog表示插件使用的archetype元数据，不加这个参数时默认为remote，local，即中央仓库archetype元数据，由于中央仓库的archetype太多了，所以导致很慢，指定internal来表示仅使用内部元数据。

这里在Properties中添加一个参数

`archetypeCatalog=internal`

，不加这个参数，在maven生成骨架的时候将会非常慢，有时候会直接卡住

