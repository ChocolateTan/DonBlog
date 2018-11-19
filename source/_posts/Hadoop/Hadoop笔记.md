---
title: Hadoop筆記
date: 2018-10-02 09:09:09
categories: Hadoop
---
hdfs dfs -copyFromLocal ./input/ /user/dontan/
hdfs dfs -cat /user/dontan/out/part-r-00000
hadoop jar /usr/local/Cellar/hadoop/3.1.1/libexec/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.1.1.jar wordcount input out