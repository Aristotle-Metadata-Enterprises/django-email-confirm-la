# cat 0003_alter_emailconfirmation_email.py 
# Generated by Django 3.2.20 on 2023-11-15 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_confirm_la', '0002_auto_20170713_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailconfirmation',
            name='email',
            field=models.EmailField(db_index=True, max_length=254, verbose_name='Email'),
        ),
    ]
