# -*- coding: utf-8 -*-
# import libraries
import csv
import urllib2
from bs4 import BeautifulSoup

'''Parses the url
#Keeps track of the num of images, links, and meta tags.
In addition to the average length of each meta tag. '''
def parse(url):
    #Values we are keeping track of
    num_images = 0
    num_links = 0
    num_meta = 0
    total_meta_len = 0
    avg_meta_len = 0
    
    #Get the page
    try:
        page = urllib2.urlopen(url)
    except:
        return

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
    tags = soup.findAll(attrs={"name":"description"})
    for tag in tags:
        num_meta = num_meta + 1
        #Find the length of the content part in the html meta tag
        try:
            total_meta_len += len(str(tag['content'].encode('utf-8')))
        except:
            pass

    #Print the number of meta tags
    print(url + ' has ' + str(num_meta) + ' meta name tags on the landing page')
    try:
        avg_meta_len = total_meta_len / num_meta
    except:
        avg_meta_len = 0

    print(url + ' has an average meta name tag length of ' + str(avg_meta_len) + ' on the landing page')


print('Starting CSV file load process')
sites = []
#Load the csv file and store all websites in sites[]
with open('top-500-websites.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        sites.append('https://www.' + row[1])
print('CSV file loaded successfully')

#Remove the head element from the list
sites.pop(0)

for site in sites:
    print(site)
    parse(site)

print('Sites successfully scrapped')











