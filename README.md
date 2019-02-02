# WA=Wechat Assistant
>"微信是一种生活方式"——by 产品经理之神

所以有个产品经理认为：你需要一个生活助理，一个bot和/或AI，协助你处理发生在微信上各种事。

## 安装
截至20190202用的是开源的[itchat](https://github.com/littlecodersh/ItChat)和纯python3.x

## 使用
1. 执行 waMain.py
2. 扫码
3. 手机确认(登录微信网页版)
4. ...

## 第一个尝试：春节祝福自动回复
“群发拜年消息”这种尴尬又不失礼貌的事情，还是交给老一辈吧。

那么我们如何尴尬又不失礼貌的回复呢？
* sfCheck方法用正则判断消息是否包含关键字
* 如果是，就用sfContent方法随机回复一条祝福
* 以及time.sleep是人工智能核心代码！

效果大概如下：

<img src="https://github.com/xxfantasy/wechat/blob/master/img/sfexample.PNG" width=50%>

## TBC
