# Generated by Django 2.2.3 on 2020-01-21 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('package_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='FileUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=100, unique=True)),
                ('upload_file', models.FileField(upload_to='file/%Y')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='package_app.FileCategory')),
                ('package_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rnfile', to='package_app.Packages')),
            ],
        ),
    ]
