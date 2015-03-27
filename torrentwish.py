#!/usr/bin/env python2
import requests
from bs4 import BeautifulSoup
import pynotify
import urllib2
import datetime

def sendnotif(title, notif):
	 pynotify.init("Test")
	 notice = pynotify.Notification(title, notif)
	 notice.show()
	 return

f = open('torrentwish_log.txt','a')
f.write('\nStart:' + str(datetime.datetime.now()))
f.close()

print "Welcome to the Password Changer program."
print "Created by: Shobhit K. Deepanker"
print "Year: 2015\n"

torr_name_add = raw_input("Enter the name of the torrent you want to add to your wish list:")

url = "https://kickass.to/usearch/" + torr_name_add + "/?rss=1"

rss_file = urllib2.urlopen(url)
#convert to string:
rss_data = rss_file.read()
print rss_data
#close file because we dont need it anymore:
rss_file.close()

