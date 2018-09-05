from django.shortcuts import render

# Create your views here.
import json
from web.models import *
from django.http import HttpResponse
from web.forms import AddForm
from web.forms import Update
import os
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
import time
from django.core.files import File

def collect(req):
    if req.POST:
        info = json.loads(req.body)
        sn = info['sn']
        sn_1 = info['sn_1']
        try:
            host = Host.objects.get(sn=sn, sn_1=sn_1)
        except:
            host = Host()
        host.sn = info['sn']
        host.sn_1 = info['sn_1']
        host.status = info['status']
        host.time = info['time']
        host.boot_time = info['boot_time']
        host.name = info['name']
        host.name1 = info['name1']
        host.family = info['family']
        host.cpu = info['cpu']
        host.memory = info['memory']
        host.disk = info['disk']
        host.disk_num = info['disk_num']
        host.hostname = info['hostname']
        host.stress_test = info['stress_test']
        host.network = info['network']
        host.mac = info['mac']
        host.mac_addr = info['mac_addr']
        host.raid = info['raid']
        host.bios = info['bios']
        host.bmc = info['bmc']
        host.message = info['message']
        host.sel = info['sel']
        host.fru = info['fru']
        host.ip = info['ip']
        host.smart_info = info['smart_info']
        try:
            host.enclosure = File(info['enclosure'])
        except:
            pass
        host.save()
        return HttpResponse('ok')
    else:
        form = Host.objects.all()
        PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return render(req, os.path.join(PROJECT_ROOT, 'web/templates', 'collect.html'), {'form':form})

def info(req):
    if req.POST:
        info = json.loads(req.body)
        data = Info()
        data.message = info['message']
        data.save()
    return HttpResponse('ok')
        
def form(req):
    if req.POST:
        info = json.loads(req.body)
        sn = info['sn']
        ip = info['ip']
        try:
            stat = Stat.objects.get(ip=ip)
        except:
            stat = Stat()
        stat.status = info['status']
        stat.ip = info['ip']
        stat.sn = info['sn']
        stat.cpu = info['cpu']
        stat.mem = info['mem']
        stat.hostname = info['hostname']
        stat.save()
        return HttpResponse('ok')
    else:
        if not req.user.username:
            return HttpResponseRedirect('/login/')
        form = Stat.objects.all()
        count = form.count()
        form = form.order_by('-status', 'hostname')
        a = 1
        for i in form:
            b = i 
            b.num = a
            a += 1
            b.save()
        num = []
        for i in form:
              if 'OS off' in i.status:
                  num.append(i.status[:-6])
              else:
                  num.append(i.status)
        dic = {}
        data = set(num)
        for i in data:
            dic[i] = num.count(i)
        strs = ""
        for k,v in dic.items():
            strs += '--"%s"(%s)--' %(k,v) 
        PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return render(req, os.path.join(PROJECT_ROOT, 'web/templates', 'status.html'), {'form':form,'count':count,'dic':strs})

def form_page(request):
    page_dic = {'page_content':None, 'page_count':None}

    if request.method == 'POST':
        page_num = request.POST.get('page', None)
        data_count = request.POST.get('count', None)
        print(page_num,data_count)
        # pagesplit_obj=pagesplit.Pager(page_num)
        page_end = int(page_num) * int(data_count)
        page_start = page_end - int(data_count)
        query_obj = Host.objects.all()[page_start:page_end]
        page_count = Host.objects.count()
        page_cont_str=''
        for i in query_obj:
            page_cont_str+='''
            <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td><a href="/res_query_check/%s"></a></td> </tr>
            '''%(i.id, i.task_name, i.task_user, i.id)
        page_dic['page_content']=page_cont_str
        page_dic['page_count']=page_count
        return  HttpResponse(json.dumps(page_dic))
    elif request.method=='GET':
        page_count = Host.objects.count()
        x,y=divmod(page_count,12)
        if y:
            page_num=x+1
        else:
            page_num=x
        return render(request,'page.html',{'pagecount':page_num})

