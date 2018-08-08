#!/usr/bin/env python
# _*_enconding:utf-8_*_
# TIME:2018/7/25 10:14
# FILE:control.py
import os



class test(object):
    def __init__(self, slot, diskname):
        self.slot = str(slot)
        self.diskname = diskname

    def diskStat(self):
        slot_list = []
        if os.path.exists('storge.json'):
            with open('storge.json', "r") as fd:
                msg = eval(fd.read())
                for key, value in msg.items():
                    slot_list.append(value["slot"])
                    if self.slot == value["slot"]:
                        print(value["off"])
        if self.slot in slot_list:
            return True
        else:
            return False

    def getDiskStat(self):
        if os.path.exists("/sys/block/".format(self.diskname)):
             return True
        else:
            return False



print(test(21).diskStat())