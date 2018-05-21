# 项目名称
proxy_scrapy
<p>
 代理自动获取，利用scrapy多线程获取，存入mongoDB，并通过flask输出

# 项目目标
自动获取代理xicidaili.com，存入数据库，调用requests进行检测，有效则存入有效代理表，通过flask可以获取，有效代理表保持20个有效代理
<p>


# 使用方法
 由主程序入口调用程序，使用flask接口获取


# 主要请求方法

 scrapy框架
 
 requests抓取网页信息
 

# 其他方法

 MongoDB,pymongo
 

# 作者信息
- cccccxw
- 2018-05-21 16:47:50

# 环境配置
## Ubuntu
### Python3的安装
```sh
# Python3 安装
sudo apt-get install python3
sudo apt-get intsall python3-pip
sudo apt-get intsall mongodb

```

### 所需库
```sh

pip3 install requests
pip3 install pymongo
pip3 install flask
pip3 install lxml

```
### 思路参考了大佬的代码
https://github.com/WiseDoge/ProxyPool
https://github.com/Germey/ProxyPool



