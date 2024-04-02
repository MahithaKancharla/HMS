# Generated by Django 5.0.1 on 2024-04-02 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0007_remove_wardeninfo_isfemale_remove_wardeninfo_ismale_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wardeninfo',
            name='blood_group',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='wardeninfo',
            name='contact_number',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='wardeninfo',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='wardeninfo',
            name='gender',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='wardeninfo',
            name='joining_year',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='wardeninfo',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='wardeninfo',
            name='room_no',
            field=models.IntegerField(),
        ),
    ]
