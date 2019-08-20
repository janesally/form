from django.urls import path

from . import views

app_name = 'forms'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:form_id>/fillForm', views.fillForm, name='fillForm'),
    path('help', views.help, name='help'),
    path('<int:form_id>/submit', views.submit, name='submit')
]
