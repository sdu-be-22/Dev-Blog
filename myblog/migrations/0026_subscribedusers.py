# Generated by Django 4.0.2 on 2022-03-24 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0025_alter_post_post_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscribedUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
