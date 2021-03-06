# Generated by Django 3.1.3 on 2020-11-24 14:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('is_right', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('category', models.CharField(max_length=255)),
                ('paragraph', models.TextField()),
                ('multi_answer', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=0)),
                ('language', models.CharField(default='RU', max_length=5)),
                ('step', models.IntegerField(default=0)),
                ('FIO', models.CharField(max_length=500)),
                ('agency', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='StudentTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('closed', models.BooleanField(default=False)),
                ('date_start', models.DateTimeField(default=django.utils.timezone.now)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot_logic.student')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot_logic.test')),
            ],
        ),
        migrations.CreateModel(
            name='StudentCondition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_selected_answers', models.ManyToManyField(to='bot_logic.Answer')),
                ('current_test', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='current_test', to='bot_logic.test')),
                ('tests', models.ManyToManyField(related_name='tests', to='bot_logic.Test')),
            ],
        ),
        migrations.CreateModel(
            name='StudentAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answers', models.ManyToManyField(to='bot_logic.Answer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot_logic.question')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot_logic.student')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot_logic.studenttest')),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
        migrations.AddField(
            model_name='student',
            name='user_condition',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bot_logic.studentcondition'),
        ),
        migrations.AddField(
            model_name='question',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot_logic.test'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot_logic.question'),
        ),
    ]
