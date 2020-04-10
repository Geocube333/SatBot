#! /usr/bin/python

import os
import hashlib as h

hashlist=[]
dirs=os.listdir('content')

def video(i):
  with open('content/video'+str(i)+'.mp4', 'rb') as f:
    byte=f.read()
    hashlist.append(h.sha1(byte).hexdigest())

def image(i):
  with open('content/image'+str(i)+'.jpg', 'rb') as f:
    byte=f.read()
    hashlist.append(h.sha1(byte).hexdigest())

def dele(fileType, ext):
  burnlist=[]
  num1=0

  for i in hashlist:
    num2=0
    for j in hashlist:
      if i==j and num1 != num2:
        burnlist.append(num2)
        hashlist.pop(hashlist[num2])
      num2+=1
    num1+=1

  burnlist.sort

  for i in burnlist:
    try:
      os.remove('content/'+fileType+str(i)+ext)
    except FileNotFoundError:
      print('File Already Deleted')


for i in range(len(dirs)):

  if dirs[i].startswith('video'):
    video(i)
  
  if dirs[i].startswith('image'):
    image(i)

dele('video','.mp4')
dele('image','.jpg')
