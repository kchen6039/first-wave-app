# Generated by Django 2.2.7 on 2019-11-18 11:35

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='波浪智投')),
                ('bank_name', models.CharField(max_length=120, verbose_name='銀行名稱：')),
                ('started_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='開始投資日期： ')),
                ('invest', models.IntegerField(default=0, verbose_name='總投資額 (TWDs): ')),
                ('withdrew', models.IntegerField(default=0, verbose_name='總提款額 (TWDs): ')),
                ('gain_loss', models.IntegerField(default=0, verbose_name='總成本的損益 (TWDs): ')),
                ('face_value', models.IntegerField(default=0, verbose_name='最後一天的波浪帳戶面值 (USDs): ')),
                ('venue', models.CharField(blank=True, max_length=120, null=True, verbose_name='警察局所屬機關: ')),
                ('officer', models.CharField(blank=True, max_length=60, null=True, verbose_name='分局警務員: ')),
                ('text', models.TextField(blank=True, verbose_name='其他備註: ')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
