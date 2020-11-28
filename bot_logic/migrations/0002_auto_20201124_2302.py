# Generated by Django 3.1.3 on 2020-11-24 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot_logic', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='user_condition',
        ),
        migrations.AddField(
            model_name='studentcondition',
            name='student',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='bot_logic.student'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='FIO',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='agency',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='city',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
