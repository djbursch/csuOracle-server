# Generated by Django 2.2.10 on 2020-02-14 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insert2DB', '0002_auto_20200214_1752'),
    ]

    operations = [
        migrations.CreateModel(
            name='markovModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolName', models.TextField(max_length=200)),
                ('departmentName', models.TextField(max_length=200)),
                ('pubDate', models.DateTimeField(verbose_name='date published')),
                ('weights', models.IntegerField()),
            ],
        ),
    ]
