---
title: Hadoop筆記
date: 2018-10-02 09:09:09
categories: Hadoop
---
### Mac Hadoop筆記

www.linuxidc.com\/Linux\/2016-10\/136188.htm

mac 启动sshd

sudo launchctl load -w \/System\/Library\/LaunchDaemons\/ssh.plist

查看启动

sudo launchctl list \| grep ssh

输出- 0 com.openssh.sshd 表示启动成功

停止sshd服务

sudo launchctl unload -w \/System\/Library\/LaunchDaemons\/ssh.plist

命令查找java home

\/usr\/libexec\/java\_home

1. sudo .\/configure
2. sudo make
3. sudo make check
4. sudo make install
5. protoc --version

### mvn

打包：mvn package

编译：mvn compile

编译测试程序：mvn test-compile

清空：mvn clean

运行测试：mvn test

生成站点目录: mvn site

生成站点目录并发布：mvn site-deploy

安装当前工程的输出文件到本地仓库: mvn install

mvn compile：编译源代码,生成对应的CLASS文件，执行流程可见流程如图3

mvn test-compile：编译**[测试](http://lib.csdn.net/base/softwaretest "软件测试知识库")**代码,生成对应的CLASS文件，执行流程可见流程如图3

mvn test：运行测试,生成对应的CLASS文件，执行流程可见流程如图3

mvn package：打包,生成JAR文件，只能本程序用，或者拷贝到其它项目使用，执行流程可见流程如图3

mvn install ：打包,生成JAR文件，并在本地仓库生成JAR和POM文件，供其它Maven项目共享,，执行流程可见流程如图3；

mvn clean ：清除产生的项目

* $ mvn -version
* $ mvn clean
* $ mvn install -DskipTests
* $ mvn compile -DskipTests
* $ mvn package -DskipTests
* $ mvn package -Pdist -DskipTests -Dtar

mvn package -Pdist,native,docs,src -DskipTests -Dtar

### Mac系统的环境变量，加载顺序为：

\/etc\/profile \/etc\/paths ~\/.bash\_profile ~\/.bash\_login ~\/.profile ~\/.bashrc

### Mac命令

rm -r -f 文件夹名

### Hadoop localhost

http:\/\/localhost:9870\/

http:\/\/localhost:8088\/cluster

