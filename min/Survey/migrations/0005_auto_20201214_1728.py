# Generated by Django 3.1.3 on 2020-12-14 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Survey', '0004_question_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='option',
            old_name='qty',
            new_name='rate',
        ),
    ]