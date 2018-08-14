#!/usr/bin/python
#  _*_ conding:utf-8 _*_
import json
import urllib
import urllib2
import pymysql
import time
import requests

mysql_conf = {
    "host": "192.168.1.182",
    "user": "root",
    "password": "Snynitfqm$janson10254415",
    "database": "janson_disk"
}

con = pymysql.connect(**mysql_conf)
cur = con.cursor()
while 1:
    cmd = "select janson_id,janson_group_id,forzen_time,add_time from janson_config"
    cur.execute(cmd)
    msg = cur.fetchall()
    now_time = time.time()
    ret, json_ret = [], {}
    for dtime in msg:
        janson_id, janson_group_id, f_time, d_time = dtime
        if int(now_time) - int(d_time) >= int(f_time):
            cmd = "select type,janson_file_id from janson_file where janson_id=\"{}\" and janson_group_id=\"{}\"".format(
                janson_id, janson_group_id)
            cur.execute(cmd)
            ret += [i for i in cur.fetchall() if i]
    num = 0
    for i in ret:
        type, janson_file_id = i
        if type == 0:
            json_ret.update({"janson_file_id_{}".format(num): janson_file_id})
            num += 1
    file_msg = json_ret
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
    # url = "http://trusme.vicp.net:81/index/json/set_file"
    # url = 'http://httpbin.org/post'

    url = "http://localhost/test.php"
    # ret = urllib2.urlopen(url=url, data=urllib.urlencode(file_msg))
    # ret1 = requests.post(url=url, data=json.dumps(file_msg), headers=headers)
    # print file_msg
    ret2 = requests.post(url=url, data=file_msg, headers=headers)
    # print ret.read()
    # print "=" * 50
    # print ret1.text
    # print "-" * 50
    print ret2.text
    time.sleep(2)

