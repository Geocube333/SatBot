#! /usr/bin/python

import os
#import requests
import selenium.webdriver as wd
from bs4 import BeautifulSoup
import gc

with open('Sources.txt', 'r') as f:
  pages=f.readlines()    

prog=len(pages)
cnt= 0
print(0.0)

for p in pages:
  print("New Profile Loaded (#"+str(int(cnt+1))+")")
  
  p=p.strip('\n')
  currentPage="https://www.instagram.com/"+p+"/"
  cnt+=.2
  print(100*(cnt/prog))

  options = wd.FirefoxOptions()
  options.add_argument('-headless')
  cnt+=.2
  print(100*(cnt/prog))

  download=wd.Firefox(options=options)
  download.get(currentPage)
  cnt+=.2
  print(100*(cnt/prog))

  soup=BeautifulSoup(download.page_source, 'html.parser')
  imageUrl=soup.findAll('div', {'class':'v1Nh3 kIKUG _bz0w'})
  
  cnt+=.2
  print(100*(cnt/prog))

  if os.path.isdir("profiles")==False:
    os.mkdir("profiles")
  if os.path.isdir("profiles/"+p)==False:
    os.mkdir("profiles/"+p)
  if os.path.isfile("profiles/"+p+"/"+p+"-data")==False:
    os.mknod("profiles/"+p+"/"+p+"-data")

  #print(soup)
  with open("profiles/"+p+"/"+p+"-data", 'a+') as f:
    for i in imageUrl:
      f.write(str(i))
  
  soup.decompose()
  download.quit()
  gc.collect()

  cnt+=.2
  print(100*(cnt/prog))

