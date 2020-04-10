#! /usr/bin/python

import os

with open('Sources.txt', 'r') as f:
  sources=f.readlines()

links=[]

for s in sources:
  s=s.strip('\n')
  with open("profiles/"+s+"/"+s+"-data",'r') as f:
    clean=f.read().split()

  for c in clean:
      if c.startswith('href="/p'):
        links.append(c.replace('href="', '').replace('"><div', '\n'))
        
  if os.path.isdir("links")==False:
    os.mkdir("links")
  if os.path.isfile("links/links.txt")==False:
    os.mknod("links/links.txt")
  if os.path.isfile("profiles/"+s+"/"+s+"-links")==False:
    os.mknod("profiles/"+s+"/"+s+"-links")

  for l in links:
    with open("links/links.txt", 'a+') as f:
        f.write("https://instagram.com"+l)
    with open("profiles/"+s+"/"+s+"-links", 'a+') as f:
        f.write("https://instagram.com"+l)
