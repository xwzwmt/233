import re
from bs4 import BeautifulSoup
import requests
import  pymongo
from bs4 import BeautifulSoup
import requests
import  random
from urllib import request
import time
client=pymongo.MongoClient('localhost',27017)
# baixin=client['baixin']
ershouche1=client['ershouche1']
ershouche_url12=ershouche1['ershouche_url12']
ershouche=client['ershouche']
info_ershouche=ershouche['info_ershouche']

proxy_list=[
    'http://27.46.41.32:9797',
    'http://183.32.88.247:6666',
    'http://47.93.3.242:80',
    'http://60.207.180.1:3128',
    'http://1.197.75.127:808',
    'http://221.217.55.199:9000',
    'http://101.132.146.103:8080'
]

def parse(url):
    url=url
    if url!="http://zhudijun.web.cn2che.com/":
        print(url)
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
        res = requests.get(url)
        # res=requests.get(url)
        soup = BeautifulSoup(res.text, 'lxml')
        # time.sleep(random.randint(1, 2))
        # print(res.text)
        price = None
        carid = None
        brand = None
        sys = None
        area = None
        sendtime = None
        price = soup.select('#price')[0].text
        print(price)
        carid = soup.select('#carid')[0].text
        print(carid)
        car_type = soup.select('#car_state_text')[0].text
        print(car_type)
        brand = re.findall('<li>车辆品牌：(.*?)</li>', res.text, re.S)[0]
        print(brand)
        sys = re.findall('<li>车辆系列：(.*?)</li>', res.text, re.S)[0]
        print(sys)
        area = soup.select('#jydq')[0].text
        print(area)
        sendtime = soup.select('.sendtime')[0].text
        print(sendtime)

        info_ershouche.insert_one(
            {'price': price, 'carid': carid, 'car_type': car_type, 'brand': brand, 'sys': sys, 'area': area,
             'sendtime': sendtime})

    else:
        pass
if __name__=='__main__':
    count=0
    for item in ershouche_url12.find():
        count=count+1
        print(count)
        if count>4755:
            if len(item['url'])>40:
                parse(item['url'])
            else:
                pass
        else:
            pass