from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.gis.db import models as gis_models

class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Add a custom related_name
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        verbose_name=('groups')
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permission_set',  # Add a custom related_name
        blank=True,
        help_text=('Specific permissions for this user.'),
        verbose_name=('user permissions')
    )

    def __str__(self):
        return self.username

class Mechanic(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience = models.IntegerField()
    vehicles_of_expertise = models.TextField()
    location = models.CharField(max_length=255)
    work_hours = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    geo_location = gis_models.PointField()
    # geo_location = models.PointField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} - Mechanic'



class Service(models.Model):
    mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.service_name
    

    
class Request(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car_model = models.CharField(max_length=255)
    car_number = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    car_image = models.ImageField(upload_to='car_images/', null=True, blank=True)
    geo_location = gis_models.PointField(geography=True, null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.car_model}'
    


class Availability(models.Model):
    mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    day_of_week = models.CharField(max_length=10)  # e.g., Monday, Tuesday
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.mechanic.user.username} - {self.day_of_week} ({self.start_time} to {self.end_time})'
