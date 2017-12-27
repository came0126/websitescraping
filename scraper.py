# -*- coding: utf-8 -*-
# import libraries
import urllib2
from bs4 import BeautifulSoup

#Parses the url
#Keeps track of the num of images, links, and meta tags.
#In addition to the average length of each meta tag.
def parse(url):
    #Values we are keeping track of
    num_images = 0
    num_links = 0
    num_meta = 0
    total_meta_len = 0
    avg_meta_len = 0
    
    #Get the page
    page = urllib2.urlopen(url)
    #Parse the website
    soup = BeautifulSoup(page, 'html.parser')
    
    #Fetch all images in the current website
    img = soup.findAll(['img'])
    for i in img:
        num_images = num_images + 1
    #Print the number of images
    print(url + ' has ' + str(num_images) + ' images on the landing page')

    #Fetch all links in the current website
    links = soup.findAll(['a'])
    for lk in links:
        num_links = num_links + 1
    #Print the number of links
    print(url + ' has ' + str(num_links) + ' links on the landing page')

    #Fetch all meta tags in the current website
    tags = soup.findAll(['meta'])
    for tag in tags:
        #Subtract 11 for length of html formatting, about 3-8 characters off for each calculation.
        total_meta_len += len(str(tag)) - 11
        num_meta = num_meta + 1
    #Print the number of meta tags
    print(url + ' has ' + str(num_meta) + ' meta tags on the landing page')
    avg_meta_len = total_meta_len / num_meta
    print(url + ' has an average meta tag length of ' + str(avg_meta_len) + ' on the landing page')


#Sample website to scrap
parse('http://www.vimeo.com')


