from django.urls import path
from . import views

urlpatterns = [
    path("", views.hello, name="hello"),

    path("post/", views.post_list, name="post_list"),
    path("post/<int:id>/", views.post_detail, name="post_detail"),
    path("post/create/", views.post_create, name="post_create"),
    path("post/update/<int:id>/", views.post_update, name="post_update"),
    path("post/delete/<int:id>/", views.delete_post, name="post_delete"),

    path('userprofile/', views.userprofile_list, name='userprofile_list'),
    path('userprofile/<int:id>/', views.userprofile_detail, name='userprofile_detail'),
    path('userprofile/create/', views.userprofile_create, name='userprofile_create'),
    path('userprofile/update/<int:id>/', views.userprofile_update, name='userprofile_update'),
    path('userprofile/delete/<int:id>/', views.userprofile_delete, name='userprofile_delete'),

    path('remindersetting/', views.remindersetting_list, name='remindersetting_list'),
    path('remindersetting/<int:id>/', views.remindersetting_detail, name='remindersetting_detail'),
    path('remindersetting/create/', views.remindersetting_create, name='remindersetting_create'),
    path('remindersetting/update/<int:id>/', views.remindersetting_update, name='remindersetting_update'),
    path('remindersetting/delete/<int:id>/', views.remindersetting_delete, name='remindersetting_delete'),

    # FAQ
    path("faq/", views.faq_list, name="faq_list"),
    path("faq/create/", views.faq_create, name="faq_create"),
    path("faq/detail/<int:id>", views.faq_detail, name="faq_detail"),
    path("faq/update/<int:id>/", views.faq_update, name="faq_update"),
    path("faq/delete/<int:id>/", views.faq_delete, name="faq_delete"),

    # Location
    path("location/", views.location_list, name="location_list"),
    path("location/create/", views.location_create, name="location_create"),
    path("location/<int:pk>/", views.location_detail, name="location_detail"),
    path("location/<int:pk>/update/", views.location_update, name="location_update"),
    path("location/<int:pk>/delete/", views.location_delete, name="location_delete"),

    # Contraceptive types
    path("contraceptive/", views.contraceptive_list, name="contraceptive_list"),
    path("contraceptive/create/", views.contraceptive_create, name="contraceptive_create"),
    path("contraceptive/update/<int:id>/", views.contraceptive_update, name="contraceptive_update"),
    path("contraceptive/delete/<int:id>/", views.contraceptive_delete, name="contraceptive_delete"),
    path("contraceptive/detail/<int:id>/", views.contraceptive_detail, name="contraceptive_detail"),

    # Stock Items
    path("stock/", views.stock_list, name="stock_list"),
    path("stock/create/", views.stock_create, name="stock_create"),
    path("stock/update/<int:id>/", views.stock_update, name="stock_update"),
    path("stock/delete/<int:id>/", views.stock_delete, name="stock_delete"),

    #Notifiction
    path("notification/", views.notification_list, name="notification_list"),
    path("notification/create/", views.notification_create, name="notification_create"),
    path("notification/<int:id>/", views.notification_detail, name="notification_detail"),
    path("notification/update/<int:id>/", views.notification_update, name="notification_update"),
    path("notification/delete/<int:id>/", views.notification_delete, name="notification_delete"),

    #stockitems
    path("", views.stock_list, name="stock_list"),
    path("create/", views.stock_create, name="stock_create"),
    path("<int:id>/", views.stock_detail, name="stock_detail"),
    path("<int:id>/update/", views.stock_update, name="stock_update"),
    path("<int:id>/delete/", views.stock_delete, name="stock_delete"),
]
