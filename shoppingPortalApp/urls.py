from django.urls import path
from shoppingPortalApp import views


urlpatterns = [
    path('main/search/previous',views.index),
    path('add/',views.index_add),
    path('main/search/',views.result, name='result'),
    path('main/<name>/',views.showMedicine_name, name='medicine'),
    path('delete/<id>/',views.index_delete),
]