# Generated by Django 3.0.8 on 2020-07-02 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app1', '0002_delete_bank'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=64)),
                ('ifsc_code', models.CharField(max_length=64)),
                ('bank_addr', models.CharField(max_length=64)),
                ('city', models.CharField(max_length=64)),
            ],
        ),
    ]
