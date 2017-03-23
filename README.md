# US National Park Lodge Scanner

```
A gift for those who want to STAY INSIDE the national park.
```


## 起因

美国国家公园内的住宿实在是太难订了。在可订时间范围内（通常是未来一年内），基本上绝大多数日期所有旅馆的房间都是sold out状态。由于可以免费取消预定，很多游客都是提前很久就先预定能预定的时间，到时候不行再取消预定。所以像我们这种提前一个月计划行程订旅馆的人来说，只能靠不停的刷预定网站，寄希望于捡别人退订的漏才能订上。不过由于游客绝大多数还是来自美国的，15个小时的时差，导致人家的退订很大概率发生在夜里4点到6点，等到国内起床的时候早都被别人订走了。

综上所述，急需一个能代替我一天24小时监测大峡谷可订客房信息的工具。


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

- 按规定格式输入要搜索的国家公园，入住日期，搜索方式用PhantomJS（后台工作）还是Chrome（可视工作）。

### 4. Get Notified!

- 脚本持续运行，根据输入的搜索设置每分钟自动搜索一次。

- 如果在指定日期的所有客房都订完（通常都是这种情况）则不推送消息。

- 如果刷出来可选的客房信息（通常是因为有人取消预定），就会立即按照设定的频率推送至手机端。


## 适用范围

Xanterra集团开发的国家公园住宿网站由于十分相似，因此基本上可以通用。测试成功以下4个国家公园：

- [`Grand Canyon South Rim`](http://www.grandcanyonlodges.com/)

- [`Zion National Park`](http://www.zionlodge.com)

- [`Crater Lake National Park`](http://www.craterlakelodges.com)

- [`Glacier National Park`](http://www.glaciernationalparklodges.com/)

## 更新

经过将近一个星期的运行，成功刷到 `Maswik` / `Bright Angel` / `Thunderbird` 这三个lodge总计四间客房，挑了其中离South Rim最近（大约30米）而且还有Canyon View的房间，把其他的三个都退掉了，大功告成。

另外感觉美国人民刷住宿也都不是盖的，我取消的三个房间在大约半小时内就被重新预定一空了。

![image](http://www.grandcanyongrandhotel.com/assets/gcsr_lookoutstudiowide_72-300x200.jpg)