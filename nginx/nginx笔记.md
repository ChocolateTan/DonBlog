---
title: nginx 笔记
date: 2020-01-30
categories: nginx
---
# nginx 笔记

---

## nginx 命令

* brew install nginx
* brew services start nginx
* nginx  #启动nginx
* nginx -s quit  #快速停止nginx
* nginx -V #查看版本，以及配置文件地址
* nginx -v #查看版本
* nginx -s reload|reopen|stop|quit   #重新加载配置|重启|快速停止|安全关闭nginx
* nginx -h #帮助

## nginx文件目录

* nginx安装文件目录/usr/local/Cellar/nginx
* nginx配置文件目录/usr/local/etc/nginx
* config文件目录 /usr/local/etc/nginx/nginx.conf
* 系统hosts位置 /private/etc/hosts