#-*-encoding:utf-8-*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from technology.forms import ErrorForm
from technology.models import Error
from technology.models import *
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
import random
import os
import time


# Create your views here.
@login_required
def erro(req):
    EXCLUSION = {'1':'处理中',
                 '2':'已完成'}
    BUG = {'1':'一般',
           '2':'严重',
           '3':'非常严重',}
    CUSTOMER = {'1':'锐捷',
                '2':'深信服',
                '3':'三盟',} 
    DISCOVERY = {'1':'公司内部',
                 '2':'客户',}
    PROJECT = {
    'ELOG': '锐捷ELOG',
    'RG-RCP': '锐捷RG-RCP',
    'RCD6000-Office': '锐捷RCD6000-Office',
    'RCD6000-Main': '锐捷RCD6000-Main',
    'RG-SE04': '锐捷RG-SE04',
    'RG-ONC-AIO-CTL': '锐捷RG-ONC-AIO-CTL',
    'RG-RCM1000-Office': '锐捷RG-RCM1000-Office',
    'RG-RCM1000-Edu': '锐捷RG-RCM1000-Edu',
    'RG-RCM1000-Smart': '锐捷RG-RCM1000-Smart',
    'MDBE': '美电贝尔',
    'ZJCC': '广东紫晶存储',
    'UDS1022-G': '锐捷UDS1022-G',
    'UDS1022-G1': '锐捷UDS1022-G1',
    'UDS2000-C': '锐捷UDS2000-C',
    'UDS2000-E': '锐捷UDS2000-E',
    'UDS2000-E1': '锐捷UDS2000-E1',
    'RG-CES': '锐捷RG-CES',
    'RG-CPV-M': '锐捷RG-CPV-M',
    'RG-CPV-S': '锐捷RG-CPV-S',
    '2513(M1)': '三盟2513(M1)',
    '2513(M3)': '三盟2513(M3)',
    '2513(VM3)': '三盟2513(VM3)',
    'ASERVER-2400': '深信服ASERVER-2400',
    'ASERVER-2405': '深信服ASERVER-2405',
    'VDS-5050': '深信服VDS-5050',
    'VDS-6550': '深信服VDS-6550',
    'VDS-8050': '深信服VDS-8050',
    'VDS-G680': '深信服VDS-G680',}
    PRODUCT = {
    'ASR1100': '华硕ASR1100',
    'K880G3': '英业达K880G3',
    'ASD2550': '华硕ASD2550',
    'RS720Q-E8': '华硕RS720Q-E8',
    'RS300-E9-PS4': '华硕RS300-E9-PS4',
    'ASR2612': '华硕ASR2612',
    'D51B-2U': '广达D51B-2U',
    'T41S-2U': '广达T41S-2U',
    'RS300-E9-PS4': '华硕RS300-E9-PS4',
    'RS520-E8-RS8': '华硕RS520-E8-RS8',
    'S210-X22RQ': '广达S210-X22RQ',
    'ESC4000G3': '华硕ESC4000G3',
    'RS520-E8-RS12': '华硕RS520-E8-RS12',}
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
    if not req.user.username:
        return HttpResponseRedirect('/login/')
    user = req.user.username
    username = req.session.get('username', '')
    number = random.randint(100000,999999)
    try:
        num_exist = Error.objects.get(num=number).num 
    except:
        num_exist = ''
    while number == num_exist:
        number = random.randint(100000,999999)
    if req.POST:
        form = ErrorForm(req.POST, req.FILES)
        if  form.is_valid():
            error = Error()
            discovery = form.cleaned_data['discovery_phase']
            customer = form.cleaned_data['customer_name']
            product = form.cleaned_data['product_name']
            project = form.cleaned_data['project_name']
            if discovery == 'other':
                error.discovery = form.cleaned_data['discovery_phase_other']
            else:
                error.discovery = DISCOVERY[discovery]
            if customer == 'other':
                error.customer = form.cleaned_data['customer_name_other']
            else:
                error.customer = CUSTOMER[customer]
            if product == 'other':
                error.product = form.cleaned_data['product_name_other']
            else:
                error.product = PRODUCT[product]
            if project == 'other':
                error.project  = form.cleaned_data['project_name_other']
            else:
                error.project  = PROJECT[project]
            if form.cleaned_data['discovery_phase_other']:
                error.discovery_phase_other = form.cleaned_data['discovery_phase_other']
            if form.cleaned_data['customer_name_other']:
                error.customer_name_other = form.cleaned_data['customer_name_other']
            if form.cleaned_data['product_name_other']:
                error.product_name_other = form.cleaned_data['product_name_other']
            if form.cleaned_data['project_name_other']:
                error.project_name_other  = form.cleaned_data['project_name_other']
            error.customer_name = form.cleaned_data['customer_name']
            error.product_name = form.cleaned_data['product_name']
            error.project_name  = form.cleaned_data['project_name']          
            error.discovery_phase = form.cleaned_data['discovery_phase']
            error.bug_person = form.cleaned_data['bug_person']
            error.test_person = form.cleaned_data['test_person']
            error.enclosure = form.cleaned_data['enclosure']
            error.email = form.cleaned_data['email']
            error.sn = form.cleaned_data['sn']
            error.bug_describe = form.cleaned_data['bug_describe']
            error.bug_level = form.cleaned_data['bug_level']
            error.level = BUG[form.cleaned_data['bug_level']]
            error.exclusion_phase = form.cleaned_data['exclusion_phase']
            error.exclusion = EXCLUSION[form.cleaned_data['exclusion_phase']]
            error.num = form.cleaned_data['num']
            error.phenomenon_description = form.cleaned_data['phenomenon_description']
            error.software_name = form.cleaned_data['software_name']
            error.step_description = form.cleaned_data['step_description']
            error.test_site = form.cleaned_data['test_site']
            error.test_model = form.cleaned_data['test_model']
            error.configuration_information = form.cleaned_data['configuration_information']
            error.software_version = form.cleaned_data['software_version']
            error.suggested_view = form.cleaned_data['suggested_view']
            error.time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            if username:
                try:
                    error.user = USER[username]
                except:
                    error.user = username
            else:
                try:
                    error.user = USER[user]
                except:
                    error.user = user
            if form.cleaned_data['exclusion_phase'] == '2':
                error.status = True
