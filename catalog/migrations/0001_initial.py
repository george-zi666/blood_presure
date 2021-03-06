# Generated by Django 3.0.6 on 2020-06-02 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('last_name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('user_login', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='UsersMeasurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('systolic', models.IntegerField(max_length=10)),
                ('dyastolic', models.IntegerField(max_length=10)),
                ('pulse', models.IntegerField(max_length=10)),
                ('date_measure', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('p', 'performed'), ('n', 'not performed')], default='p', help_text='status measurement', max_length=1)),
                ('measure', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Measure')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.User')),
            ],
            options={
                'ordering': ['date_measure'],
            },
        ),
        migrations.AddField(
            model_name='measure',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.User'),
        ),
    ]
