import requests
import re
def getHTMLText(url):
    f1=open('source.txt','r',encoding='utf-8')
    return f1.read()
##    try:
##        r=requests.get(url)
##        r.raise_for_status()
##        r.encoding=r.apparent_encoding
##        return r.text
##    except:
##        print('爬取失败！')
##        return ''
def extractTxt(txt,ls):
    plt=re.findall(r'(<span.*</span>)',txt)
    for i in range(len(plt)):
        txt1=plt[i].split('<')[1].split('>')[1]
        ls.append(txt1)
def save(ls,path='结果.txt'):
    f=open(path,'w',encoding='utf-8')
    print(len(ls))
    for l in ls:
        f.write(l+'\n')
    f.close()
def main():
    url='https://mp.weixin.qq.com/s?src=11&timestamp=1555725706&ver=1557&signature=UJf8XtQah9XzpfeyE9uMsLdJwhcqBdyw0HuGMN206T3ctwmXt9VJxPv5nMq56JrnFnA5qCbfIvhzeGoBvgZFBJpC5tAra2NapeDdD-ct8aS8PvlVKP0NDNtcJ8Wclv-*&new=1'
    txt=getHTMLText(url)
    ls=[]
    extractTxt(txt,ls)
    save(ls)
main()
    
