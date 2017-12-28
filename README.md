# urlSpider

### 概述

爬全站链接

### 环境

python 2.x/3.x

*依赖模块*

- pip install scrapy
- pip install openpyxl

### 使用

```shell
scrapy crawl bbjh -a url=www.bgzchina.com
```

结果保存为excel文档，xlsx文件存储在根目录，以 **域名_日期.xlsx** 格式命名。
