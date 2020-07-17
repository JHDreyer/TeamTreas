# Generated by Django 3.0.8 on 2020-07-17 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commerce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('location', models.CharField(default='None', max_length=255)),
                ('services', models.CharField(max_length=3000)),
                ('products', models.CharField(default='None', max_length=3000)),
                ('logo', models.ImageField(default='None', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('location', models.CharField(default='None', max_length=255)),
                ('services', models.CharField(max_length=3000)),
                ('products', models.CharField(default='None', max_length=3000)),
                ('logo', models.ImageField(default='None', upload_to='')),
            ],
        ),
    ]