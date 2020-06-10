# Generated by Django 3.0.6 on 2020-06-10 02:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('boyNum', models.IntegerField()),
                ('girlNum', models.IntegerField()),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'grades',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('sex', models.BooleanField()),
                ('content', models.CharField(max_length=40)),
                ('isDelete', models.BooleanField(default=False)),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Grade')),
            ],
            options={
                'db_table': 'students',
            },
        ),
    ]
