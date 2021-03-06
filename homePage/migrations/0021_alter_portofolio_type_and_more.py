# Generated by Django 4.0.3 on 2022-04-07 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0020_rename_نوع_portofolio_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portofolio',
            name='Type',
            field=models.CharField(choices=[('الكل', 'all'), ('كتاب', 'book'), ('صورة', 'picture'), ('فيديو', 'videos'), ('فيلم قصير', 'movies'), ('تصميم', 'design')], default='All', max_length=50),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='download_project',
            field=models.FileField(default='project', upload_to='Downloadproject/'),
        ),
    ]
