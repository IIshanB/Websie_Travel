from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

# Create your models here.



class Activity(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='activities/', null=True, blank=True)

    def __str__(self):
        return self.name

class TravelPackage(models.Model):
    name = models.CharField(max_length=255)  # Heading for the travel package
    price = models.IntegerField(default=0)
    actual_price = models.IntegerField(default=0)
    description = models.TextField()  # Detailed description of the package
    review_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)  # Average rating from reviews
    reviews_count = models.IntegerField(default=0)
    days=models.IntegerField(default=0)# Number of reviews
    image = models.ImageField(upload_to='packages/')  # Optional image for the package
    activities = models.ManyToManyField(Activity, related_name='travel_packages',blank=True)  # Related activities

    def __str__(self):
        return self.name

    def get_packagedays(self):
        return self.days+1
    def saved_amount(self):
        return self.actual_price-self.price




    def save(self, *args, **kwargs):
        # Open the image using Pillow
        img = Image.open(self.image)

        # Resize the image to a specific size (e.g., 800x600)
        if img.height > 600 or img.width > 800:
            output_size = (340, 340)
            img = img.resize(output_size, Image.Resampling.LANCZOS)

            # Save the resized image back to self.image
            img_io = BytesIO()
            img.save(img_io, format='PNG', quality=100)

            # Use Django's ContentFile to save the resized image
            self.image.save(self.image.name, ContentFile(img_io.getvalue()), save=False)

        # Call the parent save method
        super().save(*args, **kwargs)



class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='team_images/')
    twitter_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        # Open the image using Pillow
        img = Image.open(self.image)

        # Resize the image to a specific size (e.g., 800x600)
        if img.height > 10 or img.width > 10:
            output_size = (340, 340)
            img = img.resize(output_size, Image.Resampling.LANCZOS)

            # Save the resized image back to self.image
            img_io = BytesIO()
            img.save(img_io, format='PNG', quality=100)

            # Use Django's ContentFile to save the resized image
            self.image.save(self.image.name, ContentFile(img_io.getvalue()), save=False)

        # Call the parent save method
        super().save(*args, **kwargs)

from django.db import models

class TravelItinerary(models.Model):
    travel_package = models.ForeignKey(TravelPackage, related_name='itineraries', on_delete=models.CASCADE)
    day_number = models.IntegerField()  # Which day of the itinerary
    title = models.CharField(max_length=255)  # Title for the day's itinerary
    description = models.TextField()  # Description of activities for the day

    def __str__(self):
        return f"{self.travel_package.name} - Day {self.day_number} Itinerary"

class ItineraryImage(models.Model):
    itinerary = models.ForeignKey(TravelItinerary, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='itinerary_images/')
    caption = models.CharField(max_length=255, blank=True, null=True)  # Optional image caption

    def __str__(self):
        return f"Image for {self.itinerary.travel_package.name} - Day {self.itinerary.day_number}"

    def save(self, *args, **kwargs):
        # Open the image using Pillow
        img = Image.open(self.image)

        # Resize the image to a specific size (e.g., 800x600)
        if img.height > 10 or img.width > 20:
            output_size = (350, 270)
            img = img.resize(output_size, Image.Resampling.LANCZOS)

            # Save the resized image back to self.image
            img_io = BytesIO()
            img.save(img_io, format='PNG', quality=100)

            # Use Django's ContentFile to save the resized image
            self.image.save(self.image.name, ContentFile(img_io.getvalue()), save=False)

        # Call the parent save method
        super().save(*args, **kwargs)

