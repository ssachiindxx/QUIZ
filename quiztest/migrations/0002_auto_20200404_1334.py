# Generated by Django 2.2.4 on 2020-04-04 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiztest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='option1',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='option2',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='option3',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='option4',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='answer',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question',
            field=models.CharField(max_length=500),
        ),
    ]
