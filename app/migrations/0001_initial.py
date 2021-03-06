# Generated by Django 3.1.2 on 2020-10-19 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.IntegerField()),
                ('info', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=40)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
