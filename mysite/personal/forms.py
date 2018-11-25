from django import forms
from .models import CustomerInfo,BookedInfo

# Create your tests here.
class CustomerInfoForm (forms.ModelForm):
	class Meta:
		model = CustomerInfo
		fields = ['firstName', 'occupation_type', 'annual_income', 'pincode','card_list','is_credit_card','mobile','lastname']

class BookedInfoForm (forms.ModelForm):
	class Meta:
		model = BookedInfo
		fields = ['firstName','occupation_type', 'annual_income', 'pincode','email','mobile','company_name','offer_id']
