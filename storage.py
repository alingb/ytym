#!/usr/bin/env python
# _*_enconding:utf-8_*_
# TIME:2018/7/2 13:51
# FILE:storage.py
import json

import requests
import time

import re
from optparse import OptionParser
from subprocess import Popen, PIPE


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

    def getSlotNumber(self):
        cmd = "sg_ses -p2 {}".format(self.enclosu)
        msg = self.getInfo(cmd).split("Element type:")[1]
        compile_msg = re.compile(r"Element\s+(?P<disknum>[0-9]+)[\s\S]+?status:\s(.*)$", re.M)
        msg_list = compile_msg.findall(msg)
        slot_num = {}
        disk_msg, enclosu = self.makeJson()
        for key, value in msg_list:
            if value != "Not installed":
                slot_num[key] = [{"status": value, "diskname": disk_msg[key]}]
            else:
                continue
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


class ControlDisk(object):
    def __init__(self, disk_msg, enclosu):
        self.disk_msg = disk_msg
        self.enclosu = enclosu
        self.cmd = "sg_ses"
        self.argv0 = "--index=arr,"
        self.open = "--set=devoff"
        self.close = "--clear=devoff"
        self.time = 10

    def openDisk(self, disk):
        cmd = "{0} {1}{2} {3} {4}".format(self.cmd, self.argv0, self.disk_msg[disk], self.open, self.enclosu)
        msg = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)
        msg.communicate()
        var = msg.returncode
        time.sleep(self.time)

    def closeDisk(self, disk):
        cmd = "{0} {1}{2} {3} {4}".format(self.cmd, self.argv0, self.disk_msg[disk], self.close, self.enclosu)
        msg = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)
        msg.communicate()
        var = msg.returncode
        time.sleep(self.time)


if __name__ == '__main__':
    parser = OptionParser(usage="%prog -o or -c diskname", version="%prog V2.30")
    parser.add_option(
        "-o",
        "--open",
        dest="open",
        action="store_true",
        help="open disk"
    )
    parser.add_option(
        "-c",
        "--close",
        dest="close",
        action="store_true",
        help="close disk"
    )
    options, argvs = parser.parse_args()
    disk_msg, enclosu = GetDiskMessage().makeJson()
    if options.open:
        if options.disk:
            ControlDisk(disk_msg, enclosu).openDisk(argvs[0])
        else:
            print("please input control disk name")
    elif options.close:
        if options.disk:
            ControlDisk(disk_msg, enclosu).closeDisk(argvs[0])
        else:
            print("please input control disk name")
