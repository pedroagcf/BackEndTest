# Generated by Django 4.2.5 on 2023-10-02 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_dividend_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dividend',
            old_name='value',
            new_name='amount',
        ),
    ]
