---
layout: post
title: Docker搭建php開發環境
date: 2018-10-19 17:24:59
categories: docker
---

### 运行 php 容器，设置当前工作目录/www/挂载
```
docker run --name php7.2 -v  $PWD/www/:/var/www/html/ --privileged=true -d php:7.2-fpm
```

### 运行 mysql
```
docker run -p 3306:3306 --name mysql -v $PWD/mysql/conf:/etc/mysql/conf.d -v $PWD/mysql/logs:/logs -v $PWD/mysql/data:/mysql_data -e MYSQL_ROOT_PASSWORD=123456 --link php7.2 -d mysql
```

### 运行 mysql 容器
```
mkdir -p $PWD/nginx/conf.d
touch $PWD/nginx/conf.d/default.conf
```

#### default.conf 配置
```
server {
listen       80;
server_name  localhost;

access_log  /var/log/nginx/access.log  main;

location / {
    root   /www; #容器目录
    index  index.html index.htm index index.php;
}
autoindex on;
autoindex_exact_size off;
autoindex_localtime on;
#error_page  404              /404.html;

# redirect server error pages to the static page /50x.html
#
error_page   500 502 503 504  /50x.html;
location = /50x.html {
    root   /var/www/html;
}

# pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
#
location ~ \.php$ {
    #root           html;
    fastcgi_pass   172.17.0.2:9000; #php-fpm容器的ip，端口9000
    fastcgi_index  index.php;
    fastcgi_param  SCRIPT_FILENAME  /var/www/html/$fastcgi_script_name; #php-fpm 对应的
    include        fastcgi_params;
}

# deny access to .htaccess files, if Apache's document root
# concurs with nginx's one
#
#location ~ /\.ht {
#    deny  all;
#}
}
```

### 运行 nginx ，链接 mysql ，设置conf.d挂载）
```
docker run --name lnmp --link mysql:db --link php7.2:php -p 8888:80 -v $PWD/www:/var/www/html -v $PWD/nginx/conf.d:/etc/nginx/conf.d --privileged=true -d nginx
```
### 进入 php 安装 mysqli ， 一定要这个 apt 会失败。。。
```
docker exec -it php7.2 bash

docker-php-ext-install mysqli 
```

### 退出重启 php
```
docker restart php7.2
```

### 登录mysql
```
docker exec -it mysql bash

mysql -u root -p
ALTER USER 'root'@'localhost' IDENTIFIED BY '123456';
```

### 添加远程登录用户
```
CREATE USER 'test'@'%' IDENTIFIED WITH mysql_native_password BY '123456';
GRANT ALL PRIVILEGES ON *.* TO 'test'@'%';
```

### 链接 mysql， 172.17.0.3 是 mysql 容器得 ip
```
docker inspect --format='{{.NetworkSettings.IPAddress}}' mysql
```
```
<?php
$conn = mysqli_connect("172.17.0.3", "test", "123456", "mysql");

if (!$conn) {
    echo "Error: Unable to connect to MySQL." . PHP_EOL;
    echo "Debugging errno: " . mysqli_connect_errno() . PHP_EOL;
    echo "Debugging error: " . mysqli_connect_error() . PHP_EOL;
    exit;
}

echo "Success: A proper connection to MySQL was made!" . PHP_EOL;
echo "Host information: " . mysqli_get_host_info($conn) . PHP_EOL;

//准备sql语句
$sql = "select * from user";

//发送sql语句
$result = mysqli_query($conn,$sql);
echo('</br>');
var_dump($sql);
echo('</br>');
while ($row = mysqli_fetch_assoc($result))
{
    var_dump($row['User']);
    echo('</br>');
}

mysqli_close($conn);
?>
```