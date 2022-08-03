# git issue

## git pull报“unable to update local ref”解决方式

git remote prune origin

> https://blog.csdn.net/ZYC88888/article/details/88299492

## pull 错误之后回滚

git reflog 

> https://blog.csdn.net/ZhouLoverBrother/article/details/115186580?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1-115186580-blog-84634832.pc_relevant_default&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1-115186580-blog-84634832.pc_relevant_default&utm_relevant_index=2

## hint: Updates were rejected because the tag already exists in the remote.

这个问题的原因是 tag 有问题，注意是tag

方法一：

推送的时候不要勾选“推送所有标签”

方法二：

* 1、执行命令 git pull --tags（获取所有的标签），这个地方可能会报错
，问题就在这里了，would clobber existing tag 的意思是 会破坏现有的标签
* 2、执行命令 git pull --tags -f ，这个命令可以覆盖本地存在的标签冲突

> 原文链接：https://blog.csdn.net/qq_43296719/article/details/106431479
