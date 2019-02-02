import re,random
# 判断消息内容是否包含关键字
def sfCheck(text):
    sfkw='春节|新春|猪年|新年|除夕|2019'
    if re.search(sfkw,text) is None:
        return 0
    else :
        return 1
    
# 春节短信消息内容
def sfContent():
    sflist=[
        '猪年到喜迎门，送欢乐送祝福，愿您新春欢乐，万事如意，阖家欢乐，百事顺心，吉星高照，添福添寿，幸福美满，快乐一生！',
        '猪年新春到，心情无限妙；快乐把门敲，喜庆身边绕；吉祥跟你跑，幸福对你笑；健康来拥抱，愿你身体好；新的一年，愿你生活美满，幸福逍遥！',
        '朝霞映满天，盛世耀猪年。歌美舞翩翩，快乐太平年。瑞雪一片片，幸福绕猪年。春风暖心田，欢度团圆年。猪年到了，愿你快乐绵绵！'
    ]
    return random.choice(sflist)