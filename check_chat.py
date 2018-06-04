#!/usr/bin/python3
import requests
import json


url_result = {}
url_chat = { 
        "INIT_API": "http://internal-prod-init-model-947248235.cn-north-1.elb.amazonaws.com.cn:5000/api/init",
	"SENS_API": "http://internal-prod-sens-model-984049648.cn-north-1.elb.amazonaws.com.cn:5000/api/sens",
	"CHATBOT_API_1": "http://internal-prod-qa-model-1561334354.cn-north-1.elb.amazonaws.com.cn:5000/api/qa",
	"CHATBOT_API_2": "http://internal-prod-profile-model-195665453.cn-north-1.elb.amazonaws.com.cn:5000/api/profile",
	"CHATBOT_API_3": "http://internal-prod-s2s-model-1452422277.cn-north-1.elb.amazonaws.com.cn:5000/api/s2s",
	"CHATBOT_API_4": "http://internal-prod-sug-model-1265478512.cn-north-1.elb.amazonaws.com.cn:5000/api/sug",
	"CHATBOT_API_5": "http://internal-prod-s2s-shiwu-1024472403.cn-north-1.elb.amazonaws.com.cn:5000/api/s2s_shiwu",
	"CHATBOT_API_6": "http://internal-prod-s2s-aiqing-1459381811.cn-north-1.elb.amazonaws.com.cn:5000/api/s2s_aiqing",
	"CHATBOT_API_7": "http://internal-prod-s2s-donghwa-1577315554.cn-north-1.elb.amazonaws.com.cn:5000/api/s2s_donghwa"}

data = {"dialog": ["我們聊天"]}


for (k,v) in url_chat.items():

   try:
      #print("dict[%s]=" % k,v)

      res = requests.post(v, json=data)

      url_result[k] = res 

      print(k)
      print(res)

      print(res.text)

      print(json.loads(res.text))

   except:
      print("connection fail") 



print ("")

for (k,v) in url_result.items():
   print (v, k, url_chat[k])
