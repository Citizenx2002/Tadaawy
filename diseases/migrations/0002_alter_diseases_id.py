# Generated by Django 4.0 on 2021-12-22 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diseases', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diseases',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]