# Generated by Django 4.0 on 2022-01-04 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.TextField()),
                ('number', models.TextField()),
                ('bip39', models.TextField()),
                ('sha256', models.TextField()),
            ],
            options={
                'db_table': 'lottery_period',
            },
        ),
    ]