# Generated by Django 2.1.7 on 2019-05-04 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='access_key',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='provider',
            field=models.CharField(choices=[('app', 'web'), ('ka', 'kakao')], default='app', max_length=20),
        ),
        migrations.AddField(
            model_name='customuser',
            name='refresh_token',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]