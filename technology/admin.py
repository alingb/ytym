#coding:utf-8
from django.http import HttpResponse
from django.http import StreamingHttpResponse
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe
from django.conf.urls import patterns
from django.contrib import admin
from django.forms import ModelForm
from django import forms
from technology.models import *
import datetime
import time
import sys
import xlwt
import MySQLdb

reload(sys)
sys.setdefaultencoding('utf8')


USER = {'daipeibin':u'戴沛斌',
        'huangjiaqi':u'黄嘉琪',
        'jinanning':u'金安宁',
        'laiwenlong':u'赖文龙',
        'lichao':u'李超',
        'liming':u'李铭',
        'maimaotao':u'麦茂涛',
        'wangqiang':u'王强',
        'xieliye':u'谢立业',
        'zhengcongke':u'郑淙珂',
        'zhongyangchun':u'仲扬春',
        'linliubin':u'林柳彬',
        'lingbing':u'凌兵',}
EXCLUSION = {'1':'处理中',
                     '2':'已完成'}

# Register your models here.
def save_errors(self, request, queryset):
  def export(host,user,password,dbname,table_name,outputpath,num):
      conn = MySQLdb.connect(host,user,password,dbname,charset='utf8')
      cursor = conn.cursor()
      count = cursor.execute('select num,product,bug_person,project,bug_describe,discovery,bug_record,submission_time,time,user,customer,test_site,test_model,number,sn,level,exclusion from %s where %s'%(table_name, num))
#      count = cursor.execute('select num,product,project,bug_person,test_site,bug_level,exclusion_phase,customer,discovery,sn,bug_describe,bug_record,submission_time,time,user,customer,status,test_site,test_model,number,sn from %s where %s'%(table_name, num))
      # 重置游标的位置
      cursor.scroll(0,mode='absolute')
      # 搜取所有结果
      global results
      results = cursor.fetchall()
  
      # 获取MYSQL里面的数据字段名称
      fields = {'0':u'Bug编号',
                '1':u'产品名称',
                '2':u'BUG负责人',
                '3':u'项目名称',
                '4':u'BUG简述',
                '5':u'发现途径',
                '6':u'BUG记录',
                '7':u'提交时间',
                '8':u'更新时间',
                '9':u'修改者',
                '10':u'客户名称',
#                '11':u'状态',
                '11':u'发生地点',
                '12':u'处理措施',
                '13':u'编号',
                '14':u'SN',
                '15':u'BUG等级',
                '16':u'处理阶段',}
      workbook = xlwt.Workbook()
      sheet = workbook.add_sheet('table_' + table_name,cell_overwrite_ok=True)
  
      # 写上字段信息
      for field in range(0,len(fields)):
          sheet.write(0,field,fields['%s'%field])
  
      # 获取并写入数据段信息
      row = 1
      col = 0
      for row in range(1,len(results)+1):
          for col in range(0,len(fields)):
              sheet.write(row,col,u'%s'%results[row-1][col])
  
      workbook.save(outputpath)
  
  def file_iterator(file_name, chunk_size=512):
    with open(file_name) as f:
      while True:
        c = f.read(chunk_size)
        if c:
          yield c
        else:
          break
  num_count = ''
  for q in queryset:
      num_count += 'num="%s" or '% q.num
  if num_count:
      num_count = num_count[:-3]

  export('192.168.6.120', 'trusme', '6286280300', 'cmdb', 'technology_error', r'/data/media/bugsystem.xls', num_count)
  the_file_name = "/data/media/bugsystem.xls"
  response = StreamingHttpResponse(file_iterator(the_file_name))
  response['Content-Type'] = 'application/octet-stream'
  response['Content-Disposition'] = 'attachment;filename="{0}"'.format('bugsystem.xls')
  self.message_user(request, "%s haved download"% len(results))
  return response
save_errors.short_description = "download"

#class ErrorAdminForm(forms.ModelForm):
#    class Meta:
#        model = Error
#        fields = '__all__'
#        widgets = {
#                   'test_model':forms.Textarea(attrs={'cols': 90, 'rows': 3}),
#                  }

class ErrorAdmin(admin.ModelAdmin):
    actions = [save_errors, ]
    list_display = [ 
                    'number',
                    'num',
                    'bug_describe',
                    'project',
                    'bug_person',
                    'bug_level',
                    'exclusion_phase',
                    'discovery',
                    'submission_time',
#                    'record_time',
                    'time',
                    'customer',
                    'user',
                    'enclosure',
                    'status',
                    ]
    search_fields = ('num', 
                     'sn',
                     'bug_describe', 
                     'product', 
                     'project', 
                     'bug_person', 
                     'exclusion_phase', 
                     'discovery', 
                     'customer', 
                     'user', 
                     'status',)
    list_filter = ('product', 
                   'project', 
                   'bug_person', 
                   'exclusion_phase', 
                   'discovery', 
                   'customer', 
                   'user', 
                   'status', 
                   'submission_time',)
    date_hierarchy = 'submission_time'
    list_display_links = ('num',)
    list_per_page = 30
    readonly_fields = ('address_report',)
    actions_on_top = True

    def address_report(self, obj):
        return format_html_join(
            mark_safe('<br/>'),
            '{}',
            ((line,) for line in obj.test_model.split('\n')),
        ) or mark_safe("<span class='errors'>I can't determine this address.</span>")

    address_report.short_description = "Address"

