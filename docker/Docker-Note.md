---
title: Docker Note
date: 2018-10-22 12:13:06
categories: docker
---
### linux 一些命令
ps aux --sort -rss
du -sh * 看哪个目录占用空间大

### linux docker 命令
systemctl start docker
service docker stop

### 后台执行

nohup python work.py >my.log &

### run docker image
```
docker run -p 4000:80 friendlyhello
// run on background
docker run -d -p 4000:80 friendlyhello
```

```
//docker tag image username/repository:tag
docker tag friendlyhello john/get-started:part1
```

```
docker build -t friendlyname .# 使用此目录的 Dockerfile 创建镜像
docker run -p 4000:80 friendlyname  # 运行端口 4000 到 90 的“友好名称”映射
docker run -d -p 4000:80 friendlyname         # 内容相同，但在分离模式下
docker ps                                 # 查看所有正在运行的容器的列表
docker stop <hash>                     # 平稳地停止指定的容器
docker ps -a           # 查看所有容器的列表，甚至包含未运行的容器
docker kill <hash>                   # 强制关闭指定的容器
docker rm <hash>              # 从此机器中删除指定的容器
docker rm $(docker ps -a -q)           # 从此机器中删除所有容器
docker images -a                               # 显示此机器上的所有镜像
docker rmi <imagename>            # 从此机器中删除指定的镜像
docker rmi $(docker images -q)             # 从此机器中删除所有镜像
docker login             # 使用您的 Docker 凭证登录此 CLI 会话
docker tag <image> username/repository:tag  # 标记 <image> 以上传到镜像库
docker push username/repository:tag            # 将已标记的镜像上传到镜像库
docker run username/repository:tag                   # 运行镜像库中的镜像

# 推送文件到容器，拉文件
docker cp foo.txt mycontainer:/foo.txt
docker cp mycontainer:/foo.txt foo.txt

$ sudo docker login --username=390032295@qq.com registry.cn-shenzhen.aliyuncs.com
$ sudo docker login --username=390032295@qq.com registry.cn-shenzhen.aliyuncs.com
$ sudo docker tag [ImageId] registry.cn-shenzhen.aliyuncs.com/don-server/docker-mysql-collector:[镜像版本号]
$ sudo docker push registry.cn-shenzhen.aliyuncs.com/don-server/docker-mysql-collector:[镜像版本号]

```

### 使用 compose 部署
```
docker stack deploy -c docker-compose.yml getstartedlab
```

```
docker stack ls              # 列出此 Docker 主机上所有正在运行的应用
docker stack deploy -c <composefile> <appname>  # 运行指定的 Compose 文件
docker stack services <appname>       # 列出与应用关联的服务
docker stack ps <appname>   # 列出与应用关联的正在运行的容器
docker stack rm <appname>                             # 清除应用
```
docker update --restart=no my-container
docker update --restart=unless-stopped my-container

docker ps --format "{{.ID}}: {{.Command}}"

docker run --name mymongodb -p 27017:27017 -v $PWD/data/db:/data/db -d mongo --auth

docker run --name collectormongodb -p 27017:27017 -v /data/db:/data/db -v /mongodconfig/mongod.conf:/etc/mongod.conf -d mongo --auth

docker run --name collectormongodb -p 27017:27017 -v /mongodconfig/mongod.conf:/etc/mongod.conf -d mongo --auth

docker run --name mymongodb -p 27017:27017 -d mongo

sudo docker run -p 27017:27017 -v /tmp/db:/data/db -d mongo

sudo docker run -it mongo mongo --host <宿主机IP地址> --port 27017

docker run --name collectormongodb -p 27017:27017 -d mongo

Client:
 docker run -it mongo mongo --host 192.3.161.151 --port 27017

sudo docker pull docker.io/mongo-express
sudo docker run -it --rm -p 8081:8081 --link <mongoDB容器ID>:mongo mongo-express
sudo docker run -it --rm -p 8081:8081 --link collectormongodb:mongo mongo-express

sudo docker pull mongoclient/mongoclient
sudo docker run --name mongoclient -d -p 3000:3000 -e MONGO_URL=mongodb://<宿主机IP地址>:27017/ mongoclient/mongoclient
sudo docker run --name mongoclient -d -p 3000:3000 -e MONGO_URL=mongodb://192.3.161.151:27017/ mongoclient/mongoclient

sudo docker run -itd -p 8081:8081 --link collectormongodb:mongo mongo-express

sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates
sudo rm /var/cache/apt/archives/lock
sudo rm /var/lib/dpkg/lock
sudo apt-get install  docker
sudo   apt-get install   docker.io
sudo apt-get install  docker-registry
sudo systemctl  start  docker

