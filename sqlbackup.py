#!/usr/bin/env python
# _*_enconding:utf-8_*_
# TIME:2018/4/27 11:10
# FILE:sqlbackup.py

import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ytym.settings")
django.setup()

from web.models import Host, TestHost

def getSqlMsg(Obj, info, num):
    obj = Obj.objects.order_by(info).values()[:num]
    return obj


def sqlDelete(Obj):
    obj = Obj.objects.all()
    obj.delete()
    return True


def addSqlMsg(Obj, msg):
    for m in msg:
        Obj.objects.create(**m)

def changeId(Obj):
    test = TestHost.objects.all()
    count = 1
    for t in test:
        t.id = count
        t.save()
        count += 1

if __name__ == '__main__':
    msg = getSqlMsg(Host, '-stress_test', 100)
    sqlDelete(TestHost)
    addSqlMsg(TestHost, msg)
    #changeId(TestHost)
