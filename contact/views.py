from django.shortcuts import render, redirect, get_object_or_404
from . models import Contact
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from django.contrib import messages

class ContactListView(ListView):
	model = Contact
	template_name = 'contact/index.html'
	context_object_name = 'contacts'

	def get_queryset(self):
		queryset = {
			'allContact':Contact.objects.all().order_by('-date_added'),
			'contactCount':Contact.objects.all().count(),
		}
		return queryset

def addContact(request):
	if request.method == 'POST':
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		phone = request.POST.get('phone')
		address = request.POST.get('address')

		contact = Contact(first_name = first_name, last_name = last_name, address = address, phone = phone)
		contact.save()
		messages.success(request, 'Contact successfully added......')
		return redirect ('contact:index')

def editContact(request):
	contactId = request.GET.get('id')
	if request.method == 'POST':
		contact = get_object_or_404(Contact, id = contactId)
		contact.first_name = request.POST.get('first_name')
		contact.last_name = request.POST.get('last_name')
		contact.address = request.POST.get('address')
		contact.phone = request.POST.get('phone')
		contact.save()
		messages.success(request, 'Contact successfully updated')
		return redirect('contact:index')
	contact = get_object_or_404(Contact, id = contactId)
	return render(request, 'contact/editContact.html', {'contact':contact})


def delete(request, id):
	contact = get_object_or_404(Contact, id = id)
	contact.delete()
	messages.error(request, 'You\'ve successfully deleted this contact')
	return redirect('contact:index')





