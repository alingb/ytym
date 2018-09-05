#!/usr/bin/env python
# conding:utf-8
# TIME:2018/6/6 17:11
# FILE:test.py
# import document as document
# from pdfminer.converter import PDFPageAggregator
# from pdfminer.pdfparser import PDFParser
# from pdfminer.pdfdocument import PDFDocument
# from pdfminer.pdfpage import PDFPage
# from pdfminer.pdfpage import PDFTextExtractionNotAllowed
# from pdfminer.pdfinterp import PDFResourceManager
# from pdfminer.pdfinterp import PDFPageInterpreter
# from pdfminer.layout import *
# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")
#
# fp = open('Python.pdf', 'rb')
# parser = PDFParser(fp)
# doc = PDFDocument(parser)
# # outlines = doc.get_outlines()
# # for (level, title, dest, a, se) in outlines:
# #     print(level, title)
# if not doc.is_extractable:
#     raise PDFTextExtractionNotAllowed
# rsrcmgr = PDFResourceManager(caching=False)
# laparams = LAParams()
# device = PDFPageAggregator(rsrcmgr, laparams=laparams)
# interpreter = PDFPageInterpreter(rsrcmgr, device)
# file1 = file('Python.txt', 'w+')
# k = 1
# for page in PDFPage.create_pages(doc):
#     if k == 4:
#         break
#     k = k + 1
#     interpreter.process_page(page)
#     layout = device.get_result()
#     for x in layout:
#         if isinstance(x, LTTextBoxHorizontal):
#             print(x)
#             file1.write(x.get_text().encode('gbk', 'ignore'))
# import json
# import urllib2
#
# from django.core.exceptions import MultipleObjectsReturned
#
# data = json.dumps({"name": "MA102222", "sn_list": ["QTFCKJ640000BA", "G1MQ6TQ000073"]})
# a = urllib2.Request('http://192.168.1.57/web/product/', data)
# print(a)
# import time
#
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
#
# DB_CONNECT_STRING = 'mysql+pymysql://trusme:6286280300@192.168.1.57/command?charset=utf8'
# engine = create_engine(DB_CONNECT_STRING, echo=False)
# DB_Session = sessionmaker(bind=engine)
# session = DB_Session()
# start_time = time.time()
# print(session.execute('select count(1) from command.web_host').fetchall())
# end_time = time.time()
# print(end_time - start_time)
# session.close()

# import random
# import time
#
# import os
#
# from selenium import webdriver
#
# url = 'https://kyfw.12306.cn/otn/login/init'
#
# def randomSleep(minS, maxS):
#     time.sleep((maxS-minS)*random.random() + minS)
#     time.sleep((maxS-minS)*random.random() + minS)
#
# chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
# os.environ["webdriver.chrome.driver"] = chromedriver
# driver = webdriver.Chrome(chromedriver)
#
#
# driver.get(url=url)
# randomSleep(2, 5)
# driver.find_element_by_id("username").clear()
# randomSleep(1, 3)
# driver.find_element_by_id("username").send_keys("974644081@qq.com")
# randomSleep(3, 5)
# driver.find_element_by_id("password").send_keys("xxx")
# randomSleep(10, 15)
#
# driver.find_element_by_id("loginSub").click()
# randomSleep(10, 20)
# print(driver.get_cookies())
# driver.close()
# a = 1
# if isinstance(a, int):
#     print("yes")
import json

import requests
session = requests.session()

url = "http://trusme.vicp.net:81/index/disk/m_disk"
url1 = 'http://httpbin.org/post'
data = {"/dev/sdl": {"status": "OK", "slot": "21", "off": "0", "UUID": "ab17e250-d6c2-4ca4-94aa-5c4d26caeba3"}, "/dev/sdj": {"status": "OK", "slot": "17", "off": "0", "UUID": "02648200-ddb5-4d09-ad04-5fdf8a4b7d80"}, "/dev/sdk": {"status": "OK", "slot": "20", "off": "0", "UUID": "0bb8fff3-7883-41e8-bc9b-3e6a51a1398e"}, "/dev/sdh": {"status": "OK", "slot": "13", "off":"0", "UUID": "532a79ce-27e8-4d74-920e-1e509d99dea7"}, "/dev/sdi": {"status": "OK", "slot": "16", "off": "0", "UUID": "ca217eaa-93e4-42a6-a121-04b957438689"}, "/dev/sdf": {"status": "OK", "slot": "9", "off": "0", "UUID": "513a56b8-51f2-45ef-bcfe-a288bad55de7"}, "/dev/sdg": {"status": "OK", "slot": "12", "off": "0", "UUID": "fe2e8c01-8d61-4500-a3e2-cafca288adb6"}, "/dev/sdd": {"status": "OK", "slot": "5", "off": "0", "UUID": "454996b0-7bf3-47c2-b66b-4b34df0db6ee"}, "/dev/sde": {"status": "OK", "slot": "8", "off": "0", "UUID": "ec1f464b-b4c6-41e6-8510-e288cfa95dbb"}, "/dev/sda": {"status": "OK", "slot": "1", "off": "0", "UUID": ""}}
headers = {"Content-type": "application/x-www-form-urlencoded"}
# req = session.post(url1, data=json.dumps(data), headers=headers)
# print(req.url)
# print(req.text)
# print "status_code:{}".format(req.status_code)

import urllib
import urllib2

# data = {'name': 'jiezhi', 'age': '24'}
# ret = urllib2.urlopen(url=url1, data=urllib.urlencode(data))
ret = urllib2.urlopen(url=url1, data=json.dumps(data))
print(ret.read())
