# coding=utf8
# WA(wechatassistant)
import itchat,time,re
from itchat.content import *
from waSFtext import sfCheck,sfContent

# WA功能配置，后面改sql  
fncList =[
        {"id":1,"cname":"春节短信","ename":"waSFtext","status":1},
        {"id":2,"cname":"会议模式","ename":"waCFmode","status":-1},
    ]

ConAcc,SelfAcc='',''

def waNew():
    t = time.asctime(time.localtime(time.time()))
    global ConAcc,SelfAcc
    SelfAcc= itchat.search_friends()['UserName']
    if len(itchat.search_friends(name='WACC'))!= 0:
        # 这里提前把小号的备注名改为WACC(WechatAssistantControlCenter)
        ConAcc=itchat.search_friends(name='WACC')[0]['UserName']
    else:
        ConAcc = 'filehelper' 
    itchat.send(t+'\n#WechatAssistant 已启用#', ConAcc)
    waMenu()

def waMenu():
    menuStr='----功能配置情况----\n'
    for item in fncList:
        if item['status'] == -1:
            menuStr=menuStr+"功能"+str(item['id'])+" "+item['cname']+'：规划中\n'
        elif item['status'] == 0:
            menuStr=menuStr+"功能"+str(item['id'])+" "+item['cname']+'：已关闭\n'
        elif item['status'] == 1:
            menuStr=menuStr+"功能"+str(item['id'])+" "+item['cname']+'：已启用\n'
    itchat.send(menuStr,ConAcc)

@itchat.msg_register(TEXT,isFriendChat=True, isGroupChat=True)
def controler(msg):
    # 控制器的消息：wacc发给我或者我发给wacc
    if msg.fromUserName == ConAcc or msg.toUserName == ConAcc:
        if msg.text=='退出':
            itchat.send('WechatAssistant 已退出',ConAcc)
            itchat.logout()
        elif msg.text=='菜单':
            waMenu()
    # 要处理的消息：发给我的，但不是我发的消息
    elif msg.toUserName == SelfAcc and msg.fromUserName != SelfAcc:
        # 功能权限开关
        if fncList[0]["status"]==1:
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

# 登录配置
itchat.auto_login(enableCmdQR=2,loginCallback=waNew)
itchat.run()
