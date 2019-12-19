# Generated by Django 3.0 on 2019-12-19 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommonInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('commoninfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='abstract.CommonInfo')),
                ('academy', models.CharField(max_length=20)),
            ],
            bases=('abstract.commoninfo',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('commoninfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='abstract.CommonInfo')),
                ('school', models.CharField(max_length=30)),
            ],
            bases=('abstract.commoninfo',),
        ),
    ]
