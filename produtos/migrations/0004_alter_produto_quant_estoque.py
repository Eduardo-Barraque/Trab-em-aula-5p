# Generated by Django 3.2.13 on 2022-06-04 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0003_auto_20220604_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='quant_estoque',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]