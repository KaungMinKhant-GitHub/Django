# Generated by Django 3.2.6 on 2021-08-26 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('phno', models.CharField(max_length=200, null=True)),
                ('create_at', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
