# Generated by Django 4.1.7 on 2023-03-23 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100, null=True)),
                ('option', models.CharField(max_length=60, null=True)),
                ('mobile_no', models.CharField(max_length=14, null=True)),
            ],
        ),
    ]
