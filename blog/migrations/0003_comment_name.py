# Generated by Django 3.0.6 on 2020-06-02 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default='', max_length=80),
            preserve_default=False,
        ),
    ]
