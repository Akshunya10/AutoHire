# Generated by Django 3.2.4 on 2021-10-17 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_delete_create_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='address',
            field=models.CharField(max_length=300, null=True),
        ),
    ]