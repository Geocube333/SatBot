#! /usr/bin/python

import os
import shutil as sh
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

  if os.path.isdir('finalposts')==False:
    os.mkdir('finalposts')

  sortedHashes = sorted(hashlist)
  savedIndexes=[]

  for i in sortedHashes:
    savedIndexes.append(hashlist.index(i))

  savedIndexes.sort()
  savedIndexes=list(dict.fromkeys(savedIndexes))
  print(savedIndexes)

  for i in savedIndexes:
    try:
      sh.move('content/'+fileType+str(i)+ext, 'finalposts/'+fileType+str(i)+ext)
    except FileNotFoundError:
      print('File is not a '+fileType+' Or doesn\'t exist')

for i in range(len(dirs)):

  if dirs[i].startswith('video'):
    video(i)
  
  if dirs[i].startswith('image'):
    image(i)

dele('video','.mp4')
dele('image','.jpg')
