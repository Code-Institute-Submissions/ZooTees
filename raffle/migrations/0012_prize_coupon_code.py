# Generated by Django 3.2 on 2022-08-19 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raffle', '0011_auto_20220819_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='prize',
            name='coupon_code',
            field=models.CharField(editable=False, max_length=32, null=True),
        ),
    ]
