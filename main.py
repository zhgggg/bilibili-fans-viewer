import time
import re
from urllib import request
hitokoto = 'https://v1.hitokoto.cn/?encode=text'#一言
req = request.Request(hitokoto)
page = request.urlopen(req).read()
page = page.decode('utf-8')
sentence = page
print (sentence)

now = time.strftime("%m月%d日%H:%M:%S", time.localtime())
print ('现在是北京时间' + now)
print("欢迎使用 BILIBILI掉粉小助手！")

uid = input("输入你想查询的uid:")
sec = input("输入监测频率(单位:秒)")

print("查询ing")

url = 'https://api.bilibili.com/x/relation/stat?vmid=' + uid + '&jsonp=jsonp'
req = request.Request(url)
page = request.urlopen(req).read()
page = page.decode('utf-8')
string = page
begin_follower = int(re.findall('"follower":([0-9]*)',string,flags=0)[0])
oldnow_follower = begin_follower
#获取初始粉丝
nameget = 'https://api.bilibili.com/x/space/acc/info?mid='+ uid
namereq = request.Request(nameget)
npage = request.urlopen(namereq).read()
npage = npage.decode('utf-8')
cod = npage
#获取用户信息
var1 = 7
var2 = 3
first = (cod.find('name'))
last = (cod.find('sex'))
rfirst = first + var1
rlast = last - var2
name = cod[rfirst:rlast]
#从用户信息中截出用户名

while True:

    now_follower = int(re.findall('"follower":([0-9]*)',string,flags=0)[0])
    rundis_follower = oldnow_follower  - now_follower
    dis_follower = begin_follower - now_follower

    print("[掉粉小助手]" + "当前时间：" + str(now) + "     ""您正在监测"+name+"的粉丝数据     " +name+ "粉丝现在为:" + str(now_follower) + "人"     "总共取关了" + str(dis_follower) + "人     实时取关了" + str(rundis_follower) + "人" )
    with open("log.txt","a") as f: 
        f.writelines("\n" + now  + "     " + name + "粉丝现在为:" + str(now_follower) + "     总共取关了" + str(dis_follower) + "人     实时取关了" + str(rundis_follower) + "人")
        f.close()
    #记事本数据库2333333
    oldnow_follower = now_follower
    time.sleep(int(sec))#自动休眠
