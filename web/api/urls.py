from django.urls import path
from api.views import *

urlpatterns = [
    path('hello', Hello.as_view()),
    path('data', GenDataView.as_view()),
    path('save-data', SaveDataView.as_view()),
]
