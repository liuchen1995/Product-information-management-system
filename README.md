# Product-information-management-system
## 1.介绍
基于python的tkinter库和MySQL数据库开发的产品信息管理系统。

## 2.使用方法
点开exe文件，执行程序，用以下账号登录，必须主服务器开启，同时主服务器必须关闭防火墙才能连接。

主服务器IP地址：49.123.118.44

账户：liuchen

密码：******

## 3.截图


## 4.账号申请方法
主服务器数据库开通账号方法：

mysql> CREATE USER 'monty'@'localhost' IDENTIFIED BY 'some_pass';

mysql> GRANT ALL PRIVILEGES ON *.* TO 'monty'@'localhost' WITH GRANT OPTION;

mysql> CREATE USER 'monty'@'%' IDENTIFIED BY 'some_pass';

mysql> GRANT ALL PRIVILEGES ON *.* TO 'monty'@'%' WITH GRANT OPTION;
