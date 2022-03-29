# Generated by Django 4.0.1 on 2022-01-06 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='new',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('dob', models.CharField(max_length=30)),
                ('passwd', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('year', models.EmailField(max_length=30)),
                ('hobbies', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='news',
            fields=[
                ('idnew', models.AutoField(primary_key=True, serialize=False)),
                ('clz', models.CharField(max_length=30)),
                ('db', models.CharField(max_length=30)),
                ('fr_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.new')),
            ],
        ),
    ]