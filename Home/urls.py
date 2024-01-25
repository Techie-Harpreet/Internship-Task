from django.urls import path
from .views import *
urlpatterns = [
    path('', Home, name="home"),
    path('dynamic-data', dynamic_content, name="dynamic-data"),
    path('add-form-data', Add_Form_Data, name="add-form-data"),
    path('show-form-data', ShowData, name="show-form-data"),



]
