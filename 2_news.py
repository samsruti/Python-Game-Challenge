#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python Game Play
# Copyright (C) 2016 Samsruti Dash <sam.sipun@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from lxml import html
import requests
import BeautifulSoup
from bs4 import BeautifulSoup
import lxml.etree
from time import sleep
from time import gmtime, strftime
import os

def Display():
  ans=True
  print '\nPress 1 to Read News and 2 to Exit'
  ans=raw_input("") 
  if ans=="2": 
    ans = False
  else:
    while ans:  
      os.system('clear')
      print "\t\tPython script: News Updates"
      print "Written By: Samsruti Dash"
      print"Time: "+strftime("%H:%M:%S", gmtime())
      print '\n News Updated !!!!'  
      TopStories()
      International()
      National()
      Sports()
      Business()
      Tech()
      sleep(5)
        

def xmlParse(url):
  r = requests.get(url)
  soup = BeautifulSoup(r.text,'lxml')
  count = 1
  for news in soup.find_all('item',limit=1):
      title = news.find("title").text
      print (title)

      

def TopStories():
  url = 'http://feeds.feedburner.com/NdtvNews-TopStories?format=xml'
  print '\nTop Stories:'

def International():
  url = 'http://feeds.feedburner.com/ndtv/TqgX?format=xml'
  print "\nInternational News:", xmlParse(url)

def National():
  url = 'http://feeds.feedburner.com/ndtv/Lsgd?format=xml'
  print "\nNational News: ", xmlParse(url)

def Sports():
  url = 'http://feeds.feedburner.com/NDTV-Sports?format=xml'
  print "\nSports news:", xmlParse(url)

def Business():
  url = 'http://feeds.feedburner.com/NDTV-Business?format=xml'
  print "\nBusiness News:", xmlParse(url)

def Tech():
  url = 'http://feeds.feedburner.com/NDTV-Tech?format=xml'
  print "\nTechnology News: ", xmlParse(url)




Display()

