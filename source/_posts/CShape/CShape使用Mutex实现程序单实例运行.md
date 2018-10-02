---
title: C#使用Mutex实现程序单实例运行
date: 2018-10-02 09:09:09
categories: CShape
---
# C#使用Mutex实现程序单实例运行

大家在开发程序的时候，有时需要限制程序，只能同时运行一个实例，实现此功能，对于VB.NET是非常容易的，只要指定一个属性即可，但是C#实现起来，就稍微繁琐了。
C#实现单实例运行的方法，也有多种，比如利用 Process 查找进程的方式，利用 API findwindow 查找窗体的方式，还有就是 利用 Mutex 原子操作，上面几种方法中， 综合考虑利用 Mutex 的方式是较好的选择。
下面给出使用 Mutex 实现单实例运行的例子：
C# 中，找到 program.cs ，这里面的 

```c#
[STAThread]
 
static
void Main()
 
{
 
    //……
 
}
```

是程序运行的入口点，默认情况下，里面的代码大致如下： 
```c#
[STAThread]
static void Main()
{
    Application.EnableVisualStyles();
    Application.SetCompatibleTextRenderingDefault(false);
    Application.Run(new Form1());
}
```
复制代码
加入单实例限制后的代码如下： 
```c#
[STAThread]
static void Main()
{
    bool isAppRunning = false;
    System.Threading.Mutex mutex = new System.Threading.Mutex(
        true,
        System.Diagnostics.Process.GetCurrentProcess().ProcessName,
        out isAppRunning);
    if (!isAppRunning)
    {
        MessageBox.Show("本程序已经在运行了，请不要重复运行！");
        Environment.Exit(1);
    }
    else
    {
        Application.EnableVisualStyles();
        Application.SetCompatibleTextRenderingDefault(false);
        Application.Run(new Form1());
    }
}
```
另一个利用Mutex实现互斥的类
```c#
using System; 
using System.Collections.Generic; 
using System.Linq; 
using System.Text; 
using System.Threading ; 
 
namespace 多线程 
{ 
    class Mutex互斥类 
    { 
        public static void Main() 
        { 
            //Mutex互斥类主要特点就是进程间共享，进程间互相排斥，抢锁,用名称做标识。 
            bool createdNew ; 
            Mutex mutex = new Mutex( false , "Aladdin" , out createdNew ) ; 
 
            if( mutex.WaitOne(1000,false ) ) 
            { 
                try 
                { 
                    Console.WriteLine( "正常启动。。。。。" ) ; 
                    Console.ReadLine() ; 
                } 
                finally 
                { 
                    mutex.ReleaseMutex() ; 
                } 
            } 
            else 
            { 
                Console.WriteLine( "你已经启动了一个了，不要再闹了" ) ; 
                Console.Read() ; 
            } 
 
            //注，如果单纯判断一个互斥线程是不是已经存在，可以直接用createdNew out参数来判断 
        } 
    } 
}
```
>来源：
>[1]: <http://hi.baidu.com/szhesh/item/c3c28b27ebf5423394f62b01>
 