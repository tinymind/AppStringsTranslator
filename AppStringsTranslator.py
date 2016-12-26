#!/usr/bin/python  
#-*- coding:utf-8 -*-  

# 百度翻译 API 文档：http://api.fanyi.baidu.com/api/trans/product/apidoc

import httplib
import md5
import urllib
import random
import re
import json
import os
import sys


kBaiduAppID = 'Please generate from you Baidu developer center' # 百度开发管理后台申请的 AppID
kBaiduSecretKey = 'Please generate from you Baidu developer center'  # 百度开发管理后台申请的 SecretKey


gStringsFileName = ''
gStringsKeyList = []
gStringsValueList = []
gAllSupportedLangList = ['auto', 'zh', 'en', 'yue', 'wyw', 'jp', 'kor', 'fra', 'spa', 'th', 'ara', 'ru', 'pt', 'de', 'it', 'el', 'nl', 'pl', 'bul', 'est', 'dan', 'fin', 'cs', 'rom', 'slo', 'swe', 'hu', 'cht', 'vie']


reload(sys)
sys.setdefaultencoding( "utf-8" )


def initStringsKeyValueFromFile(fileName):
	global gStringsFileName
	global gStringsKeyList
	global gStringsValueList

	gStringsFileName = fileName

	try:
		f = open(fileName, 'r')  
		lines = f.readlines()  
	except IOError as e:  
		print e  
	else:
		for line in lines:  
			match = re.search(r'"(?P<key>.*?)" = "(?P<value>.*?)"', line)
			if match:
				gStringsKeyList.append(match.group('key'))
				gStringsValueList.append(match.group('value'))
			else:
				# 为了保存注释或空行到新的翻译文件
				gStringsKeyList.append(line)
				gStringsValueList.append('')
	finally:  
		f.close()


def translateToLanguageList(fromLang, toLangs):
	if fromLang not in gAllSupportedLangList:
		print fromLang + 'is not supported'
		return

	for toLang in toLangs:
		if toLang not in gAllSupportedLangList:
			print toLang + 'is not supported'
			break
		translateToLang(fromLang, toLang)


def translateToLang(fromLang, toLang):
	httpClient = None
	myurl = '/api/trans/vip/translate'
	
	httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')

	extension = os.path.splitext(gStringsFileName)[1]
	toFileName = gStringsFileName.replace(extension, '_' + toLang + extension)
	toFile = open(toFileName, 'w');

	print 'Translating ' + toLang + ' to fileName: ' + toFileName

	for index,val in enumerate(gStringsValueList):
		q = val

		if q:
			salt = random.randint(32768, 65536)

			sign = kBaiduAppID + q + str(salt) + kBaiduSecretKey
			m1 = md5.new()
			m1.update(sign)
			sign = m1.hexdigest()
			myurl = myurl + '?appid=' + kBaiduAppID + '&q=' + urllib.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign
			 
			try:
				httpClient.request('GET', myurl)
			 
				#response是HTTPResponse对象
				response = httpClient.getresponse()

				jsonData = json.loads(response.read())
				dst = jsonData['trans_result'][0]['dst']

				result = '"' + gStringsKeyList[index] + '" = "' + dst + '";\n'
				toFile.write(result)

			except Exception, e:
				print e

		else:
			# 不需要翻译，直接保存原来的 Key
			toFile.write(gStringsKeyList[index])

	if httpClient:
		httpClient.close()

	if toFile:
		toFile.close()

	print 'Finished translating to ' + toLang 


fileName = raw_input('Enter a fileName: ')
initStringsKeyValueFromFile(fileName)
print 'Supports languages:'
print gAllSupportedLangList
fromLang = raw_input('Enter from language: ')
toLangs = raw_input('Enter to language list, split by space: ')
print 'Start'
translateToLanguageList(fromLang, toLangs.split())
print 'All done!'

