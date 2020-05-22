from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
	path('', views.ContactListView.as_view(), name = 'index'),
	path('addContact/', views.addContact, name ='addContact'),
	path('editContact/', views.editContact, name = 'editContact'),
	path('delContact/<int:id>/', views.delete, name = 'delete'),

]