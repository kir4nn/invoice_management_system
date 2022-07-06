from django import forms
from .models import Inventory

class InventoryForm(forms.ModelForm):
	class Meta:
		model = Inventory
		fields = ['product_number','product','title','amount']

	def clean_product_number(self):
		product_number = self.cleaned_data.get('product_number')
		if not product_number:
			raise forms.ValidationError('This field is required')
		return product_number

	def clean_product(self):
		product = self.cleaned_data.get('product')
		if not product:
			raise forms.ValidationError('This field is required')
		return product

	def clean_title(self):
		title = self.cleaned_data.get('title')
		if not title:
			raise forms.ValidationError('This field is required')
		return title

	def clean_amount(self):
		amount = self.cleaned_data.get('amount')
		if not amount:
			raise forms.ValidationError('This field is required')
		return amount

class InventorySearchForm(forms.ModelForm):
	class Meta:
		model = Inventory
		fields = ['product_number', 'title']

class InventoryUpdateForm(forms.ModelForm):
	class Meta:
		model = Inventory
		fields = ['product_number','product','title','amount']

	def clean_product_number(self):
		product_number = self.cleaned_data.get('product_number')
		if not product_number:
			raise forms.ValidationError('This field is required')
		return product_number

	def clean_product(self):
		product = self.cleaned_data.get('product')
		if not product:
			raise forms.ValidationError('This field is required')
		return product

	def clean_title(self):
		title = self.cleaned_data.get('title')
		if not title:
			raise forms.ValidationError('This field is required')
		return title

	def clean_amount(self):
		amount = self.cleaned_data.get('amount')
		if not amount:
			raise forms.ValidationError('This field is required')
		return amount
