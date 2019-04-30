
https://blog.csdn.net/qq_38380025/article/details/80647620
https://blog.csdn.net/mmingxiang/article/details/81980392

容器操作系统用户 root：helowin
root/helowin
helowin

docker pull registry.cn-hangzhou.aliyuncs.com/helowin/oracle_11g

docker run -d -p 1521:1521 --name oracle11g registry.cn-hangzhou.aliyuncs.com/helowin/oracle_11g

docker exec -it oracle11g bash