#            information = u'''bug现象描述:%s
#测试软件名称:%s
#bug产生步骤描述:%s
#测试地点:%s
#配置信息:%s
#软件版本:%s
#处理方式:%s
#建议看法:%s''' % (error.phenomenon_description, error.software_name, error.step_description, error.test_site, error.configuration_information, error.software_version, error.test_model, error.suggested_view)
            list_phenomenon_description = ''
            list_step_description = ''
            list_configuration_information = ''
            list_suggested_view = ''
            if "\r\n" in error.phenomenon_description:
                for i in error.phenomenon_description.split('\r\n'):
                    list_phenomenon_description += i + '\r\n\t\t\t    '
                error.phenomenon_description = list_phenomenon_description.strip()
            if "\r\n" in error.step_description:
                for i in error.step_description.split('\r\n'):
                    list_step_description += i + '\r\n\t\t\t    '
                error.step_description = list_step_description.strip()
            if "\r\n" in error.configuration_information:
                for i in error.configuration_information.split('\r\n'):
                    list_configuration_information += i + '\r\n\t\t'
                error.configuration_information = list_configuration_information.strip()
            if "\r\n" in error.suggested_view:
                for i in error.suggested_view.split('\r\n'):
                    list_suggested_view += i + '\r\n\t\t'
                error.suggested_view = list_suggested_view.strip()
            information = u'''bug现象详细描述:%s
%s
bug产生步骤描述:%s
%s
配置信息:%s
%s
建议看法:%s''' % (error.phenomenon_description,'='*20, error.step_description,'='*20,error.configuration_information,'='*20,error.suggested_view)
            error.bug_record = information
            error.save()
            data = Error.objects.all()
            total_num = data.count()
            for i in data:
                i.number = total_num
                total_num -= 1
                i.save()       
            return HttpResponseRedirect('/technology/technology/error/')
    else:
        form = ErrorForm()
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return render(req, os.path.join(PROJECT_ROOT, 'technology/templates', 'erro.html'), {'form':form,'num':number,'user':user})


def alogin(request):
    errors= []
    account=None
    password=None
    if request.method == 'POST' :
        if not request.POST.get('account'):
            errors.append('Please Enter account')
        else:
            account = request.POST.get('account')
        if not request.POST.get('password'):
            errors.append('Please Enter password')
        else:
            password= request.POST.get('password')
        if account is not None and password is not None:
            user = auth.authenticate(username=account, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    request.session['username'] = account
                    return HttpResponseRedirect('/')
                else:
                    errors.append('disabled account')
            else:
                errors.append('invaild user')
    return render_to_response('login.html', {'errors': errors})

def logout(req):
    try:
        del req.session['username']
    except KeyError:
        pass
    return HttpResponseRedirect('/login/')


def smart(req):
    if req.POST:
        info = json.loads(req.body)
        return HttpResponse(info)
        try:
            smart = Smart.objects.get(sn=sn)
        except:
            smart = Smart()
        smart.sn = info['sn']
        smart.sn_1 = info['sn_1']
        smart.sel = info['sel']
        smart.smart_info = info['smart_info']
        smart.save()
        return HttpResponse('ok')
    else:
        form = Smart.objects.all()
#        PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#        return render(req, os.path.join(PROJECT_ROOT, 'web/templates', 'smart.html'), {'form':form})
        return HttpResponse(form)

