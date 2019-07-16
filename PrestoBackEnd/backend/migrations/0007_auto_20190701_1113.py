# Generated by Django 2.2.2 on 2019-07-01 04:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20190701_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodoption',
            name='option',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.Option'),
        ),
        migrations.AddField(
            model_name='option',
            name='markets',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.Market'),
        ),
        migrations.AlterField(
            model_name='order',
            name='timeToOrder',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 7, 1, 11, 13, 5, 40813), null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='timeToSend',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 7, 1, 11, 13, 5, 40813), null=True),
        ),
        migrations.AlterField(
            model_name='staterider',
            name='timeFinishOrder',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 7, 1, 11, 13, 5, 40813), null=True),
        ),
        migrations.AlterField(
            model_name='staterider',
            name='timeTakeFood',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 7, 1, 11, 13, 5, 40813), null=True),
        ),
        migrations.AlterField(
            model_name='staterider',
            name='timeTakeOrder',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 7, 1, 11, 13, 5, 40813), null=True),
        ),
    ]
