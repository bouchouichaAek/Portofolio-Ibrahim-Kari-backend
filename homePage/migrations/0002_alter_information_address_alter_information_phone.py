# Generated by Django 4.0.3 on 2022-03-23 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='Address',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='information',
            name='Phone',
            field=models.TextField(),
        ),
    ]
