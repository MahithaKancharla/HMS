# Generated by Django 5.0.1 on 2024-04-02 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0005_alter_studentinfo_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WardenInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('joining_year', models.CharField(max_length=255)),
                ('room_no', models.IntegerField()),
                ('blood_group', models.CharField(max_length=255)),
                ('contact_number', models.CharField(max_length=255)),
                ('ismale', models.BooleanField(default=False)),
                ('isfemale', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
