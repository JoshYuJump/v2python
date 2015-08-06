# -*- coding: utf-8 -*- 

from django.db import models

# Create your models here.

class Request(models.Model):
    req_user = models.CharField(max_length=100, verbose_name=u'请假人')
    req_depart = models.CharField(max_length=200, verbose_name=u'部门')
    req_duty = models.CharField(max_length=200, verbose_name=u'职务')

    req_type = models.CharField(max_length=200, verbose_name=u'请假类型')

    req_begin = models.DateTimeField(u'请假开始时间')
    req_end = models.DateTimeField(u'请假结束时间')

    req_reason = models.CharField(max_length=500, verbose_name=u'请假事由')
    req_contact = models.CharField(max_length=200, verbose_name=u'请假期间联系方式')
    req_client = models.CharField(max_length=200, verbose_name=u'请假期间工作委托人')

    def __unicode__(self):
        return self.req_user