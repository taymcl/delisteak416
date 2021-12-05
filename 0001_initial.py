# Generated by Django 3.2.9 on 2021-12-02 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('reserve_time', models.TimeField()),
                ('reserve_email', models.EmailField(max_length=254)),
                ('reserve_date', models.DateField()),
                ('reserve_party', models.IntegerField()),
            ],
        ),
    ]