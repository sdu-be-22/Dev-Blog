# Generated by Django 4.0.2 on 2022-03-13 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0020_comment_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='profile_pic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myblog.profile'),
        ),
    ]