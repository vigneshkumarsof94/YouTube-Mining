# -*- coding: utf-8 -*-

#Youtube libraries
from gdata.youtube import service
import gdata.youtube
import gdata.youtube.service

#Library to get video details
import pafy

#System R/W Libraries
from datetime import datetime,timedelta
import os
import sys
import csv
import httplib2
#Google Api Service

YOUTUBE_SCOPES = ["https://www.googleapis.com/auth/youtube.readonly","https://www.googleapis.com/auth/yt-analytics.readonly"]
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
YOUTUBE_ANALYTICS_API_SERVICE_NAME = "youtubeAnalytics"
YOUTUBE_ANALYTICS_API_VERSION = "v1"

yt_service = gdata.youtube.service.YouTubeService()

comment_feed_url = "https://gdata.youtube.com/feeds/api/videos/%s/comments?orderby=published&max-results=50"
USERNAME = ''
PASSWORD = ''


# Turn on HTTPS/SSL access.
# Note: SSL is not available at this time for uploads.
#Google Developer Id
yt_service.ssl = True
yt_service.developer_key = 'xxxx'
yt_service.client_id = 'xxxx'

url = ('http://gdata.youtube.com/feeds/api/videos/Y6lGI1SsYn8/comments?' + 'start-index=1&max-results=25')
print 'Title$Time & Date$Tags$PlayerUrl$Link$Likes$Dislikes$Duration$Uploader$Viewers$VideoID'
allc = []

f= open('C:\\Social Media Analytics 2.0\\SocialMediaAnalytics\\YouTube Analytics\\Data\\ChannelComment.csv','w')
cs=csv.writer(f)
data=[['video_id','Author','Comment','DateAndTime']]
cs.writerows(data)
f.close()

def comm_details(video_id):
    client = service.YouTubeService()
    client.ClientLogin(USERNAME, PASSWORD)
    url = comment_feed_url % video_id
    comment_feed = client.GetYouTubeVideoCommentFeed(uri=url)
    for comment in comment_feed.entry:
       try: 
        f= open('C:\\Social Media Analytics 2.0\\SocialMediaAnalytics\\YouTube Analytics\\Data\\ChannelComment.csv','a')
        cs1=csv.writer(f);
        author_name = comment.author[0].name.text
        text = comment.content.text
    
        post_date = comment.published.text
        dat1=[[video_id,author_name,text,post_date]]
        cs1.writerows(dat1)
        
        #last_update_date = comment.update.text
        #print author_name
        #print("{}(date:{}): {}".format(author_name, post_date, text))
       except Exception:
           break
    
def WriteCommentFeed(video_id):
    client = service.YouTubeService()
    client.ClientLogin(USERNAME, PASSWORD)
    url = comment_feed_url % video_id
    comment_feed = client.GetYouTubeVideoCommentFeed(uri=url)
    allComments = []
    while comment_feed:
        try:
             for comment_entry in comment_feed.entry:
                 f= open('C:\\Social Media Analytics 2.0\\SocialMediaAnalytics\\YouTube Analytics\\Data\ChannelComment.csv','a')
                 cs1=csv.writer(f)
                 
                 allc=str(comment_entry.content.text)
                 message=str(allc).replace("\n"," ").replace("\r"," ").replace("  "," ").replace("   "," ").replace("    "," ").replace("     "," ").replace("\t"," ").replace("|"," ").replace("\""," ").replace("﻿","\n").replace("\"","")
                 msg=str(message).replace("\n"," ").replace("\r"," ").replace("  "," ").replace("   "," ").replace("    "," ").replace("     "," ").replace("\t"," ").replace("|"," ").replace("\""," ").replace("﻿","\n").replace("\"","")
                 print message.encode('utf-8')
                 dat1=[[allc]]
                 cs1.writerows(dat1)
                
                
             comment_feed = client.Query(comment_feed.GetNextLink().href)
        except Exception:
             #print "Over"
             break
             
    print allComments
    
#Print Video Details
def PrintEntryDetails(entry):  
  myurl=entry.GetSwfUrl()
  myvid=pafy.new(myurl)
  u=myvid.videoid
    
  print "\"" + str(entry.media.title.text) + "\"" +  '$' + "\"" + str(entry.published.text) + "\"" +  '$' + "\"" + str(entry.media.keywords.text) + "\"" +  '$' + "\"" + str(entry.media.player.url)+ "\"" +  '$' + "\"" +entry.GetSwfUrl()+ "\"" +  '$' + "\"" +str(myvid.likes)+ "\"" +  '$' + "\"" +str(myvid.dislikes)+ "\"" +  '$' + "\"" + str(entry.media.duration.seconds)+ "\"" +  '$' + "\"" + str(myvid.username)+ "\"" +  '$' + "\"" + str(myvid.viewcount)+ "\"" +  '$' + "\"" +str(myvid.videoid)+"\""+ '$' + "\""  +str(comm_details(u)).encode('utf-8')

def PrintVideoFeed(feed):  
 for entry in feed.entry:
   try:  
    PrintEntryDetails(entry)
   except Exception:
    break   

def GetAndPrintUserUploads(username):
          yt_service = gdata.youtube.service.YouTubeService()
          uri = 'http://gdata.youtube.com/feeds/api/users/%s/uploads?max-query=50&start-index=1' %username 
          uri1 = 'http://gdata.youtube.com/feeds/api/users/%s/uploads?max-query=50&start-index=26' %username
          uri2 = 'http://gdata.youtube.com/feeds/api/users/%s/uploads?max-query=50&start-index=51' %username
          uri3 = 'http://gdata.youtube.com/feeds/api/users/%s/uploads?max-query=50&start-index=76' %username
          uri4 = 'http://gdata.youtube.com/feeds/api/users/%s/uploads?max-query=50&start-index=101' %username
          uri5 = 'http://gdata.youtube.com/feeds/api/users/%s/uploads?max-query=50&start-index=126' %username
          uri6 = 'http://gdata.youtube.com/feeds/api/users/%s/uploads?max-query=50&start-index=5000' %username
          PrintVideoFeed(yt_service.GetYouTubeVideoFeed(uri))
          PrintVideoFeed(yt_service.GetYouTubeVideoFeed(uri1)) 
          PrintVideoFeed(yt_service.GetYouTubeVideoFeed(uri2))
          PrintVideoFeed(yt_service.GetYouTubeVideoFeed(uri3))
          PrintVideoFeed(yt_service.GetYouTubeVideoFeed(uri4))
          PrintVideoFeed(yt_service.GetYouTubeVideoFeed(uri5))


GetAndPrintUserUploads('Axe')

#WriteCommentFeed("rq4uxFpHj5o")

#AXE
#doveindia
#ILoveLakme
#Kwality Wall's - Topic
#KissanIndia
#liptontea
#pureitindia
#surfexcel
#rin
#comfort


