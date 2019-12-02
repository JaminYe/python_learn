import requests
import time
from lxml import etree


def xpath_demo(html):
    html=etree.HTML(html)
    string='//*[@id="app"]/div/div/div[1]/dl/dd['
    for i in range(1,10):
        xpathtest=string+str(i)+']/i/text()'
        print(xpathtest)
        print(html.xpath(string+str(i)+']/i/text()'))
def get_one_page(url):
    try:
        headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}
        response = requests.get(url, headers=headers)  # 构造响应
        if response.status_code == 200:  # 判断状态码
            return response.text
        return None
    except requests.exceptions.RequestException as r:
        return None
url="https://maoyan.com/board/6?offset=0"
html=get_one_page(url)
xpath_demo(html)
