# Generated by Django 3.0.6 on 2020-05-25 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200524_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=500)),
                ('pub_date', models.DateField()),
            ],
        ),
    ]
