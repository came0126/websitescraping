# -*- coding: utf-8 -*-
# import libraries
import urllib2
from bs4 import BeautifulSoup


def scrap(url):
    #Values we are keeping track of
    num_images = 0
    num_links = 0
    num_meta = 0
    len_meta = 0
    
    #Get the page
    page = urllib2.urlopen(url)
    
    #Parse the website
    soup = BeautifulSoup(page, 'html.parser')
    
    #Fetch all images in the current website
    img=soup.findAll(['img'])
    for i in img:
        num_images = num_images + 1
    
    print(num_images)



scrap('http://www.vimeo.com')