def change_bios_bmc(req):
    def sshConn(ip, cmd):
        import paramiko
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(ip,22,'root','admin123',timeout=1)        
        except:
            return False
        stdin, stdout, stderr = ssh.exec_command(cmd)
        data = stdout.read()
        ssh.close()
        return data
        

    def dataDelete():
        obj_ip = ChangeBiosBmc.objects.all().values('ip')
        for obj in obj_ip:
            key, ip = obj.items()[0]
            cmd = 'ps aux | grep "ls" | wc -l'
            num = sshConn(ip, cmd)
            if num < 5:
                ChangeBiosBmc.objects.filter(ip=ip).delete()
            

    def dataCreate(sn, sn_1):
        host_msg = Host.objects.filter(sn=sn,sn_1=sn_1).values("sn", "sn_1", 
                                                               "ip", "bios", 
                                                               "bmc", "name", 
                                                               "family", "fru")[0]
        try:
            ChangeBiosBmc.objects.get(sn=sn,sn_1=sn_1)
        except:
            ChangeBiosBmc.objects.create(**host_msg)

    if req.POST:
        data = req.POST.getlist('msg', '')
        bmc = req.POST.get('bmcversion')
        bios = req.POST.get('biosversion')
        filedata = req.FILES.get('filename')
        erro_msg, stat = [], []
        dataDelete()
        for i in data:
            msg_list = i.split(',')
            sn = msg_list[0]
            sn_1 = msg_list[1]
            ip = msg_list[2]
            dataCreate(sn, sn_1)
            cmd = 'ps aux | egrep "cpu" | grep -v grep | wc -l'
            data = sshConn(ip, cmd)
            if data:
                if data > 1:
                    stat.append('The program is running')
                else:
                    cmd = 'ls'
                    sshConn(ip, cmd)
            else:
                erro_msg.append('conn erro')
    return HttpResponseRedirect('/change_status')


def change_status(req):
    import paramiko
    change_msg = ChangeBiosBmc.objects.all().values_list('sn',"sn_1")
    for sn,sn_1 in change_msg:
        host_msg = Host.objects.filter(sn=sn,sn_1=sn_1).values("ip", "bios", "bmc", "name", "family", "fru")[0]
        ChangeBiosBmc.objects.filter(sn=sn,sn_1=sn_1).update(**host_msg)
    msgs = ChangeBiosBmc.objects.all()
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for msg in msgs:
        conn_ip = msg.ip
        try:
            ssh.connect(conn_ip,22,'root','admin123',timeout=1)
        except:
            msg.stat = 'error'
            msg.save()
            continue
        stdin, stdout, stderr = ssh.exec_command('ps aux | grep ls | wc -l')
        number = int(stdout.read())
        if number > 10:
            msg.stat = 'running...'
            msg.save()
            continue
        else:
            msg.stat = 'complete'
            msg.save()
        ssh.close()
    form = ChangeBiosBmc.objects.all()
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return render(req, os.path.join(PROJECT_ROOT, 'web/templates', 'test.html'),{'form':form})


def index(req):
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return render(req, os.path.join(PROJECT_ROOT, 'web/templates', 'index.html'),)
                                                              
def smart(req):
    if req.POST:
        info = json.loads(req.body)
        sn = info['sn']
        try:
            smart = Smart.objects.get(sn=sn)
        except:
            smart = Smart()
        smart.sn = info['sn']
        smart.sn_1 = info['sn_1']
        smart.sel = info['sel']
        smart.time = info['time']
        smart.explain = info['explain']
        smart.smart_info = info['smart_info']
        smart.save()
        return HttpResponse('ok')
    else:
        form = Smart.objects.all()
#        PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#        return render(req, os.path.join(PROJECT_ROOT, 'web/templates', 'smart.html'), {'form':form})
        return HttpResponse(form)

def product(req, productName):
    prot = Product.objects.get(name=productName)
    orders = prot.orders.all()
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return render(req, os.path.join(PROJECT_ROOT, 'web/templates', 'product.html'), {'name':productName, 'orders':orders})

def productCollect(req):
    from django.core.exceptions import MultipleObjectsReturned
    msg = []
    try:
        if req.POST:
            info = json.loads(req.body)
            prot = Product.objects.get_or_create(name=info["name"])[0]
	    for sn in info["sn_list"]:
                try:
 	            host = Host.objects.get(sn=sn)
        	    prot.orders.add(host)
                except:
                    msg.append("sn:{} no foud\n".format(sn))
                    try:
                        host = Host.objects.get(sn_1=sn)
        	        prot.orders.add(host)
                    except:
                        msg.append("sn_1:{} no foud\n".format(sn))
    except Exception as e:
    	return HttpResponse("no")
    return HttpResponse(msg)


