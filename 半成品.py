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
            start=match1.end()-2-3
            cut1,cut2=match1.start()+1,match1.end()-2-3
        else:
            break
        a2=re.compile(r'>[^<>/]*?</span')
        match2=a2.search(txt[start:])
        if match2:
            start=match2.end()-2-4
            insertPoint=match2.start()+1
        else:
            break
        txtcatch=txt[0:cut1]+txt[cut2:insertPoint]+txt[cut1:cut2]+txt[insertPoint:]
        txt=''
        txt=txtcatch
def getHTMLText(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print('爬取失败！')
        return ''
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
                        flag=True
                    if so.name=='span':
                        if so.parent.name=='p':
                            flag=False
                        else:
                            flag=True
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
    standardization()
    f2=open('123.txt','w',encoding='utf-8')
    f2.write(txt)
    f2.close()
    ls=[]
    extractTxt(ls)
    save(ls)
txt=''
main()

