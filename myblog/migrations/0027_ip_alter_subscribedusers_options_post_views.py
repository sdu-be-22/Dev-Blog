# Generated by Django 4.0.2 on 2022-03-25 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0026_subscribedusers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='subscribedusers',
            options={'verbose_name_plural': 'Subscribed Users'},
        ),
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.ManyToManyField(blank=True, related_name='post_views', to='myblog.Ip', verbose_name='Views'),
        ),
    ]
