# Generated by Django 5.0.1 on 2024-04-02 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentinfo',
            name='address',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='blood_group',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='contact_number',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='department',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='father_name',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='gender',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='joining_year',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='mother_name',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='room_no',
            field=models.IntegerField(default=None),
        ),
    ]
