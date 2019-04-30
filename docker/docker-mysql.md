# docker mysql

docker run -p 3306:3306 -dit --restart unless-stopped --name mysqldb -v /mysqldata:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=dontounchme -d mysql:5.6
docker inspect mysqlsock
docker exec -it mysql bash