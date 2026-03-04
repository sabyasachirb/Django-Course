from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="brand_logos/")
    def __str__(self):
        return self.name


class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete = models.CASCADE)
    model = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    image = models.ImageField(upload_to="car_images/")
    slug = models.SlugField(unique=True, blank=True, null=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{self.brand.name.lower()}-{self.model.lower().replace(' ', '-')}"
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.brand.name} -> {self.model}"
    
class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.car.model}"
