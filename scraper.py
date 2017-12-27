# -*- coding: utf-8 -*-
# import libraries
import csv
import urllib2
from bs4 import BeautifulSoup

#Lists that will be plotted
images = []
links = []
meta_tags = []
len_tags = []

'''
Parses the url
Keeps track of the num of images, links, and meta tags.
In addition to the average length of each meta tag
'''
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
    
        #Parse the website
        soup = BeautifulSoup(page, 'html.parser')
    except:
        return
    
    
    #Fetch all images in the current website
    img = soup.findAll(['img'])
    for i in img:
        num_images = num_images + 1
    images.append(num_images)

    #Fetch all links in the current website
    lks = soup.findAll(['a'])
    for lk in lks:
        num_links = num_links + 1
    links.append(num_links)


    #Fetch all meta tags in the current website
    tags = soup.findAll(attrs={"name":"description"})
    for tag in tags:
        num_meta = num_meta + 1
        #Find the length of the content part in the html meta tag
        try:
            total_meta_len += len(str(tag['content'].encode('utf-8')))
        except:
            pass
    meta_tags.append(num_meta)
    #Compute average
    try:
        avg_meta_len = total_meta_len / num_meta
    except:
        avg_meta_len = 0
    len_tags.append(avg_meta_len)


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

i = 1
for site in sites:
    print('(' + str(i) + '/' + str(500) + '), ' + site)
    i += 1
    parse(site)

print('Sites successfully scrapped')
print('Starting CSV creation process')

#Write to csv file
with open('scrapped-results.csv', 'wb') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    #Custom Header
    header = ['Links', 'Images', 'Meta Name Tags', 'Avg. Meta Tag Length']
    writer.writerow(header)
    
    for i in range(0, len(links)):
        msg = []
        msg.append(links[i])
        try:
            msg.append(images[i])
            msg.append(meta_tags[i])
            msg.append(len_tags[i])
        except:
            pass
        writer.writerow(msg)
        i += 1

print('CSV file successfully created')
print('Final results')



