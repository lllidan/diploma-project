'''
Created on 2017年4月15日

@author: mywow
'''

#!/usr/bin/env python
# encoding: utf-8
# @author: cc <chai_pengfei@163.com>

import requests
import re
import os.path
from sqlalchemy.sql.expression import false
from asyncio.tasks import sleep

class HuabanCrawler():
    """ 抓去花瓣网上的图片 """

    def __init__(self):
        """ 在当前文件夹下新建images文件夹存放抓取的图片 """
        self.homeUrl = "http://huaban.com/search/?q=saber"
        self.images = []
        if not os.path.exists('./images'):
            os.mkdir('./images')
        self.count=0

    def __load_homePage(self):
        """ 加载主页面 """
#         print(requests.get(url = self.homeUrl).content)
        return requests.get(url = self.homeUrl).content

    def __make_ajax_url(self, No):
        """ 返回ajax请求的url """
        return self.homeUrl + "&j1j9x6vx&page=" + str(No) + "&per_page=20&wfl=1"

    def __load_more(self, maxNo):
        """ 刷新页面 """
        return requests.get(url = self.__make_ajax_url(maxNo)).content

    def __process_data(self, htmlPage):
        
        """ 从html页面中提取图片的信息 """
        prog = re.compile(r'app\.page\["pins"\].*')
        
        htmlPage=htmlPage.decode('utf-8')
        
        appPins = prog.findall(htmlPage)
    
        
#         print(len(appPins[0][19:-1]))
        # 将js中的null定义为Python中的None
        # 将js中的true定义为Python中的True
        # 将js中的false定义为Python中的False
        null = None
        true = True
        false =False
        if appPins == []:
            return None
        result = eval(appPins[0][19:-1])
#         print(appPins[0][19:-1])
        for i in result:
            info = {}
            info['id'] = str(i['pin_id'])
            
            info['url'] = "http://img.hb.aicdn.com/" + i["file"]["key"] + "_fw658"
            if 'image' == i["file"]["type"][:5]:
                info['type'] = i["file"]["type"][6:]
            else:
                info['type'] = 'NoName'
            self.images.append(info)

#         print(self.images)
    def __save_image(self, imageName, content):
        """ 保存图片 """
        with open(imageName, 'wb') as fp:
            fp.write(content)
#         self.count+=1
#         print('第%s个图片已下载完毕' % self.count)

    def get_image_info(self, num):
        """ 得到图片信息 """
        self.__process_data(self.__load_homePage())
        print(int((num-1)/20))
        #网站默认初始一次加载20个图片，需要动态加载的次数也就是20的倍数
        for i in range(int((num-1)/20)):
        
#         for i in range(10):
            self.__process_data(self.__load_more(i+3))
        
        return self.images

    def down_images(self):
        """ 下载图片 """
        print ("{} image will be download".format(len(self.images)))
        for key, image in enumerate(self.images):
            print ('download {0} ...'.format(key+1))
            try:
                req = requests.get(image["url"])
            except :
                print ('error')
            imageName = os.path.join("./images", image["id"] + "." + image["type"])
            self.__save_image(imageName, req.content)

        
if __name__ == '__main__':
    hc = HuabanCrawler()
    hc.get_image_info(100)
    hc.down_images()
