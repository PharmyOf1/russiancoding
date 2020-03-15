# Generated by Django 3.0.1 on 2020-03-07 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200301_2250'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vocab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('russian', models.CharField(max_length=200)),
                ('english', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['russian'],
            },
        ),
    ]
