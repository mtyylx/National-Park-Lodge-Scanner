# US National Park Lodge Scanner

```
A gift for those who want to stay INSIDE the national park.
```


## 起因

美国国家公园内的住宿实在是太难订了。在可订时间范围内（通常是未来一年内），基本上绝大多数日期所有旅馆的房间都是sold out状态。由于可以免费取消预定，很多游客都是提前很久就先预定能预定的时间，到时候不行再取消预定。所以像我们这种提前一个月计划行程订旅馆的人来说，只能靠不停的刷预定网站，寄希望于捡别人退订的漏才能订上。不过由于游客绝大多数还是来自美国的，15个小时的时差导致退订大概率发生在夜里，等到起床的时候早都被别人订走了。

综上所述，急需一个能代替我一天24小时检测大峡谷可订客房信息的工具。


## 解决方案


1. 自动获取信息：`Selenium`驱动`PhantomJS`或者`Chromedriver`来访问指定搜索结果的网页，每隔一分钟刷一次。

2. 网页内容分析：`BeautifulSoup`解析搜索结果，判断每个旅馆是否有room available。

3. `IFTTT`手机推送通知：将客房信息用Web Request发给`IFTTT`的Trigger，将通知推送至手机端，确保在发现新大陆时能及时预定。


## 使用方法


### 1. Dependency

- Selenium

- PhantomJS / Chromedriver

- BeautifulSoup

- IFTTT
    
### 2. Configure IFTTT Recipe


- THIS：选Maker Webhook，Event名称定义为hotel_update

- THAT：选Notification

- 记得把key修改成自己账号的key。

    
### 3. Run

- 运行run.py

- 根据提示格式输入要搜索的国家公园，入住日期，搜索方式用PhantomJS（后台工作）还是Chrome（可视工作）。

### 4. Get Notified!

- 脚本持续运行，每隔一分钟自动访问一次网站。

- 如果完全没有可选客房，会每隔1个小时推送至手机端。如果一旦发现可选客房，就会立即实时推送至手机端。


## 适用范围

Xanterra集团开发的国家公园住宿网站由于十分相似，因此基本上可以通用。测试成功以下4个国家公园：

- Grand Canyon South Rim

- Zion National Park

- Crater Lake National Park

- Glacier National Park
