# Generated by Django 3.2.4 on 2021-08-01 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0004_trial_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='trial',
            name='enrolled',
            field=models.BooleanField(default=True),
        ),
    ]