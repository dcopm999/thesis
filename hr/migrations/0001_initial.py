# Generated by Django 3.1.13 on 2021-09-23 11:00

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='Name')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='First name')),
                ('middle_name', models.CharField(max_length=100, verbose_name='Middle name')),
                ('last_name', models.CharField(db_index=True, max_length=100, verbose_name='Last name')),
                ('photo', sorl.thumbnail.fields.ImageField(upload_to='photos/staff/', verbose_name='Photo')),
                ('position', models.CharField(max_length=100, verbose_name='Position')),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Salary')),
                ('date_birth', models.DateField(verbose_name='Birth day')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hr.department', verbose_name='Department')),
            ],
            options={
                'verbose_name': 'Staff',
                'verbose_name_plural': 'Staff',
                'unique_together': {('first_name', 'middle_name', 'last_name', 'department')},
            },
        ),
        migrations.AddField(
            model_name='department',
            name='director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='director', to='hr.staff', verbose_name='Director'),
        ),
        migrations.AddField(
            model_name='department',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='hr.department'),
        ),
    ]