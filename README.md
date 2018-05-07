背景：此项目是保证爬虫项目时，提供可用足量的代理地址。

1.技术栈
  	Flask+grequest+redis+gevent

2.项目安装
  	pip install -r requirements.txt；
  
  	修改配置文件（conf）Redis相关配置；
  
  	运行后可访问页面 http://localhost:3456(默认)， 可修改启动脚本的端口地址
  
  
 3.项目结构
  
	  主要为抓取-->过滤-->调度-->定时检测 四个模块
	  运行流程为 调度器启动抓取和定时检测模块，根据设定代理数量判定是否进行抓取操作，将抓取的代理放入redis相应的队列右侧，并同时从左侧取出代理进行检测。
	  web部署为Flask+gevent。提供三个基本的URL地址,/ /get /count 分别返回主页面/一条代理/代理总量




  
