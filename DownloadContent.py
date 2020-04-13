#! /usr/bin/python

import gc
import urllib.request
import selenium.webdriver as wd 
from bs4 import BeautifulSoup
import os
import sys

with open("links/links.txt", 'r') as f:
  #if os.path.isdir("Content")==False:
  #  os.mkdir("Content")
  
  contentLinks=f.readlines()

dirSize=len(os.listdir("links"))
fileNum=0
vid=False
pic=False
links=[]

if len(sys.argv)==2:
  fileNum=int(sys.argv[1])

for l in contentLinks:
  options = wd.FirefoxOptions()
  options.add_argument('-headless')
  
  download=wd.Firefox(options=options)
  download.get(l)

  soup=BeautifulSoup(download.page_source, 'html.parser')
  imageUrl=str(soup.findAll('img', {'class':'FFVAD'}))
  videoUrl=str(soup.findAll('video', {'class':'tWeCl'}))

  if len(videoUrl)==2:
    contentUrl=imageUrl
    pic=True
  elif len(videoUrl)!=0:
    contentUrl=videoUrl
    vid=True

  if vid:
    extension='.mp4'
    filename='video'
  if pic:
    extension='.jpg'
    filename='image'

  if os.path.isdir("tmp")==False:
    os.mkdir("tmp")
  if os.path.isfile("tmp/cdTemp.txt")==False:
    os.mknod("tmp/cdTemp.txt")

  if os.path.isdir("content")==False:
    os.mkdir("content")

  with open('tmp/cdTemp.txt', 'a+') as f:
    f.write(contentUrl)
  
  with open('tmp/cdTemp.txt', 'r') as f:
    clean=f.read().split()
    for l in clean:
      if l.startswith('src="'):
        temp=l.replace('amp;', '')
        temp=temp.replace('"', '')
        temp=temp.replace('src=', '')
        #try:
        urllib.request.urlretrieve(temp, 'content/'+filename+str(fileNum)+extension)
        urllib.request.urlcleanup()
        #except 

  os.remove('tmp/cdTemp.txt')

  print("Page Downloaded: "+str(fileNum))
  fileNum+=1

  soup.decompose()
  download.quit()
  gc.collect()

