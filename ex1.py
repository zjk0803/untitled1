from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
import urllib.request
def imageSpider(url):
    try:
        urls = []
        req = urllib.request.Request(url,headers=headers)
        data = urllib.request.urlopen(req)
        data = data.read()
        dammit = UnicodeDammit(data,["utf-8"])
        data = dammit.unicode_markup
        soup = BeautifulSoup(data,"lxml")
        images = soup.select("img")
        for image in images:
            try:
                src = image["src"]
                url1 = urllib.request.urljoin(url,src)
                if url1 not in urls:
                    urls.append(url1)
                    print(url1)
                    download(url1)
            except Exception as err:
                print(err)
    except Exception as err:
        print(err)

def download(url):
    global count
    try:
        count+=1
        if(url[len(url)-4]=="."):
            ext = url[len(url)-4:]
        else:
            ext = ""
        req = urllib.request.Request(url,headers=headers)
        data = urllib.request.urlopen(req,timeout=1000)
        data = data.read()
        fobj = open("images\\" + str(count) + ext,"wb")
        fobj.write(data)
        print("download" + str(count) + ext)
    except  Exception as err:
        print(err)
start_url = "https://www.zhihu.com/question/62753680"
headers = {

        "User - Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763"
    }
count = 0
imageSpider(start_url)

