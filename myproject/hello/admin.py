from django.contrib import admin

# Register your models here.
from .models import (
    Profile,Post,UserProfile,
    ReminderSetting,Notification,chatbotFAQ,Location,ContraceptiveType,
    StockItem,IoTReading,StockAlert)

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(UserProfile)
admin.site.register(ReminderSetting)
admin.site.register(Notification)
admin.site.register(chatbotFAQ)
admin.site.register(Location)
admin.site.register(ContraceptiveType)
admin.site.register(StockItem)
admin.site.register(IoTReading)
admin.site.register(StockAlert)
