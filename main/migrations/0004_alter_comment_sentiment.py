# Generated by Django 4.2.5 on 2023-12-02 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_comment_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='sentiment',
            field=models.CharField(max_length=100),
        ),
    ]
