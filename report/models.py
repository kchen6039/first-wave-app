# Create your models here.

from django.conf import settings
from django.db import models
from datetime import datetime
from django.utils import timezone

class Report(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField('波浪智投', max_length=200)
    bank_name = models.CharField('銀行名稱：', max_length=120)
    started_date = models.DateTimeField('開始投資日期： ', default=datetime.now)
    invest = models.IntegerField('總投資額 (TWDs): ', default=0)
    withdrew = models.IntegerField('總提款額 (TWDs): ', default=0)
    gain_loss = models.IntegerField('總成本的損益 (TWDs): ', default=0)
    face_value = models.IntegerField('最後一天的波浪帳戶面值 (USDs): ', default=0)
    venue = models.CharField('警察局所屬機關: ', max_length=120, blank=True, null=True)
    officer = models.CharField('分局警務員: ', max_length = 60, blank=True, null=True)
    text = models.TextField('其他備註: ', blank=True)

    def __str__(self):
        return self.title