# Generated by Django 4.0.3 on 2022-09-21 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_employee_employee_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_code',
            field=models.CharField(max_length=200),
        ),
    ]