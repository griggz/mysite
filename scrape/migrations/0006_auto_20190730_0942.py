# Generated by Django 2.1 on 2019-07-30 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scrape', '0005_remove_results_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='business',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='business', to='scrape.Yelp'),
        ),
    ]