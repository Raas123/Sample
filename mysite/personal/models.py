from django.db import models


# Create your models here.

class CustomerInfo(models.Model):
	firstName = models.CharField(max_length=100)
	
	OCCUPATION_TYPE_CHOICES =(
		('salaried',"Salaried"),
		('self-employed business',"Self-Employed Business"),
		('self-employed professional',"Self-Employed Professional"),
		)
	occupation_type = models.CharField(
		max_length=15,
		choices = OCCUPATION_TYPE_CHOICES,
		blank=True
		)
	
	annual_income= models.IntegerField(default=False)
	pincode = models.IntegerField(default=False)
	
	
	CARD_TYPE_CHOICES =(
		('hdfc',"HDFC"),
		('icici',"ICICI"),
		('other',"Other"),
		)
	card_list = models.CharField(
		max_length=15,
		choices = CARD_TYPE_CHOICES,
		blank=True
		)
	
	is_credit_card = models.BooleanField(default=False)
	
	mobile = models.IntegerField()
	lastname = models.CharField(max_length=100,default=True)
	
	
	
	
	
	def __str__(self):
		return self.firstName

class OfferInfo(models.Model):
	
	offerName = models.CharField(max_length=100,default='Offer')
	imageLocation = models.CharField(max_length=100)
	is_Travel = models.BooleanField(default=False)
	is_Airport_Lounge = models.BooleanField(default=False)
	is_Shopping = models.BooleanField(default=False)
	is_Dining = models.BooleanField(default=False)
	is_Movies = models.BooleanField(default=False)
	is_Fuel = models.BooleanField(default=False)
	
	first_year_fees= models.IntegerField(default=False)
	reward_values = models.IntegerField(default=False)
	chance_of_Approval = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
	
	'''def __str__(self):
		return self.offerName'''
		
class BookedInfo(models.Model):
	
	firstName = models.CharField(max_length=100,default='Test')
	
	OCCUPATION_TYPE_CHOICES =(
		('salaried',"Salaried"),
		('self-employed business',"Self-Employed Business"),
		('self-employed professional',"Self-Employed Professional"),
		)
	occupation_type = models.CharField(
		max_length=15,
		choices = OCCUPATION_TYPE_CHOICES,
		blank=True
		)
	
	annual_income= models.IntegerField(default=False)
	pincode = models.IntegerField(default=False)
	email = models.CharField(max_length=100,blank=True)
	mobile = models.IntegerField(default=False)
	
	COMPANY_CHOICES =(
		('interra',"Interra"),
		('test_IT',"Test Company"),
		('digital_company',"Digital Company"),
		)
	company_name = models.CharField(
		max_length=15,
		choices = COMPANY_CHOICES,
		blank=True
		)
		
	offer_id= models.IntegerField(default=False)
	#company_name = 
	
	
	
		
	
	
	
	
	
	
