from django.urls.conf import path
from pages import views


urlpatterns = [
    path('',views.home,name="home"),
    path('add',views.add,name="add"),



]
