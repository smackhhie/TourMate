# Generated by Django 4.2.7 on 2023-12-25 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_report_detail_results'),
    ]

    operations = [
        migrations.CreateModel(
            name='TechAdd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50)),
                ('contact', models.IntegerField()),
                ('password', models.CharField(max_length=50)),
                ('com_password', models.CharField(max_length=50)),
                ('gender', models.DateField(max_length=50)),
            ],
        ),
    ]
