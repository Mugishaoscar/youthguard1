from django import forms
# from .models import Post

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title', 'content']
        
# from django import forms
from .models import Post, Profile, UserProfile, chatbotFAQ,ReminderSetting,Notification,chatbotFAQ, Location, ContraceptiveType, StockItem
                    

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'

class chatbotFAQForm(forms.ModelForm):
    class Meta:
        model = chatbotFAQ
        fields = '__all__'

class ReminderSettingForm(forms.ModelForm):
    class Meta:
        model= ReminderSetting
        fields='__all__'

class NotificationForm(forms.ModelForm):
    class Meta:
        model=Notification
        fields='__all__'

class FAQForm(forms.ModelForm):
    class Meta:
        model = chatbotFAQ
        fields = "__all__"

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'description']

class ContraceptiveForm(forms.ModelForm):
    class Meta:
        model = ContraceptiveType
        fields = ['category', 'instructions', 'side_effects']

class StockItemForm(forms.ModelForm):
    class Meta:
        model = StockItem
        fields = "__all__"
