# Generated by Django 3.2 on 2022-08-17 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('raffle', '0007_alter_userentry_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userentry',
            name='user_profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.userprofile'),
        ),
    ]
