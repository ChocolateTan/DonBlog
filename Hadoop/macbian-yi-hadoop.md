---
title: Mac安装protobuf
date: 2018-10-02 09:09:09
categories: Hadoop
---
### Mac安装protobuf

编译 Hadoop需要使用protobuf2.5.0

> 参考：[http://www.jianshu.com/p/8e88c3ef47b3](http://www.jianshu.com/p/8e88c3ef47b3)

```
tar -zxf  protobuf-2.6.1.tar.gz
./configure --prefix=/Users/don/tool/protobuf  这个目录记得更改为自己的//
make clean//不使用这个有可能会出现找不到protobuf/lib/libprotobuf.9.dylib
make
make install
vi ~/.bash_profile

//输入内容
export PROTOBUF=/Users/don/tool/protobuf
export PATH=$PROTOBUF/bin:$PATH

source ~/.bash_profile
protoc --version
```

```
mvn package -e -X -Pdist,native -DskipTests -Dtar
```

编译错误

```
[ERROR] Failed to execute goal org.apache.maven.plugins:maven-antrun-plugin:1.7:run (make) on project hadoop-pipes: An Ant BuildException has occured: exec returned: 1
[ERROR] around Ant part ...<exec failonerror="true" dir="/Users/don/Downloads/hadoop-2.7.3-src/hadoop-tools/hadoop-pipes/target/native" executable="cmake">... @ 5:131 in /Users/don/Downloads/hadoop-2.7.3-src/hadoop-tools/hadoop-pipes/target/antrun/build-main.xml
[ERROR] -> [Help 1]
org.apache.maven.lifecycle.LifecycleExecutionException: Failed to execute goal org.apache.maven.plugins:maven-antrun-plugin:1.7:run (make) on project hadoop-pipes: An Ant BuildException has occured: exec returned: 1
around Ant part ...<exec failonerror="true" dir="/Users/don/Downloads/hadoop-2.7.3-src/hadoop-tools/hadoop-pipes/target/native" executable="cmake">... @ 5:131 in /Users/don/Downloads/hadoop-2.7.3-src/hadoop-tools/hadoop-pipes/target/antrun/build-main.xml
    at org.apache.maven.lifecycle.internal.MojoExecutor.execute(MojoExecutor.java:212)
    at org.apache.maven.lifecycle.internal.MojoExecutor.execute(MojoExecutor.java:153)
    at org.apache.maven.lifecycle.internal.MojoExecutor.execute(MojoExecutor.java:145)
    at org.apache.maven.lifecycle.internal.LifecycleModuleBuilder.buildProject(LifecycleModuleBuilder.java:116)
    at org.apache.maven.lifecycle.internal.LifecycleModuleBuilder.buildProject(LifecycleModuleBuilder.java:80)
    at org.apache.maven.lifecycle.internal.builder.singlethreaded.SingleThreadedBuilder.build(SingleThreadedBuilder.java:51)
    at org.apache.maven.lifecycle.internal.LifecycleStarter.execute(LifecycleStarter.java:128)
    at org.apache.maven.DefaultMaven.doExecute(DefaultMaven.java:307)
    at org.apache.maven.DefaultMaven.doExecute(DefaultMaven.java:193)
    at org.apache.maven.DefaultMaven.execute(DefaultMaven.java:106)
    at org.apache.maven.cli.MavenCli.execute(MavenCli.java:863)
    at org.apache.maven.cli.MavenCli.doMain(MavenCli.java:288)
    at org.apache.maven.cli.MavenCli.main(MavenCli.java:199)
    at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
    at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
    at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
    at java.lang.reflect.Method.invoke(Method.java:498)
    at org.codehaus.plexus.classworlds.launcher.Launcher.launchEnhanced(Launcher.java:289)
    at org.codehaus.plexus.classworlds.launcher.Launcher.launch(Launcher.java:229)
    at org.codehaus.plexus.classworlds.launcher.Launcher.mainWithExitCode(Launcher.java:415)
    at org.codehaus.plexus.classworlds.launcher.Launcher.main(Launcher.java:356)
Caused by: org.apache.maven.plugin.MojoExecutionException: An Ant BuildException has occured: exec returned: 1
around Ant part ...<exec failonerror="true" dir="/Users/don/Downloads/hadoop-2.7.3-src/hadoop-tools/hadoop-pipes/target/native" executable="cmake">... @ 5:131 in /Users/don/Downloads/hadoop-2.7.3-src/hadoop-tools/hadoop-pipes/target/antrun/build-main.xml
    at org.apache.maven.plugin.antrun.AntRunMojo.execute(AntRunMojo.java:355)
    at org.apache.maven.plugin.DefaultBuildPluginManager.executeMojo(DefaultBuildPluginManager.java:134)
    at org.apache.maven.lifecycle.internal.MojoExecutor.execute(MojoExecutor.java:207)
    ... 20 more
Caused by: /Users/don/Downloads/hadoop-2.7.3-src/hadoop-tools/hadoop-pipes/target/antrun/build-main.xml:5: exec returned: 1
    at org.apache.tools.ant.taskdefs.ExecTask.runExecute(ExecTask.java:646)
    at org.apache.tools.ant.taskdefs.ExecTask.runExec(ExecTask.java:672)
    at org.apache.tools.ant.taskdefs.ExecTask.execute(ExecTask.java:498)
    at org.apache.tools.ant.UnknownElement.execute(UnknownElement.java:291)
    at sun.reflect.GeneratedMethodAccessor22.invoke(Unknown Source)
    at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
    at java.lang.reflect.Method.invoke(Method.java:498)
    at org.apache.tools.ant.dispatch.DispatchUtils.execute(DispatchUtils.java:106)
    at org.apache.tools.ant.Task.perform(Task.java:348)
    at org.apache.tools.ant.Target.execute(Target.java:390)
    at org.apache.tools.ant.Target.performTasks(Target.java:411)
    at org.apache.tools.ant.Project.executeSortedTargets(Project.java:1399)
    at org.apache.tools.ant.Project.executeTarget(Project.java:1368)
    at org.apache.maven.plugin.antrun.AntRunMojo.execute(AntRunMojo.java:327)
    ... 22 more
[ERROR] 
[ERROR] 
[ERROR] For more information about the errors and possible solutions, please read the following articles:
[ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/MojoExecutionException
[ERROR] 
[ERROR] After correcting the problems, you can resume the build with the command
[ERROR]   mvn <goals> -rf :hadoop-pipes
```

检查提示中对应的buil-main.xml文件，找到该exec语句，在控制台中尝试执行

```
cmake /Users/lishengda/Downloads/hadoop-2.7.0-src/hadoop-tools/hadoop-pipes/src/ -DJVM_ARCH_DATA_MODEL=64
```

```
-- The C compiler identification is AppleClang 8.1.0.8020038
-- The CXX compiler identification is AppleClang 8.1.0.8020038
-- Check for working C compiler: /Library/Developer/CommandLineTools/usr/bin/cc
-- Check for working C compiler: /Library/Developer/CommandLineTools/usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /Library/Developer/CommandLineTools/usr/bin/c++
-- Check for working CXX compiler: /Library/Developer/CommandLineTools/usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
CMake Error at /usr/local/Cellar/cmake/3.7.2/share/cmake/Modules/FindPackageHandleStandardArgs.cmake:138 (message):
  Could NOT find OpenSSL, try to set the path to OpenSSL root folder in the
  system variable OPENSSL_ROOT_DIR (missing: OPENSSL_INCLUDE_DIR)
Call Stack (most recent call first):
  /usr/local/Cellar/cmake/3.7.2/share/cmake/Modules/FindPackageHandleStandardArgs.cmake:378 (_FPHSA_FAILURE_MESSAGE)
  /usr/local/Cellar/cmake/3.7.2/share/cmake/Modules/FindOpenSSL.cmake:385 (find_package_handle_standard_args)
  CMakeLists.txt:20 (find_package)


-- Configuring incomplete, errors occurred!
```

提示显示没找到openssl,需要添加环境变量，于是添加

命令行执行：vim ~/.bash\_profile

在打开的文件中添加如下两行（具体vim怎么用请另行查询）

export OPENSSL\_ROOT\_DIR=/usr/local/Cellar/openssl/1.0.2j

export OPENSSL\_INCLUDE\_DIR=/usr/local/Cellar/openssl/1.0.2j/include

退出后执行source ~/.bash\_profile使之生效



////////3.1.1 mac
//进程显示不全
cat /private/etc/hosts
sudo vi /private/etc/hosts
127.0.0.1  dontan

