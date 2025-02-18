# Generated by Django 4.2.9 on 2024-09-15 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0008_teammember'),
    ]

    operations = [
        migrations.CreateModel(
            name='TravelItinerary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_number', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('travel_package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itineraries', to='homepage.travelpackage')),
            ],
        ),
        migrations.CreateModel(
            name='ItineraryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='itinerary_images/')),
                ('caption', models.CharField(blank=True, max_length=255, null=True)),
                ('itinerary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='homepage.travelitinerary')),
            ],
        ),
    ]
