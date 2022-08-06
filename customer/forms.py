from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = ['customer_id','name','ph_no', 'email']

	def clean_customer_id(self):
		customer_id = self.cleaned_data.get('customer_id')
		if not customer_id:
			raise forms.ValidationError('This field is required')
		return customer_id

	def clean_name(self):
		name = self.cleaned_data.get('name')
		if not name:
			raise forms.ValidationError('This field is required')
		return name

	def clean_ph_no(self):
		ph_no = self.cleaned_data.get('ph_no')
		if not ph_no:
			raise forms.ValidationError('This field is required')
		return ph_no

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if not email:
			raise forms.ValidationError('This field is required')
		return email

class CustomerSearchForm(forms.Form):
	customer_id = forms.CharField(max_length=100, required=False)
	name = forms.CharField(max_length=100, required=False)
	class Meta:
		model = Customer
		fields = ['customer_id', 'name']

class CustomerUpdateForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = ['customer_id', 'name', 'ph_no', 'email']

	def clean_customer_id(self):
		customer_id = self.cleaned_data.get('customer_id')
		if not customer_id:
			raise forms.ValidationError('This field is required')
		return customer_id

	def clean_name(self):
		name = self.cleaned_data.get('name')
		if not name:
			raise forms.ValidationError('This field is required')
		return name

	def clean_ph_no(self):
		ph_no = self.cleaned_data.get('ph_no')
		if not ph_no:
			raise forms.ValidationError('This field is required')
		return ph_no

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if not email:
			raise forms.ValidationError('This field is required')
		return email
