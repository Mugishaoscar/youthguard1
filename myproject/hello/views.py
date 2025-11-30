from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PostForm,UserProfileForm,ReminderSettingForm,chatbotFAQForm,LocationForm,StockItemForm,ContraceptiveForm,NotificationForm
from .models import Post,UserProfile,ReminderSetting,chatbotFAQ,Location,StockItem,ContraceptiveType,Notification



def hello(request):
    context = {"names": ["world", "oscar", "Best"]}
    return render(request, "hello/hello.html", context)

def post_list(request):
    posts = Post.objects.all()
    return render(request, "post/list.html", {"posts": posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, "post/detail.html", {"post": post})


@login_required
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect("post_list")
    return render(request, "post/create.html", {"form": form})


@login_required
def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect("post_list")
    return render(request, "post/update.html", {"form": form, "post": post})


@login_required
def delete_post(request, id):
    post = Post.objects.get(id=id)

    if request.method == "POST":
        post.delete()
        return redirect('post_list')

    return render(request, 'post/delete.html', {'post': post})

@login_required
def userprofile_create(request):
    form = UserProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('userprofile_list')
    return render(request, 'userprofile/create.html', {'form': form})

@login_required
def userprofile_update(request, id):
    user = get_object_or_404(UserProfile, id=id)
    form = UserProfileForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('userprofile_list')
    return render(request, 'userprofile/update.html', {'form': form, 'user': user})

@login_required
def userprofile_list(request):
    users = UserProfile.objects.all()
    return render(request, 'userprofile/list.html', {'users': users})
@login_required
def userprofile_detail(request, id):
    user = get_object_or_404(UserProfile, id=id)
    return render(request, 'userprofile/detail.html', {'user': user})
@login_required
def userprofile_delete(request, id):
    user = get_object_or_404(UserProfile, id=id)
    if request.method == "POST":
        user.delete()
        return redirect('userprofile_list')
    return render(request, 'userprofile/delete.html', {'user': user})

#reminder setting

def remindersetting_list(request):
    reminders = ReminderSetting.objects.all()
    return render(request, 'remindersetting/list.html', {'reminders': reminders})

# DETAIL
def remindersetting_detail(request, id):
    reminder = get_object_or_404(ReminderSetting, id=id)
    return render(request, 'remindersetting/detail.html', {'reminder': reminder})

# CREATE
def remindersetting_create(request):
    if request.method == "POST":
        form = ReminderSettingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('remindersetting_list')
    else:
        form = ReminderSettingForm()
    return render(request, 'remindersetting/create.html', {'form': form})

# UPDATE
def remindersetting_update(request, id):
    reminder = get_object_or_404(ReminderSetting, id=id)
    if request.method == "POST":
        form = ReminderSettingForm(request.POST, instance=reminder)
        if form.is_valid():
            form.save()
            return redirect('remindersetting_list')
    else:
        form = ReminderSettingForm(instance=reminder)
    return render(request, 'remindersetting/update.html', {'form': form})

# DELETE
def remindersetting_delete(request, id):
    reminder = get_object_or_404(ReminderSetting, id=id)
    if request.method == "POST":
        reminder.delete()
        return redirect('remindersetting_list')
    return render(request, 'remindersetting/delete.html', {'reminder': reminder})

def faq_detail(request, id):
    faq = chatbotFAQ.objects.get(id=id)
    return render(request, "chatbotFAQ/detail.html", {"faq": faq})


def faq_list(request):
    faqs = chatbotFAQ.objects.all()
    return render(request, 'chatbotFAQ/list.html', {'faqs': faqs})

from .forms import FAQForm

def faq_create(request):
    if request.method == "POST":
        form = FAQForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faq_list')
    else:
        form = FAQForm()

    return render(request, 'chatbotFAQ/create.html', {'form': form})


def faq_update(request, id):
    faq = chatbotFAQ.objects.get(id=id)

    if request.method == "POST":
        form = FAQForm(request.POST, instance=faq)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = FAQForm(instance=faq)

    return render(request, 'chatbotFAQ/update.html', {'form': form})

def faq_delete(request, id):
    faq = get_object_or_404(chatbotFAQ, id=id)

    if request.method == "POST":
        faq.delete()
        return redirect('faq_list')

    return render(request, 'chatbotFAQ/delete.html', {'faq': faq})

def location_list(request):
    locations = Location.objects.all()
    return render(request, "location/list.html", {"locations": locations})

# DETAIL
def location_detail(request, pk):
    location = get_object_or_404(Location, pk=pk)
    return render(request, "location/detail.html", {"location": location})

# CREATE
def location_create(request):
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("location_list")
    else:
        form = LocationForm()
    return render(request, "location/create.html", {"form": form, "title": "Create Location"})

# UPDATE
def location_update(request, pk):
    location = get_object_or_404(Location, pk=pk)
    if request.method == "POST":
        form = LocationForm(request.POST, instance=location)
        if form.is_valid():
            form.save()
            return redirect("location_list")
    else:
        form = LocationForm(instance=location)
    return render(request, "location/update.html", {"form": form, "title": "Update Location"})

# DELETE
def location_delete(request, pk):
    location = get_object_or_404(Location, pk=pk)
    if request.method == "POST":
        location.delete()
        return redirect("location_list")
    return render(request, "location/delete.html", {"location": location})

def contraceptive_list(request):
    items = ContraceptiveType.objects.all()
    return render(request, "contraceptive/list.html", {"items": items})

def contraceptive_create(request):
    form = ContraceptiveForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("contraceptive_list")
    return render(request, "contraceptive/create.html", {"form": form})

def contraceptive_update(request, id):
    item = get_object_or_404(ContraceptiveType, id=id)
    form = ContraceptiveForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('contraceptive_list')

    return render(request, "contraceptive/update.html", {"form": form})


def contraceptive_delete(request, id):
    item = get_object_or_404(ContraceptiveType, id=id)
    
    if request.method == "POST":
        item.delete()
        return redirect("contraceptive_list")

    return render(request, "contraceptive/delete.html", {"item": item})

def contraceptive_detail(request, id):
    item = get_object_or_404(ContraceptiveType, id=id)
    return render(request, "contraceptive/detail.html", {"item": item})



def stock_list(request):
    items = StockItem.objects.all()
    return render(request, 'hello/stock_list.html', {'items': items})

def stock_create(request):
    form = StockItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('stock_list')
    return render(request, 'hello/stock_form.html', {'form': form})

def stock_update(request, id):
    item = StockItem.objects.get(id=id)
    form = StockItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('stock_list')
    return render(request, 'hello/stock_form.html', {'form': form})

def stock_delete(request, id):
    item = StockItem.objects.get(id=id)
    item.delete()
    return redirect('stock_list')

#Notifiction

def notification_list(request):
    items = Notification.objects.all()
    return render(request, "notification/list.html", {"items": items})

def notification_create(request):
    form = NotificationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("notification_list")
    return render(request, "notification/create.html", {"form": form})

def notification_detail(request, id):
    item = get_object_or_404(Notification, id=id)
    return render(request, "notification/detail.html", {"item": item})

def notification_update(request, id):
    item = get_object_or_404(Notification, id=id)
    form = NotificationForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect("notification_list")

    return render(request, "notification/update.html", {"form": form})

def notification_delete(request, id):
    item = get_object_or_404(Notification, id=id)

    if request.method == "POST":
        item.delete()
        return redirect("notification_list")

    return render(request, "notification/delete.html", {"item": item})

#stoch items
# LIST VIEW
def stock_list(request):
    items = StockItem.objects.all()
    return render(request, "stock/stock_list.html", {"items": items})


# CREATE VIEW
def stock_create(request):
    form = StockItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("stock_list")
    return render(request, "stock/stock_form.html", {"form": form})


# DETAIL VIEW
def stock_detail(request, id):
    item = get_object_or_404(StockItem, id=id)
    return render(request, "stock/stock_detail.html", {"item": item})


# UPDATE VIEW
def stock_update(request, id):
    item = get_object_or_404(StockItem, id=id)
    form = StockItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect("stock_list")
    return render(request, "stock/stock_form.html", {"form": form})


# DELETE VIEW
def stock_delete(request, id):
    item = get_object_or_404(StockItem, id=id)
    if request.method == "POST":
        item.delete()
        return redirect("stock_list")
    return render(request, "stock/stock_delete.html", {"item": item})
