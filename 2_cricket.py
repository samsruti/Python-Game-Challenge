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

import requests
from bs4 import BeautifulSoup
from time import sleep
import lxml.etree
import json
import re
import urllib2
from time import gmtime, strftime
import os

def notify_message(title, message):
  os.system('notify-send "'+title+'" "'+message+'"')

filename = raw_input("\nEnter the file name you want to save the Live Cricket Scores: ")
with open(filename+".txt", 'wb') as f:
    url = "http://static.cricinfo.com/rss/livescores.xml"
    doc = lxml.etree.parse(url)
    totalNumber_of_matches= int(doc.xpath('count(//item)'))
    f.write("Live Matches: "+ str(totalNumber_of_matches)+"\n")
    while True:
        r = requests.get(url)
        while r.status_code is not 200:
                r = requests.get(url)
        soup = BeautifulSoup(r.text)
        match_id = soup.find_all("guid")
        match_title = soup.find_all("title")
        match_link = soup.find_all("link")
        message_notify_final = ""
        f.write("Time: "+strftime("%H:%M:%S", gmtime()))
        #message_notify_final+="Time: "+strftime("%H:%M:%S", gmtime())
        for x in range(0,totalNumber_of_matches):
            title = match_title[x].text
            if(title != "Cricinfo Live Scores"):
                s = title.split(' v ')
                team_1 = s[0]
                team_1_name = re.sub(r'[*|/|^0-9|&]',r'',team_1)
                team_1_score = re.sub(r'[^0-9|^/|^"  "|^*|^&]',r'',team_1)

                team_2 = s[1]
                team_2_name = re.sub(r'[*|/|^0-9|&]',r'',team_2)
                team_2_score = re.sub(r'[^0-9|^/|^"  "|^*|^&]',r'',team_2)

                
                f.write(team_1_name+" VS "+team_2_name)
                message_notify_final+= "\n"+team_1_name+" VS "+team_2_name
                if(len(team_1_score.split())==0 and len(team_2_score.split())==0):
                    f.write("Match Not Started Yet !!")
                    #message_notify_final+="\n"+ "Match Not Started Yet !!"
                else:
                    f.write(team_1_name+": "+team_1_score+"\n"+team_2_name+": "+team_2_score.strip())
                    message_notify_final+="\n"+team_1_name+": "+team_1_score+"\n"+team_2_name+": "+team_2_score.strip()
                f.write("\n\n")
            #print message_notify_final
            notify_message("Scores Updated",message_notify_final)
        sleep(60)

f.write("Thank you for using this script :)")
