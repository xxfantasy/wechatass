# coding=utf8
# WA(wechatassistant)
import itchat,time,re
from itchat.content import *
from waSFtext import *
from waBZstatus import *

# WA功能配置，后面改sql  
fncList =[
        {"id":1,"cname":"春节短信","ename":"waSFtext","status":-1},
        {"id":2,"cname":"忙碌模式","ename":"waBZstatus","status":-1},
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
            menuStr=menuStr+"功能"+str(item['id'])+" "+item['cname']+'：已关闭\n'
        elif item['status'] == 0:
            menuStr=menuStr+"功能"+str(item['id'])+" "+item['cname']+'：规划中\n'
        elif item['status'] == 1:
            menuStr=menuStr+"功能"+str(item['id'])+" "+item['cname']+'：运行中\n'
    itchat.send(menuStr,ConAcc)

def waFNCswitch(id):
    if fncList[id-1]["status"] != 0:
        fncList[id-1]["status"]=0-fncList[id-1]["status"]
        if fncList[id-1]["status"] == -1:
            eval(fncList[id-1]["ename"]+"_Off()")
            itchat.send(fncList[id-1]["cname"]+"功能已关闭",ConAcc)
        elif fncList[id-1]["status"] == 1:
            eval(fncList[id-1]["ename"]+"_On()")
            itchat.send(fncList[id-1]["cname"]+"功能运行中",ConAcc) 
    else:
        itchat.send(fncList[id-1]["cname"]+"功能还在规划中",ConAcc)



# def waHelp(user):

    

@itchat.msg_register(TEXT,isFriendChat=True, isGroupChat=True)
def controler(msg):
    # 控制器的消息：wacc发给我或者我发给wacc
    if msg.fromUserName == ConAcc or msg.toUserName == ConAcc:
        if msg.text=='退出':
            itchat.send('WechatAssistant 已退出',ConAcc)
            itchat.logout()
        elif msg.text=='菜单':
            waMenu()
        elif re.match(r'sw(\d)$', msg.text,re.I):
            waFNCswitch(int(re.match(r'sw(\d)$', msg.text,re.I).group(1)))
        # elif msg.text=='帮助':
        #     waHelp(ConAcc)
        # else:
        #     itchat.send('可以输入\'帮助\'查看指令',ConAcc)

    # 要处理的消息：发给我的，但不是我发的消息
    elif msg.toUserName == SelfAcc and msg.fromUserName != SelfAcc:
        # 判断功能开启
        if fncList[0]["status"]==1:
            # 判断是否群聊消息
            if re.match('@@',msg.fromUserName):
                if msg.isAt:
                    contentList =sfCheck(msg)
                    if contentList:
                        for content in contentList:
                            time.sleep(2) 
                            msg.user.send(content)
            else:
                contentList =sfCheck(msg)
                if contentList:
                    for content in contentList:
                        time.sleep(2) 
                        msg.user.send(content)
        if fncList[1]["status"]==1:
            if re.match('@@',msg.fromUserName):
                if msg.isAt:
                    contentList =bzCheck(msg)
                    if contentList:
                        for content in contentList:
                            time.sleep(2) 
                            msg.user.send(content)
            else:
                contentList =bzCheck(msg)
                if contentList:
                    for content in contentList:
                        time.sleep(2) 
                        msg.user.send(content)

# 登录配置
itchat.auto_login(enableCmdQR=2,loginCallback=waNew)
itchat.run()
