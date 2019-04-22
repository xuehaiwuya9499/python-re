from bs4 import BeautifulSoup
import requests
import bs4
import time
import lxml
import re
def standardization():
    global txt
    start,end=0,len(txt)
    while True:
        a1=re.compile(r'>[^<>/]+?<span')
        match1=a1.search(txt[start:])
        if match1:
            cut1,cut2=match1.start()+1+len(txt[0:start]),match1.end()-2-3+len(txt[0:start])
            start=match1.end()-2-3
        else:
            break
        a2=re.compile(r'>[^<>/]*?</span')
        match2=a2.search(txt[start:])
        if match2:
            insertPoint=match2.start()+1+len(txt[0:start])
            start=match2.end()-2-4
        else:
            break
        txtcatch=txt[0:cut1]+txt[cut2:insertPoint]+txt[cut1:cut2]+txt[insertPoint:]
##        print('txt[0:cut1]:',txt[0:cut1])
##        print('txt[cut2:insertPoint]:',txt[cut2:insertPoint])
##        print('txt[cut1:cut2]:',txt[cut1:cut2])
##        print('txt[insertPoint:]:',txt[insertPoint:])
        txt=''
        txt=txtcatch
def getHTMLText(url):
##    try:
##        r=requests.get(url)
##        r.raise_for_status()
##        r.encoding=r.apparent_encoding
##        return r.text
##    except:
##        print('爬取失败！')
##        return ''
    return '<p style="line-height: 1.75em;">A：<span style="caret-color: red;">我负责的是跳组，校运会递交报名表那几天心情很复杂，因为有的同学没有项目。因为田赛需要的人少，但跳组人挺多的，他们为了最后能够参加运动会，每天重复一遍又一遍的基础动作，再累再苦也都在坚持，我觉得这些00后的小孩，都很棒！</span></p><p><br  /></p><p style="line-height: 1.75em;"><span style="caret-color: red;">Q：带队比较辛苦，你觉得是什么原因让你一直坚持到了现在？</span></p><p style="line-height: 1.75em;">A:也是<span style="caret-color: red;">有感情了吧，在体育部两年，带了两年的田径队。有时候一天上完课很累，但一去田径场感觉立马就不一样了，陪他们一起训练，最后一起放松聊聊天，也不用想那么多。田径队很简单，让我感到很舒服。</span></p><p><br  /></p><p style="line-height: 1.75em;">Q:<span style="caret-color: red;">你一直为比赛坚持着，现在比赛结束了，你此刻的心情是怎么样的呢？</span></p><p style="line-height: 1.75em;">A:<span style="caret-color: red;">两天半的比赛真的激动，感觉那么久的努力没有白费，看到他们那么努力，真的感动。结束以后有点不舍，时间过得太快了，总觉得第一天训练好像没过去多久，现在就要结束了。虽然在一个学校，但以后见面的机会也不会太多。我想说：＂我会非常想念你们的。＂</span></p></section></section>'
#    return '<p style="line-height: 1.75em;">A：<span style="caret-color: red;">我负责的是跳组，校运会递交报名表那几天心情很复杂，因为有的同学没有项目。因为田赛需要的人少，但跳组人挺多的，他们为了最后能够参加运动会，每天重复一遍又一遍的基础动作，再累再苦也都在坚持，我觉得这些00后的小孩，都很棒！</span></p><p><br  /></p><p style="line-height: 1.75em;"><span style="caret-color: red;">Q：带队比较辛苦，你觉得是什么原因让你一直坚持到了现在？</span></p><p style="line-height: 1.75em;">A:也是<span style="caret-color: red;">'
#    return '<p style="line-height: 1.75em;"><span style="caret-color: red;">Q：带队比较辛苦，你觉得是什么原因让你一直坚持到了现在？</span></p><p style="line-height: 1.75em;">A:也是<span style="caret-color: red;">'
#    return '<p style="line-height: 1.75em;">A：<span style="caret-color: red;">我负责的是跳组，校运会递交报名表那几天心情很复杂，因为有的同学没有项目。因为田赛需要的人少，但跳组人挺多的，他们为了最后能够参加运动会，每天重复一遍又一遍的基础动作，再累再苦也都在坚持，我觉得这些00后的小孩，都很棒！</span></p><p><br  /></p>'

def extractTxt(ls):
    global txt
    flag=True
    soup=BeautifulSoup(txt,'lxml')
    #用soup.find_all(True)遍历所有标签
    for so in soup.find_all(True):
        #判断so是否为标签类型
        if isinstance(so,bs4.element.Tag):
            #判断一个标签的NavigableString是否存在
            if isinstance(so.string,bs4.element.NavigableString):
                if so.name in {'p','title','span'}:
                    if so.name=='p':
                        if 'span' in so.contents:
                            flag=False
                        else:
                            flag=True
                    if so.name=='span':
                        if so.parent.name in {'p','span'}:
                            flag=True
                        else:
                            flag=False
                    if flag:
                        ls.append(so.string)
                    else:
                        continue
def save(ls,path='文字'):
    f=open(path+str(time.time()).replace('.','')+'.txt','w',encoding='utf-8')
    print(len(ls))
    for l in ls:
        f.write(l+'\n')
    f.close()
def main():
    global txt
    url=input('请输入微信公众号文章的链接：')
    txt=getHTMLText(url)
    txt=re.sub(r'<[^<>]+?/>','',txt)
    txt=re.sub(r'<p></p>','',txt)
    standardization()
    f2=open('123.txt','w',encoding='utf-8')
    f2.write(txt)
    f2.close()
    ls=[]
    extractTxt(ls)
    save(ls)
txt=''
main()
