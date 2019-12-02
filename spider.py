
import requests
import time
from lxml import etree

'''
author: Jamin
date: 2019/12/2
'''


'''
创建连接抓取源码
'''
def get_one_page(url):
    try:
        headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}
        response = requests.get(url, headers=headers)  # 构造响应
        if response.status_code == 200:  # 判断状态码
            return etree.HTML(response.text)
        return None
    except requests.exceptions.RequestException as r:
        return None

'''
抓取时间
'''
def spiderTime(html):
    return html.xpath('//*[@id="app"]/div/div/div[1]/p[1]/text()')
'''
爬虫分析
'''
def xpath_demo(html):
    string='//*[@id="app"]/div/div/div[1]/dl/dd['
    for i in range(1,11):
        yield{
        'index':html.xpath(string+str(i)+']/i/text()'),
        'name':html.xpath(string+str(i)+']/div/div/div[1]/p[1]/a/text()'),
        'actor':html.xpath(string+str(i)+']/div/div/div[1]/p[2]/text()'),
        'releasetime':html.xpath(string+str(i)+']/div/div/div[1]/p[3]/text()')
        }

'''
分页抓取
'''
def main(offset):
    url="https://maoyan.com/board/6?offset={0}".format(str(offset*10))
    html=get_one_page(url)
    if i==0:
        print('爬取时间:',spiderTime(html))
    for item in xpath_demo(html):
        print(item)


'''
desc: main方法
'''
if __name__=='__main__':
    print("start".center(200,'-'))
    for i in range(5):
        main(i)
        time.sleep(10)