def usename(req, table, id, mang):
    if table == 'Host':
        form = Host.objects.get(id=id)
    elif table == 'HostCheck':
        form = HostCheck.objects.get(id=id)
    message = form.message    
    dic = {}
    import re
    ALL_LIST = []
    for i in message.split('\n'):
        re_info = re.findall(r'(^[A-Z]{1,8}[\s_]*[A-Z1-9]*):', i, re.M)
        if re_info:
            ALL_LIST.append(re_info[0])
    for i in xrange(len(ALL_LIST)):
        try:
            info = message.split(ALL_LIST[i+1])[0].strip()
            split_info = ALL_LIST[i] +  ':'
            try:
                data = info.split(split_info)[1].strip()
            except:
                data = ''
           # if ALL_LIST[i] == 'NAME' or ALL_LIST[i] == 'FIMILY':
           #     dic[ALL_LIST[i].replace(' ', '_')] = '' + data.strip()
           # else:
            dic[ALL_LIST[i].replace(' ', '_')] = data.strip()
        except:
            info = message.split(ALL_LIST[i])[0]
            dic[ALL_LIST[i].replace(' ', '_')] = info.split(':')[1]
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if mang:
        return render(req, os.path.join(PROJECT_ROOT, 'web/templates', '{}.html'.format(mang)), {'form':dic,'all':form})
    else:
        return render(req, os.path.join(PROJECT_ROOT, 'web/templates', 'detail.html'), {'form':dic,'all':form})


def checkStat(req):
    if req.POST: 
        info = req.POST
        if info['check'] == 'run':
            return HttpResponse('run')
        if info['check'] == 'stop':
            return HttpResponse('stop')
    else:
        return HttpResponse('else')

def smartid(req, id):
    form = Smart.objects.get(id=id)
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return render(req, os.path.join(PROJECT_ROOT, 'web/templates', 'smart.html'), {'form':form})

#def change_bios_bmc(req):
#    form = Host.objects.get(id='1000')
#    message = form.message
#    dic = {}
#    import re
#    ALL_LIST = []
#    for i in message.split('\n'):
#        re_info = re.findall(r'(^[A-Z]{1,8}[\s_]*[A-Z1-9]*):', i, re.M)
#        if re_info:
#            ALL_LIST.append(re_info[0])
#    for i in xrange(len(ALL_LIST)):
#        try:
#            info = message.split(ALL_LIST[i+1])[0]
#            split_info = ALL_LIST[i] +  ':'
#            try:
#                data = info.split(split_info)[1]
#            except:
#                data = ''
#            if ALL_LIST[i] == 'NAME' or ALL_LIST[i] == 'FIMILY':
#                dic[ALL_LIST[i].replace(' ', '_')] = '\t' + data.strip()
#                dic[ALL_LIST[i].replace(' ', '_')] = '\t' + data.strip()
#            else:
#                dic[ALL_LIST[i].replace(' ', '_')] = data
#        except:
#            info = message.split(ALL_LIST[i])[0]
#            dic[ALL_LIST[i].replace(' ', '_')] = info.split(':')[1]
#                data = info.split(split_info)[1]
#            except:
#                data = ''
#            if ALL_LIST[i] == 'NAME' or ALL_LIST[i] == 'FIMILY':
#                dic[ALL_LIST[i].replace(' ', '_')] = '\t' + data.strip()
#                dic[ALL_LIST[i].replace(' ', '_')] = '\t' + data.strip()
#            else:
#                dic[ALL_LIST[i].replace(' ', '_')] = data
#        except:
#            info = message.split(ALL_LIST[i])[0]
#            dic[ALL_LIST[i].replace(' ', '_')] = info.split(':')[1]
#    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#    return render(req, os.path.join(PROJECT_ROOT, 'web/templates', 'change_bios_bmc.html'),  {'form':dic,'all':form})

def test(req):
    msg = []
    rt = {'erro':None}
    try:
        import paramiko
        post_info = req.POST
        power_time = req.POST.get('power')
        time = int(power_time) * 60
        cmd = 'nohup shutdown -c --no-wall && shutdown -h +%s --no-wall &>/root/shutdown.time &' % time
        for k, v in post_info.items():
            ret = {}
            if 'ip' in k:
                ip = v
                try:
                    ssh = paramiko.SSHClient()
                    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    ssh.connect(ip,22,'root','admin123',timeout=5)
                    stdin, stdout, stderr = ssh.exec_command(cmd)
                    ret['ip'] = ip 
                    ret['status'] = 'successed'
                    ret['time']  = power_time + 'H'
                    ssh.close()
                    msg.append(ret)
                except:
                    ret['ip'] = ip 
                    ret['status'] = 'unsuccessed'
                    ret['time']  = power_time + 'H'
                    msg.append(ret)
    except Exception as e:
        rt['erro'] = e
        ret['status'] = 'unsuccessed'
        ret['time']  = power_time + 'H'
        msg.append(ret)
    finally:
        PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return render(req, os.path.join(PROJECT_ROOT, 'web/templates', 'run.html'), {'ret':msg,'rt':rt})
