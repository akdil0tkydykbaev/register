# Generated by Django 5.1.4 on 2024-12-21 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_person_delete_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.CharField(max_length=15, verbose_name='пaроль'),
        ),
    ]
