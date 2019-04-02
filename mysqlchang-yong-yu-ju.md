---
title: MySQL
date: 2018-10-02 09:09:09
categories: MySQL
---
1.創建時間和修改時間

    CREATE TABLE `tb_user` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `name` varchar(45) COLLATE utf8_bin DEFAULT NULL,
      `password` varchar(45) COLLATE utf8_bin DEFAULT NULL,
      `isDelete` int(11) DEFAULT NULL,
      `createDate` datetime DEFAULT CURRENT_TIMESTAMP,
      `modifyDate` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;




