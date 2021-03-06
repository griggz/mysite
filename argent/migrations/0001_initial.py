# Generated by Django 2.1 on 2019-03-16 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('city', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'ordering': ['city'],
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('country', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'ordering': ['country'],
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('spending', models.CharField(blank=True, max_length=500, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('spending_sum', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('currency', models.CharField(blank=True, choices=[('USD', '(USD) US Dollar'), ('EUR', '(EUR) Euro'), ('GBP', '(GBP) United Kingdom Pound'), ('CZK', '(CZK) Czech Republic Koruna'), ('HUF', '(HUF) Hungary Forint'), ('CHF', '(CHF) Swiss Franc')], max_length=900, null=True)),
                ('xrate', models.DecimalField(blank=True, decimal_places=4, max_digits=9, null=True)),
                ('dollars_sum', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('daily_savings_dollars', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('daily_savings_display', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='argent.City')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='MonthYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(blank=True, max_length=500, null=True)),
                ('year', models.CharField(blank=True, max_length=500, null=True)),
                ('total_spent', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('total_spent_dollars', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('total_savings', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('total_savings_display', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Savings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_spent', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('total_spent_dollars', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('total_savings', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('total_savings_display', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='argent.Country'),
        ),
    ]
