##本程序现仅能提取“河南农业大学农学院微信公众号的文章”
import requests
from bs4 import BeautifulSoup
import bs4
import time
import lxml
import re
def getHTMLText(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print('爬取失败！')
        return ''
def extractTxt(txt,ls):
    soup=BeautifulSoup(txt,'lxml')
    for so in soup.find_all(True):
        if isinstance(so,bs4.element.Tag):
            if isinstance(so.string,bs4.element.NavigableString):
                if so.name=='p':
                    ls.append(so.string)
def save(ls,path='文字'):
    f=open(path+str(time.time()).replace('.','')+'.txt','w',encoding='utf-8')
    print(len(ls))
    for l in ls:
        f.write(l+'\n')
    f.close()
def main():
    url=input('请输入微信公众号文章的链接：')
    txt=getHTMLText(url)
    txt=re.sub(r'<[^<>]+?/>','',txt)
    ls=[]
    extractTxt(txt,ls)
    save(ls)
main()
