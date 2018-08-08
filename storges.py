#!/usr/bin/env python
# _*_enconding:utf-8_*_
# TIME:2018/7/23 14:58
# FILE:storges.py

import json
import re
from subprocess import Popen, PIPE
import requests


class GetDiskMessage(object):
    def __init__(self):
        self.enclosu = self.getEnclosu()[0]

    def getInfo(self, cmd):
        popen = Popen(cmd, stderr=PIPE, stdout=PIPE, shell=True)
        msg = popen.stdout.read()
        return msg

    def getEnclosu(self):
        cmd = "lsscsi -g"
        enclosu = re.compile(r"[0-9:]+.*JB4242.*(/dev/\w+)$", re.M)
        enclosu_msg = enclosu.findall(self.getInfo(cmd))
        return enclosu_msg

    def getUUID(self, msg):
        cmd = "blkid {}".format(msg)
        uuid_msg = re.compile(r"UUID=\"(.*)\"\sTYPE=.*", re.M)
        uuid = uuid_msg.search(self.getInfo(cmd))
        if uuid:
            uuid = uuid.group(1)
        else:
            uuid = ""
        return uuid

    def getSlotNumber(self):
        cmd = "sg_ses -p2 {}".format(self.enclosu)
        msg = self.getInfo(cmd).split("Element type:")[1]
        compile_msg = re.compile(r"Element\s+(?P<disknum>[0-9]+)[\s\S]+?status:\s(.*)[\s\S]+?Device\soff=(.*)", re.M)
        msg_list = compile_msg.findall(msg)
        slot_num = {}
        disk_msg, enclosu = self.makeJson()
        for id, status, off in msg_list:
            for key, value in eval(disk_msg).items():
                if value == id:
                    slot_num[key] = {"status": status, "slot": id, "off": off, "UUID":self.getUUID(key)}
        return slot_num

    def parseInfo(self):
        cmd = "lsscsi -L -t -g"
        ident = re.compile(
            r"[0-9:]+.*?(?P<diskname>/dev/\w+)\s+(?P<diskgroupname>/dev/\w+)[\s\S]+?bay_identifier=(?P<disknumber>[0-9]+)",
            re.M)
        parse_msg = ident.findall(self.getInfo(cmd))
        return parse_msg

    def makeJson(self):
        disk_dict = {}
        msg = self.parseInfo()
        if msg:
            for i in msg:
                disk_dict[i[0]] = i[2]
            info = json.dumps(disk_dict)
            return info, self.enclosu
        else:
            return False

if __name__ == '__main__':
    msg = GetDiskMessage()
    data = msg.getSlotNumber()
    print(data)
    session = requests.session()
    url = ""
    session.post(url, data=data)