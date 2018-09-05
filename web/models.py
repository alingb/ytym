#-*-encoding:utf-8-*-
from django.db import models

# Create your models here.
class Host(models.Model):
    id = models.AutoField(primary_key=True)
    sn = models.CharField(max_length=250)
    sn_1 = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    name1 = models.CharField(max_length=250)
    family = models.CharField(max_length=250)
    status = models.CharField(max_length=550)
    time = models.DateTimeField()
    boot_time = models.CharField(max_length=250)
    cpu = models.CharField(max_length=250)
    memory = models.CharField(max_length=250)
    disk = models.CharField(max_length=550)
    raid = models.CharField(max_length=550)
    network = models.CharField(max_length=550)
    mac = models.CharField(max_length=550)
    mac_addr = models.CharField(max_length=550)
    ip = models.CharField(max_length=550, blank=True)
    bios = models.CharField(max_length=250)
    bmc = models.CharField(max_length=250)
    sel = models.TextField()
    stress_test = models.CharField(max_length=250)
    hostname = models.CharField(max_length=250)
    disk_num = models.IntegerField()
    message = models.TextField()
    fru = models.TextField()
    smart_info = models.TextField(blank=True)
    enclosure = models.FileField('breakin', blank=True)
    class Meta:
        verbose_name_plural = u'老化测试系统'
        verbose_name = u'服务器信息'
    def __unicode__(self):
        return self.sn



#class Product(models.Model):
#    name = models.CharField(max_length=250)
#    orders = models.ManyToManyField(Host)
#    def __unicode__(self):
#        return self.name
    


class HostCheck(models.Model):
    id = models.AutoField(primary_key=True)
    sn = models.CharField(max_length=250)
    sn_1 = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    name1 = models.CharField(max_length=250)
    family = models.CharField(max_length=250)
    status = models.CharField(max_length=550)
    time = models.DateTimeField()
    boot_time = models.CharField(max_length=250)
    cpu = models.CharField(max_length=250)
    memory = models.CharField(max_length=250)
    disk = models.CharField(max_length=550)
    raid = models.CharField(max_length=550)
    network = models.CharField(max_length=550)
    mac = models.CharField(max_length=550)
    mac_addr = models.CharField(max_length=550)
    bios = models.CharField(max_length=250)
    bmc = models.CharField(max_length=250)
    sel = models.TextField()
    stress_test = models.CharField(max_length=250)
    hostname = models.CharField(max_length=250)
    disk_num = models.IntegerField()
    message = models.TextField()
    fru = models.TextField()
    smart_info = models.TextField(blank=True)
    enclosure = models.FileField(blank=True)
    class Meta:
        verbose_name_plural = u'近期服务器信息'
        verbose_name = u'服务器信息'
    def __unicode__(self):
        return self.sn



KIND_CHOICES = (
    ('run','run'),
    ('stop','stop'),
    ('poweroff','poweroff'),
    ('bmcLogClear','bmcLogClear'),
)
class Stat(models.Model):
    ip = models.GenericIPAddressField()
    sn = models.CharField(max_length=150,default='no date')
    status = models.CharField(max_length=50,choices=KIND_CHOICES,default='wait')
    cpu = models.CharField(max_length=150)
    mem = models.CharField(max_length=150)
    num = models.CharField(max_length=150)
    hostname = models.CharField(max_length=150)
    def __unicode__(self):
        return "%s(%s)" %(self.status,self.hostname)


class Group(models.Model):
    stat = models.ManyToManyField(Stat,blank=True)
    statname = models.CharField(max_length=50,unique=True,choices=KIND_CHOICES,default='wait')
    class Meta:
        verbose_name_plural = u'运行状态'
        verbose_name = u'运行'


class Info(models.Model):
    message = models.FileField(blank=True)
    url = models.URLField(blank=True)


class Smart(models.Model):
    sn = models.CharField('sn', max_length=250)
    sn_1 = models.CharField('sn_1', max_length=250)
    sel = models.TextField('BMC日志',)
    smart_info = models.TextField('数据',)
    time = models.CharField('时间', max_length=150, blank=True)
    explain = models.CharField('说明', max_length=550, blank=True)


class ChangeBiosBmc(models.Model):
    sn = models.CharField('sn', max_length=250)
    sn_1 = models.CharField('sn_1', max_length=250)
    ip = models.CharField('ip', max_length=250)
    bios = models.CharField('bios', max_length=250)
    bmc = models.CharField('bmc', max_length=250)
    name = models.CharField('name', max_length=250)
    family = models.CharField('family', max_length=250)
    #number = models.IntegerField('number')
    fru = models.CharField('fru_info', max_length=250, blank=True)
    stat = models.CharField('status', max_length=250, blank=True)