#    def save_model(self, request, obj, form, change):
#        obj.user = request.user.username
#        obj.save()
    
    def changelist_view(self, request, extra_context=None):
        user = request.user
        if user.groups.values():
            group = user.groups.values()[0]['name']
        else:
            group = ''
        if user.is_superuser:
            self.readonly_fields = ("user",'num',)
        elif group == 'technology':
            self.fields = ('num', 
                          ('product','project'),
                          ('bug_person','test_site'),
                          ('bug_level','exclusion_phase'),
                          ('discovery','customer'), 
                          ('enclosure', 'sn'), 
                          'bug_describe', 
                          'bug_record', 
                          'test_model', 
                          'record_update')
            self.readonly_fields = ("user",
                                    'num', 
                                    'product', 
                                    'project', 
                                    'bug_person', 
                                    'test_site', 
                                    'bug_level', 
                                    'discovery', 
                                    'customer', 
                                    'sn', 
                                    'bug_describe',)
        else:
            self.fields = ('num', 
                           ('product','project'),
                           ('bug_person','test_site'),
                           ('bug_level','exclusion_phase'),
                           ('discovery','customer'), 
                           ('enclosure', 'sn'), 
                           'bug_describe', 
                           'test_model', 
                           'bug_record', 
                           'record_update')
            self.readonly_fields = ("user",
                                    'num', 
                                    'product', 
                                    'project', 
                                    'bug_person', 
                                    'test_site', 
                                    'bug_level', 
                                    'discovery', 
                                    'customer', 
                                    'sn', 
                                    'bug_describe', )
#            self.fields = (('num', 'sn'),('product','project'),('bug_person','test_site'),('bug_level','exclusion_phase'),('discovery','customer'),'bug_describe','bug_record', 'record_update')
  #          self.fields = ('num',('product','project'),('bug_person','test_model'),('software_name','bug_person'),('bug_level','exclusion_phase'),('discovery','customer'),('test_site','software_version'),'bug_describe','bug_record', 'record_update')
        return super(ErrorAdmin, self).changelist_view(request, extra_context=None)

    def save_model(self, request, obj, form, change):
