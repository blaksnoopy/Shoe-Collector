# Generated by Django 2.2.6 on 2019-12-17 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=20)),
                ('brand_name', models.CharField(max_length=20)),
                ('colorway', models.CharField(max_length=20)),
                ('size', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cleaning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('condition', models.CharField(choices=[('C', 'Clean'), ('S', 'Slightly Dirty'), ('D', 'Dirty')], default='C', max_length=1)),
                ('shoe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Shoe')),
            ],
        ),
    ]
