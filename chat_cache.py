import redis 
from hashlib import md5
import random
import requests
import json


class chat_cache:

	def __init__(self):
		pool = redis.ConnectionPool(host='chat-redis.izdgsg.ng.0001.apse1.cache.amazonaws.com', port=6379, decode_responses=True)
		self.r = redis.Redis(connection_pool=pool)
		self.url = "http://cognitive.nuwarobotics.cn:5006/v3/chatbot/product"
		self.data = {"dialog": ["加油"]}

	def use_cache(self):

		res = requests.post(self.url, json=self.data)
		answer = json.loads(res.text)['chat']
		question_list = list(self.data["dialog"])

		if len(question_list) > 2:

		   print(question_list[-3:])
		   chat_list = question_list[-3:]

		elif len(question_list) > 1:
		   
		   print(question_list[-2:])
		   chat_list = question_list[-2:]

		else:
		   
		   print(question_list[-1:])
		   chat_list = question_list[-1:]  


		index = md5(str(chat_list).encode("utf-8")).hexdigest()

		print(answer)
		print(index)

		if self.r.smembers(index):

		   print("exist")
		   print(self.r.srandmember(index))

		else:

		   print("no exist")
		   self.r.sadd(index, answer)
		   print(answer)

	def add_cache(self):

		res = requests.post(self.url, json=self.data)
		answer = json.loads(res.text)['chat']

		question_list = list(self.data["dialog"])

		if len(question_list) > 2:

		   print(question_list[-3:])
		   chat_list = question_list[-3:]

		elif len(question_list) > 1:
		   
		   print(question_list[-2:])
		   chat_list = question_list[-2:]

		else:
		   
		   print(question_list[-1:])
		   chat_list = question_list[-1:]  


		index = md5(str(chat_list).encode("utf-8")).hexdigest()

		print(answer)
		print(index)

		if self.r.smembers(index):

		   print("exist")
		   self.r.sadd(index, answer)
		   print(answer)

		else:

		   print("no exist")
		   self.r.sadd(index, answer)
		   print(answer)


if __name__ == '__main__':
	c = chat_cache()
	#.use_cache()
	for i in range(10):
		c.add_cache()
