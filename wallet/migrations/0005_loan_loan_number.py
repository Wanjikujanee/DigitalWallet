# Generated by Django 4.1 on 2022-08-26 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0004_loan_guarantor'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='loan_number',
            field=models.IntegerField(default=None),
        ),
    ]
