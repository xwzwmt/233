import  pymongo
from bs4 import BeautifulSoup
import requests
import  random
from urllib import request
from multiprocessing import Pool
import time
client=pymongo.MongoClient('localhost',27017)
# baixin=client['baixin']
ershouche1=client['ershouche1']
ershouche_url13=ershouche1['ershouche_url13']

# item_link = ['{}{}?page={}'.format(url_host, channel, str(i)) for i in range(1, 101)]


def qiche(url):
    proxy_list = [
        'http://123.57.72.107:8080',
        'http://221.233.85.64:3128',
        'http://180.127.1.96:25083',
        'http://222.92.141.250:80',
        'http://110.185.170.184:8080',
        'http://166.111.61.227:8123',
        'http://183.245.148.130:80'
    ]
    item=url
    proxy = random.choice(proxy_list)
    proxy_support = request.ProxyHandler({'http': proxy})
    opener = request.build_opener(proxy_support)
    opener.addheaders = random.choice([('User-Agent',
                                        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36Query String Parametersview sourceview URL encoded')
                                       # ('User - Agent', ' Mozilla / 4.0(compatible; MSIE7 .0; WindowsNT6 .0'),
                                       # ('User-Agent',
                                       #  'Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1'),
                                       # ('User-Agent', 'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1'),
                                       # ('User-Agent', 'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)')
                                       ])
    request.install_opener(opener)
    print(item)
    res = requests.get(item)
    print(res)
    time.sleep(random.randint(2, 4))
    # res = requests.get(item)
    soup = BeautifulSoup(res.text, 'lxml')
    titles = soup.select('ul dt a')
    for i in titles:
        title = i['href']
        ershouche_url13.insert_one({'url':title})
        # info_urls.insert({'info_url': info_url})
        print(title)

if __name__ == '__main__':
    url_host = ['http://nmg.cn2che.com/buycar/c3b0c0s0p0c0m0p{}c0r1989m0i0o0o2'.format(str(i)) for i in range(1,27)]

    pool = Pool()
    pool.map(qiche,url_host)
    pool.close()  # 关闭进程池，不再接受新的进程
    pool.join()  # 主进程阻塞等待子进程的退出



