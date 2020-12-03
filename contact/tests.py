from django.test import TestCase
from contact.models import Contact
from django.urls import reverse

class ContactTestCase(TestCase):
	
	def setUp(self):
		Contact.objects.create(first_name = 'Ayotunde', last_name = "Okunubi", address = "Any address", phone = "09086746433")

	def test_contactHasPhone(self):
		contact = Contact.objects.get(first_name = 'Ayotunde')
		self.assertEqual(contact.hasPhone(), True)

class ContactListViewTests(TestCase):

	def test_noContact(self):
		"""in case there sre no contacts, these should return a string containing, "you do not hava any conacts yet",
		and the context dictionary should return an empty list. The status code should also be 200
		bcos the page loads successfully"""
		response = self.client.get(reverse('contact:index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "You do not have any contacts yet")
		self.assertQuerysetEqual(response.context['contacts']['allContact'],[])

	def test_displayMultipleContacts(self):
		contact1 = Contact.objects.create(first_name = 'Ayotunde', last_name = "Okunubi", address = "Any address", phone = "09086746433")	
		contact1 = Contact.objects.create(first_name = 'Anuoluwapo', last_name = "Okunubi", address = "Any address", phone = "09084546433")
		response = self.client.get(reverse('contact:index'))
		self.assertQuerysetEqual(response.context['contacts']['allContact'], ['<Contact: Anuoluwapo>', '<Contact: Ayotunde>'])

	def test_displaySIngleContact(self):
		contact1 = Contact.objects.create(first_name = 'Ayotunde', last_name = "Okunubi", address = "Any address", phone = "09086746433")	
		response = self.client.get(reverse('contact:index'))
		self.assertQuerysetEqual(response.context['contacts']['allContact'], ['<Contact: Ayotunde>'])

class AddContactTest(TestCase):

	def test_postDataWorking(self):
		response = self.client.post(reverse('contact:addContact'), {'first_name':'Ayotunde', 'last_name':'Okunubi', 'address':'56, Okun Street', 'phone':'09087678564'})
		self.assertEqual(response.status_code, 302)



