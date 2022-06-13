# Generated by Django 4.0.5 on 2022-06-13 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=80, null=True)),
                ('length', models.IntegerField()),
                ('link', models.CharField(max_length=300)),
            ],
        ),
    ]