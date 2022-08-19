# Generated by Django 3.2 on 2022-08-19 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('raffle', '0010_alter_userentry_user_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userentry',
            name='won',
        ),
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raffle_entry', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='raffle.userentry')),
            ],
        ),
    ]
