# Generated by Django 2.1.7 on 2019-04-19 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0003_remove_registration_registered_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=23)),
                ('mobile_no', models.BigIntegerField()),
                ('email_id', models.EmailField(max_length=254)),
                ('block', models.CharField(choices=[('N.B', 'NEW BLOCK'), ('N.B.X', 'NBX'), ('M.B', 'MESS BLOCK'), ('M.M', 'MM'), ('I.T', 'IT'), ('I.H', 'IH')], max_length=3)),
                ('room_no', models.CharField(max_length=5)),
                ('subject', models.TextField()),
                ('complaint', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LeaveApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=29)),
                ('block', models.CharField(choices=[('N.B', 'NEW BLOCK'), ('N.B.X', 'NBX'), ('M.B', 'MESS BLOCK'), ('M.M', 'MM'), ('I.T', 'IT'), ('I.H', 'IH')], max_length=3)),
                ('room_no', models.CharField(max_length=5)),
                ('stu_mob_no', models.BigIntegerField()),
                ('par_mob_no', models.BigIntegerField()),
                ('leaving_date', models.DateTimeField()),
                ('arriving_date', models.DateTimeField()),
            ],
        ),
    ]
