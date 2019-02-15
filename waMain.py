# coding=utf8
# WA(wechatassistant)
import itchat,time,re
from itchat.content import *
from waSFtext import sfCheck,sfContent

# 获取作为控制器的小号的UserName作为controlaccount
ConAcc='filehelper'

# def waNew():
#     t = time.asctime(time.localtime(time.time()))
#     global ConAcc
#     # 这里提前把小号的备注名改为WACC(WechatAssistantControlCenter)
#     ConAcc=itchat.search_friends(name='WACC')[0]['UserName']
#     itchat.send(t+'\nWechatAssistant 启用中', ConAcc)
#     waMenu()

# def waMenu():
#     menuDic ={
#         "func1": {"name": "春节短信","status": 0},
#         "func2": {"name": "会议模式","status": -1}
#     }
#     menuStr='----功能情况----\n'
#     for k,v in menuDic.items():
#         if v['status'] == -1:
#             menuStr=menuStr+v['name']+'：规划中\n'
#         elif v['status'] == 0:
#             menuStr=menuStr+v['name']+'：已关闭\n'
#         elif v['status'] == 1:
#             menuStr=menuStr+v['name']+'：已打开\n'
#     itchat.send(menuStr,ConAcc)

@itchat.msg_register(TEXT,isFriendChat=True, isGroupChat=True)
def controler(msg):
    if msg.toUserName == ConAcc or msg.fromUserName == ConAcc:
        if msg.text=='退出':
            print('退出')
            itchat.send('WechatAssistant 已退出',ConAcc)
            itchat.logout()
        elif msg.text=='状态':
            waMenu()
    elif msg.fromUserName != itchat.search_friends()['UserName']:
        # 功能权限开关，控制器设置开关，这里先默认春节短信回复始终打开，后面写controler的时候再改
        if True:
            # 判断是否群聊消息，感觉随时就要抽象出来单独做函数
            if re.match('@@',msg.fromUserName):
                if msg.isAt:
                    if sfCheck(msg.text,msg.fromUserName):
                        for content in sfContent(msg.fromUserName):
                           time.sleep(2) 
                           msg.user.send(content)
            else:
                if sfCheck(msg.text,msg.fromUserName):
                    for content in sfContent(msg.fromUserName):
                        time.sleep(2) 
                        msg.user.send(content)

    # elif sfCheck(msg.text):
    #     time.sleep(1)
    #     msg.user.send('谢谢你的祝福')
    #     time.sleep(3)
    #     msg.user.send(sfContent())
    # else:
    #     print(msg.content)


# 登录配置
# itchat.auto_login(enableCmdQR=2,loginCallback=waNew)
itchat.auto_login(enableCmdQR=2)
itchat.run()