#        USER = {'daipeibin':u'戴沛斌',
#                'huangjiaqi':u'黄嘉琪',
#                'jinanning':u'金安宁',
#                'laiwenlong':u'赖文龙',
#                'lichao':u'李超',
#                'liming':u'李铭',
#                'maimaotao':u'麦茂涛',
#                'wangqiang':u'王强',
#                'xieliye':u'谢立业',
#                'zhengcongke':u'郑淙珂',
#                'zhongyangchun':u'仲扬春',
#                'linliubin':u'林柳彬',
#                'lingbing':u'凌兵',}
#        EXCLUSION = {'1':'处理中',
#                     '2':'已完成'}
        if change:
            obj_old = self.model.objects.get(pk=obj.pk)
        else:
            obj_old = None
        obj.user = request.user
        if obj.user.groups.values():
            group = obj.user.groups.values()[0]['name']
        else:
            group = ''
        if request.user.is_superuser:
            obj.user = request.user.username
            try:
                obj.user = USER[obj.user]
            except:
                pass
            obj.time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            obj.exclusion = EXCLUSION[obj.exclusion_phase]
            if obj.exclusion_phase == '1':
                obj.status = False
            elif obj.exclusion_phase == '2':
                obj.status = True
            obj.save()
        if group == 'technology':
            obj.user = request.user.username
            try:
                obj.user = USER[obj.user]
            except:
                pass
            obj.time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            obj.exclusion = EXCLUSION[obj.exclusion_phase]
            if obj.exclusion_phase == '1':
                obj.status = False
            elif obj.exclusion_phase == '2':
                obj.status = True
            if obj.record_update:
                obj.test_model = obj_old.test_model
                obj.bug_record = '%s\n====================\n%s\n(%s,%s)'% (obj_old.bug_record, obj.record_update, obj.user, datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S'))
                obj.record_update = ''
           # else:
           #     obj.bug_record = obj_old.bug_record
           #     obj.test_model = obj_old.test_model
            obj.save()

#class SmartAdmin(admin.ModelAdmin):
#    list_display = [
#                    'sn',
#                    'sn_1',
#                    'data',
#                    ]
#    search_fields = ('sn', 'sn_1',  )
#    list_filter = ('sn', 'sn_1', )
#
class FaeErrorAdmin(admin.ModelAdmin):
    list_display = [
                    'number',
                    'num',
                    'product',
                   # 'exclusion_phase',
                    'bug_describe',
                    #'phenomenon_description',
                    'submission_time',
                    'time',
                    'customer',
                    'user',
                    'enclosure',
                    'status',
                    ]
    search_fields = ('num',
                     'sn',
                     'product',
                     'exclusion_phase',
                     'customer',
                     'user',
                     'status',)
    list_filter = ('product',
                   'exclusion_phase',
                   'customer',
                   'user',
                   'status',
                   'submission_time',)
    date_hierarchy = 'submission_time'
    list_display_links = ('num',)
    list_per_page = 30
    readonly_fields = ('address_report',)
    actions_on_top = True

    def address_report(self, obj):
        return format_html_join(
            mark_safe('<br/>'),
            '{}',
            ((line,) for line in obj.resolvent.split('\n')),
        ) or mark_safe("<span class='errors'>I can't determine this address.</span>")

    address_report.short_description = "Address"

#    def save_model(self, request, obj, form, change):
#        obj.user = request.user.username
#        obj.save()

    def changelist_view(self, request, extra_context=None):
        user = request.user
        if user.groups.values():
            group = user.groups.values()[0]['name']
        else:
            group = ''
        if user.is_superuser:
            self.readonly_fields = ("user",'num',)
        elif group == 'technology':
            self.fields = ('num',
                          ('product'),
                          ('exclusion_phase'),
                          ('customer'),
                          ('enclosure', 'sn'),
                          'bug_describe',
                          'bug_record',
                          #'resolvent',
                          'record_update')
            self.readonly_fields = ("user",
                                    'num',
                                    'product',
                                    'customer',
                                    'sn',
                                    'bug_describe',)
        else:
            self.fields = ('num',
                          ('product'),
                          ('exclusion_phase'),
                          ('customer'),
                          ('enclosure', 'sn'),
                          'bug_record',
                          'bug_describe',
                          #'resolvent',
                          'record_update')
            self.readonly_fields = ("user",
                                    'num',
                                    'product',
                                    'customer',
                                    'sn',
                                    'bug_describe',)
        return super(FaeErrorAdmin, self).changelist_view(request, extra_context=None)

    def save_model(self, request, obj, form, change):
#        USER = {'daipeibin': u'戴沛斌',
#                'huangjiaqi': u'黄嘉琪',
#                'jinanning': u'金安宁',
#                'laiwenlong': u'赖文龙',
#                'lichao': u'李超',
#                'liming': u'李铭',
#                'maimaotao': u'麦茂涛',
#                'wangqiang': u'王强',
#                'xieliye': u'谢立业',
#                'zhengcongke': u'郑淙珂',
#                'zhongyangchun': u'仲扬春',
#                'linliubin': u'林柳彬',
#                'lingbing': u'凌兵', }
#        EXCLUSION = {'1': '处理中',
#                     '2': '已完成'}
        if change:
            obj_old = self.model.objects.get(pk=obj.pk)
        else:
            obj_old = None
        obj.user = request.user
        if obj.user.groups.values():
            group = obj.user.groups.values()[0]['name']
        else:
            group = ''
        if request.user.is_superuser:
            obj.user = request.user.username
            try:
                obj.user = USER[obj.user]
            except:
                pass
            obj.time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            obj.exclusion = EXCLUSION[obj.exclusion_phase]
            if obj.exclusion_phase == '1':
                obj.status = False
            elif obj.exclusion_phase == '2':
                obj.status = True
            obj.save()
        if group == 'technology':
            obj.user = request.user.username
            try:
                obj.user = USER[obj.user]
            except:
                pass
            obj.time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            obj.exclusion = EXCLUSION[obj.exclusion_phase]
            if obj.exclusion_phase == '1':
                obj.status = False
            elif obj.exclusion_phase == '2':
                obj.status = True
            if obj.record_update:
                obj.resolvent = obj_old.resolvent
                obj.bug_record = '%s\n====================\n%s\n(%s,%s)'% (obj_old.bug_record, obj.record_update, obj.user, datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S'))
                obj.record_update = ''
           # else:
           #     obj.bug_record = obj_old.bug_record
           #     obj.resolvent = obj_old.resolvent
            obj.save() 

admin.site.register(Error,ErrorAdmin)
admin.site.register(FaeError,FaeErrorAdmin)
#admin.site.register(Smart,SmartAdmin)
