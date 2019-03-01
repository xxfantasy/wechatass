# coding=utf8
userDic={}

def waBZstatus_On():
    global userList
    userList.clear()

def waBZstatus_Off():
    global userList
    userList.clear()

def bzCheck(msg):
    bzContent=[]
    global userDic
    if msg['FromUserName'] in userDic.keys():
        timeDiff = msg['CreateTime'] - userDic[msg['FromUserName']]['time']
        userDic[msg['FromUserName']]['time'] = msg['CreateTime']
        userDic[msg['FromUserName']]['count'] = userDic[msg['FromUserName']]['count']+1
        if  timeDiff > 1800:
            bzContent.append('不好意思我现在正忙，稍后回复')
            if userDic[msg['FromUserName']]['count'] > 30:
                bzContent.append('有急事可以打我134开头的手机')
                userDic[msg['FromUserName']]['count'] = 1
            else:
                pass
        else:
            pass
    else:
        userDic[msg['FromUserName']]={
                'time':msg['CreateTime'],
                'count':1
            }
        bzContent.append('不好意思我现在正忙，稍后回复')
    return bzContent
    