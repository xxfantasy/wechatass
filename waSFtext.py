import re,random
# 判断消息内容是否包含关键字
userDic={}

def sfCheck(text,user):
    sfkw='春节|新春|猪年|新年|除夕|2019'
    if re.search(sfkw,text) is None:
        return False
    else :
        global userList
        if user in userDic:
            userDic[user]= userDic[user]+1
        else:
            userDic[user]= 0    
        return True
    
# 春节短信消息内容
def sfContent(user):
    contentList=[]
    thxlist=[
        '谢谢啦',
        '非常感谢'
    ]
    sflist=[
        '猪年到喜迎门，送欢乐送祝福，愿您新春欢乐，万事如意，阖家欢乐，百事顺心，吉星高照，添福添寿，幸福美满，快乐一生！',
        '猪年新春到，心情无限妙；快乐把门敲，喜庆身边绕；吉祥跟你跑，幸福对你笑；健康来拥抱，愿你身体好；新的一年，愿你生活美满，幸福逍遥！',
        '朝霞映满天，盛世耀猪年。歌美舞翩翩，快乐太平年。瑞雪一片片，幸福绕猪年。春风暖心田，欢度团圆年。猪年到了，愿你快乐绵绵！'
    ]
    if user in userDic:
        if userDic[user] == 0:
            contentList.append(random.choice(thxlist))  
            contentList.append(random.choice(sflist))
        elif userDic[user] > 0 and userDic[user] < 10:
            contentList.append(random.choice(thxlist))
            contentList.append('已经收到过祝福啦')
        else:
            contentList.append('你是机器人吗？一直发发发')
    else:
        contentList.append(random.choice(thxlist))  
        contentList.append(random.choice(sflist))
    return contentList