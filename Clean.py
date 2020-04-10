#! /usr/bin/python

import os
import sys
import shutil as sh

def rm():
  if len(sys.argv)==1:
    try:
      sh.rmtree('links')
      sh.rmtree('tmp')
    except FileNotFoundError:
      print('links/ And tmp/ Already Deleted')  
    sh.rmtree('content')
    sh.rmtree('profiles')
    os.remove('geckodriver.log')
    #os.remove('ghostdriver.log')
 
    print('Full Clean')
    return

  if sys.argv[1]=='-k':
    try:
      sh.rmtree('links')
    except FileNotFoundError:
      sh.rmtree('tmp')
  
    print('links/ And tmp/ Removed')

rm()
