from django.db import models
#-*-encoding:utf8-*-

# Create your models here.
BUG_CHOICES = (
    ('1', '一般'),
    ('2', '严重'),
    ('3', '非常严重'),
)
PRODUCT_CHOICES = (
    ('ASR1100', '华硕ASR1100'),
    ('K880G3', '英业达K880G3'),
    ('ASD2550', '华硕ASD2550'),
    ('RS720Q-E8', '华硕RS720Q-E8'),
    ('RS300-E9-PS4', '华硕RS300-E9-PS4'),
    ('ASR2612', '华硕ASR2612'),
    ('D51B-2U', '广达D51B-2U'),
    ('T41S-2U', '广达T41S-2U'),
    ('RS300-E9-PS4', '华硕RS300-E9-PS4'),
    ('RS520-E8-RS8', '华硕RS520-E8-RS8'),
    ('S210-X22RQ', '广达S210-X22RQ'),
    ('ESC4000G3', '华硕ESC4000G3'),
    ('RS520-E8-RS12', '华硕RS520-E8-RS12'),
    ('other', '其他'),
)
PROJECT_CHOICES = (
    ('ELOG', '锐捷ELOG'),
    ('RG-RCP', '锐捷RG-RCP'),
    ('RCD6000-Office', '锐捷RCD6000-Office'),
    ('RCD6000-Main', '锐捷RCD6000-Main'),
    ('RG-SE04', '锐捷RG-SE04'),
    ('RG-ONC-AIO-CTL', '锐捷RG-ONC-AIO-CTL'),
    ('RG-RCM1000-Office', '锐捷RG-RCM1000-Office'),
    ('RG-RCM1000-Edu', '锐捷RG-RCM1000-Edu'),
    ('RG-RCM1000-Smart', '锐捷RG-RCM1000-Smart'),
    ('MDBE', '美电贝尔'),
    ('ZJCC', '广东紫晶存储'),
    ('UDS1022-G', '锐捷UDS1022-G'),
    ('UDS1022-G1', '锐捷UDS1022-G1'),
    ('UDS2000-C', '锐捷UDS2000-C'),
    ('UDS2000-E', '锐捷UDS2000-E'),
    ('UDS2000-E1', '锐捷UDS2000-E1'),
    ('RG-CES', '锐捷RG-CES'),
    ('RG-CPV-M', '锐捷RG-CPV-M'),
    ('RG-CPV-S', '锐捷RG-CPV-S'),
    ('2513(M1)', '三盟2513(M1)'),
    ('2513(M3)', '三盟2513(M3)'),
    ('2513(VM3)', '三盟2513(VM3)'),
    ('ASERVER-2400', '深信服ASERVER-2400'),
    ('ASERVER-2405', '深信服ASERVER-2405'),
    ('VDS-5050', '深信服VDS-5050'),
    ('VDS-6550', '深信服VDS-6550'),
    ('VDS-8050', '深信服VDS-8050'),
    ('VDS-G680', '深信服VDS-G680'),
    ('other', '其他'),
)
EXCLUSION_CHOICES = (
    ('1', '处理中'),
    ('2', '已完成'),
)
CUSTOMER_CHOICES = (
    ('1', '锐捷'),
    ('2', '深信服'),
    ('3', '三盟'), 
    ('other', '其他'),

)
DISCOVERY_CHOICES = (
    ('1', '公司内部'),
    ('2', '客户'),
    ('other', '其他')
)
class Error(models.Model):
    product_name = models.CharField('产品名称', choices=PRODUCT_CHOICES, max_length=500)
    product_name_other = models.CharField('其他产品名称', max_length=500, blank=True,)
    product = models.CharField('产品名称',max_length=500 ,blank=True)
    bug_person = models.CharField('BUG负责人', max_length=500)
    project_name  = models.CharField('项目名称', choices=PROJECT_CHOICES, max_length=500)
    project_name_other = models.CharField('其他项目名称', max_length=500, blank=True)
    project = models.CharField('项目名称', max_length=500, blank=True)
    test_person = models.CharField('测试人员', max_length=500, blank=True)
    enclosure = models.FileField('附件上传', blank=True)
    email = models.CharField('抄送人员', max_length=500, blank=True)
    bug_describe = models.TextField('BUG简述', max_length=500)
    bug_level = models.CharField('BUG等级',choices=BUG_CHOICES, max_length=500)
    level = models.CharField('BUG等级', max_length=500, blank=True)
    discovery_phase = models.CharField('发现途径', choices=DISCOVERY_CHOICES, max_length=500)
    discovery_phase_other = models.CharField('其他发现途径', max_length=500, blank=True)
    discovery = models.CharField('发现途径', max_length=500, blank=True)
    exclusion_phase = models.CharField('处理阶段', choices=EXCLUSION_CHOICES, max_length=500)
    exclusion = models.CharField('处理阶段', max_length=500, blank=True)
    bug_record = models.TextField('BUG记录', blank=True)
    submission_time = models.DateTimeField('提交时间', auto_now_add=True)
    record_time = models.DateTimeField('更新时间', auto_now=True)
    time = models.CharField('更新时间', max_length=250, blank=True,)
    user = models.CharField('修改者', max_length=50, blank=True,)
    customer_name = models.CharField('客户名称', choices=CUSTOMER_CHOICES, max_length=500)
    customer_name_other = models.CharField('其他客户名称', max_length=500, blank=True)
    customer = models.CharField('客户名称', max_length=500, blank=True)
    num = models.IntegerField('bug编号',blank=True)
    status = models.BooleanField(default=False)
    phenomenon_description = models.CharField('bug现象详细描述', max_length=500)
    software_name = models.CharField('测试软件名称', max_length=500, blank=True)
    step_description = models.CharField('bug发生步骤', max_length=500)
    test_site = models.CharField('发生地点', max_length=500, blank=True)
    test_model = models.TextField('处理措施', max_length=500, blank=True)
#    test_model = models.CharField('处理措施', max_length=500, blank=True)
    configuration_information = models.CharField('配置信息', max_length=500)
    software_version = models.CharField('软件版本', max_length=500, blank=True)
    suggested_view = models.CharField('建议看法', max_length=500)
    record_update = models.TextField('记录更新', max_length=500,blank=True)
    number = models.CharField('编号', max_length=50, blank=True)
    sn = models.CharField('产品sn', max_length=250)
    class Meta:
        verbose_name = u'fault'
        verbose_name_plural = u'bugsystem'
#    def __unicode__(self):
#        return self.num


class Smart(models.Model):
    sn = models.CharField('sn', max_length=250)
    sn_1 = models.CharField('sn_1', max_length=250)
    sel = models.TextField('BMC日志', blank=True )
    smart_info = models.TextField('数据', blank=True)


