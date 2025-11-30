from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
class UserProfile(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    preferences = models.TextField()

    def __str__(self):
        return self.user_name

class ReminderSetting(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    reminder_time = models.CharField(max_length=50)
    reminder_message = models.TextField()

    def __str__(self):
        return f"Reminder for {self.user.user_name}"
    
class Notification(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=50)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification to {self.user.user_name}"


class chatbotFAQ(models.Model):
    question=models.TextField()
    answer = models.TextField(default="No answer provided")

    def __str__(self):
        return self.question[:40]

class Location(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class ContraceptiveType(models.Model):
    category = models.CharField(max_length=100)
    instructions = models.TextField()
    side_effects = models.TextField()

    def __str__(self):
        return self.category
    
class StockItem(models.Model):
    type = models.ForeignKey(ContraceptiveType, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.type.category} @ {self.location.location_name}"
    
class IoTReading(models.Model):
    device_id = models.IntegerField()
    stock_level = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    timestamp = models.DateTimeField()

    def __str__(self):
        return f"IoT Reading at {self.location.location_name}"
    
class StockAlert(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    item = models.ForeignKey(StockItem, on_delete=models.CASCADE)
    alert_type = models.CharField(max_length=50)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"Alert at {self.location.location_name}"