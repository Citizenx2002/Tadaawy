# Generated by Django 4.0 on 2021-12-25 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diseases', '0007_remove_diseases_id_alter_diseases_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='diseases',
            name='attribute',
            field=models.CharField(default=1, max_length=800),
            preserve_default=False,
        ),
    ]
