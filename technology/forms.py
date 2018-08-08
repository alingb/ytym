#encoding:utf-8
from django.forms import ModelForm
from technology.models import Error
from django import forms

class ErrorForm(ModelForm):
    class Meta:
        model = Error
        fields = '__all__'
        widgets = {
            'bug_describe': forms.Textarea(attrs={'cols': 50, 'rows': 2, 'placeholder': '错误描述'}),
            'product_name_other': forms.TextInput(attrs={'placeholder': '其他产品名称'}),
            'project_name_other': forms.TextInput(attrs={'placeholder': '其他项目名称'}),
            'discovery_phase_other': forms.TextInput(attrs={'placeholder': '其他发现途径'}),
            'customer_name_other': forms.TextInput(attrs={'placeholder': '其他客户名称'}),
            'phenomenon_description': forms.Textarea(attrs={'cols': 90, 'rows': 3}),
            'software_name': forms.Textarea(attrs={'cols': 90, 'rows': 1}),
            'step_description': forms.Textarea(attrs={'cols': 90, 'rows': 3}),
            'test_site': forms.Textarea(attrs={'cols': 90, 'rows': 3}),
            'test_model': forms.Textarea(attrs={'cols': 90, 'rows': 3}),
            'configuration_information': forms.Textarea(attrs={'cols': 90, 'rows': 3}),
            'software_version': forms.Textarea(attrs={'cols': 90, 'rows': 3}),
            'suggested_view': forms.Textarea(attrs={'cols': 90, 'rows': 3}),
                 } 
