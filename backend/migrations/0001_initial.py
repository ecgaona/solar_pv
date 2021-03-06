# Generated by Django 3.0.8 on 2020-07-29 02:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('solarpv', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('model_number', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('cell_technology', models.CharField(max_length=50)),
                ('cell_manufacturer', models.CharField(max_length=50)),
                ('number_of_cells', models.IntegerField()),
                ('number_of_cells_in_series', models.IntegerField()),
                ('number_of_series_strings', models.IntegerField()),
                ('number_of_diodes', models.IntegerField()),
                ('product_length', models.FloatField()),
                ('product_width', models.FloatField()),
                ('product_weight', models.FloatField()),
                ('superstrate_type', models.CharField(max_length=50)),
                ('superstrate_manufacturer', models.CharField(max_length=50)),
                ('substrate_type', models.CharField(max_length=50)),
                ('substrate_manufacturer', models.CharField(max_length=50)),
                ('frame_type', models.CharField(max_length=50)),
                ('frame_adhesive', models.CharField(max_length=50)),
                ('encapsulant_type', models.CharField(max_length=50)),
                ('encapsulant_manufacturer', models.CharField(max_length=50)),
                ('junction_box_type', models.CharField(max_length=50)),
                ('junction_box_manufacturer', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TestSequence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence_name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='TestStandard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('published_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('is_fl_required', models.BooleanField()),
                ('fl_frequency', models.FloatField()),
                ('standard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.TestStandard')),
            ],
        ),
        migrations.CreateModel(
            name='PerformanceData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_system_voltage', models.FloatField()),
                ('voc', models.FloatField()),
                ('isc', models.FloatField()),
                ('vmp', models.FloatField()),
                ('imp', models.FloatField()),
                ('pmp', models.FloatField()),
                ('ff', models.FloatField()),
                ('model_number', models.ForeignKey(db_column='model_number', on_delete=django.db.models.deletion.CASCADE, to='backend.Product')),
                ('sequence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.TestSequence')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(max_length=30)),
                ('address2', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=2)),
                ('postal_code', models.IntegerField()),
                ('phone_number', models.CharField(max_length=15)),
                ('fax_number', models.CharField(max_length=15)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solarpv.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('certificate_number', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('report_number', models.IntegerField()),
                ('issue_date', models.DateField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Location')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Product')),
                ('standard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.TestStandard')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
