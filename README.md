# Product-information-management-system
## 一.介绍
基于python的tkinter库和MySQL数据库开发的产品信息管理系统。

## 二.使用方法
点开exe文件，执行程序，用以下账号登录，必须主服务器开启，同时主服务器必须关闭防火墙才能连接。

主服务器IP地址：49.123.118.44

账户：liuchen

密码：******

## 三.截图

### 1.登录界面
![Aaron Swartz](https://raw.githubusercontent.com/liuchen1995/Product-information-management-system/master/截图/登录界面.jpg)

### 2.主界面
![Aaron Swartz](https://raw.githubusercontent.com/liuchen1995/Product-information-management-system/master/%E6%88%AA%E5%9B%BE/%E4%B8%BB%E7%95%8C%E9%9D%A2.jpg)

### 3.创建新产品界面
![Aaron Swartz](https://raw.githubusercontent.com/liuchen1995/Product-information-management-system/master/%E6%88%AA%E5%9B%BE/%E5%88%9B%E5%BB%BA%E6%96%B0%E4%BA%A7%E5%93%81.jpg)

### 4.产品录入界面
![Aaron Swartz](https://raw.githubusercontent.com/liuchen1995/Product-information-management-system/master/%E6%88%AA%E5%9B%BE/%E4%BA%A7%E5%93%81%E5%BD%95%E5%85%A5.jpg)

### 5.产品查询和删除界面
![Aaron Swartz](https://raw.githubusercontent.com/liuchen1995/Product-information-management-system/master/%E6%88%AA%E5%9B%BE/%E4%BA%A7%E5%93%81%E6%9F%A5%E8%AF%A2.jpg)

### 6.关于界面
![Aaron Swartz](https://raw.githubusercontent.com/liuchen1995/Product-information-management-system/master/%E6%88%AA%E5%9B%BE/%E5%85%B3%E4%BA%8E.jpg)

## 四.账号申请方法
主服务器数据库开通账号方法：

mysql> CREATE USER 'monty'@'localhost' IDENTIFIED BY 'some_pass';

mysql> GRANT ALL PRIVILEGES ON *.* TO 'monty'@'localhost' WITH GRANT OPTION;

mysql> CREATE USER 'monty'@'%' IDENTIFIED BY 'some_pass';

mysql> GRANT ALL PRIVILEGES ON *.* TO 'monty'@'%' WITH GRANT OPTION;
