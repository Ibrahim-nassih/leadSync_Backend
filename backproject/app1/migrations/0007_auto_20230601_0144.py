# Generated by Django 3.2 on 2023-06-01 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]