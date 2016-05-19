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

import json
import urllib2,urllib
from prettytable import PrettyTable

print 'Today\'s weather\n '
api_key = '205fa0fe8e0455c92089ae97d508aaa7'
cityname = raw_input('Enter the city name: ')
url = 'http://api.openweathermap.org/data/2.5/weather?'
values = {'q':cityname,'apikey': api_key ,'units':'metric'}
params = urllib.urlencode(values)
url = url + params
response = urllib.urlopen(url)
data = json.loads(response.read())

t = PrettyTable([' ', ''])
t.add_row(['City Name', data['name']])
t.add_row(['Weather',data["weather"][0]["main"]])
t.add_row(['Description',data["weather"][0]["description"]])
t.add_row(['Temperature',str(data["main"]["temp"]) + ' C'])
t.add_row(['Pressure',str(data["main"]["pressure"]) + ' hpa'])
t.add_row(['Humidity',str(data["main"]["humidity"]) + ' %' ])
print t
