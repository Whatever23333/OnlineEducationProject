# Generated by Django 2.0.4 on 2018-06-12 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180605_0844'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emailverifyrecord',
            options={'verbose_name': '邮箱验证码', 'verbose_name_plural': '邮箱验证码'},
        ),
    ]
