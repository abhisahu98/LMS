# Generated by Django 5.1.4 on 2024-12-06 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='assessment_id',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='user',
        ),
        migrations.AddField(
            model_name='feedback',
            name='instructor',
            field=models.CharField(default='Unknown', max_length=255),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='course_id',
            field=models.CharField(max_length=255),
        ),
    ]