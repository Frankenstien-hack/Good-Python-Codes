# Generated by Django 2.1.2 on 2018-10-06 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('cuisine', models.CharField(choices=[(1, 'Chinese'), (2, 'North Indian'), (3, 'South Indian'), (4, 'Italian')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('closing_time', models.TimeField(blank=True, null=True)),
                ('owner', models.CharField(blank=True, max_length=100, null=True)),
                ('contact', models.EmailField(max_length=254)),
                ('address', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Restaurant'),
        ),
    ]
