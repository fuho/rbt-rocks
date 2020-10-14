from django.urls import path, include

from rbts.views import index

app_name = 'rbts'
urlpatterns = [
    path('', index)
]
