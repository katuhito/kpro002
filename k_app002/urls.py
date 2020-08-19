from django.urls import path
from . import views
# from django.conf.urls import url
# from .views import HelloView

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    


    # url(r'', HelloView.as_view(), name='index'),
    
    # path('', views.index, name='index'),
    # path('<int:id>/<nickname>/', views.index, name='index'),
    # path('next', views.next, name='next'),
    # path('form', views.form, name='form'),
]