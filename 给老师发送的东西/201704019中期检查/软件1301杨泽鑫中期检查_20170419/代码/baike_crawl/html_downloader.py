'''
Created on 2017年4月14日

@author: mywow
'''
from urllib import request;


class HtmlDownloader(object):
    
    
    def download(self,url):
        if url is None:
            return None
        response =request.urlopen(url)
        
        if response.getcode()!=200:
            return None
        else:
            return response.read().decode("utf-8")


