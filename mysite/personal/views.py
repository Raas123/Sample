from django.shortcuts import render, redirect
from .models import CustomerInfo
from .models import OfferInfo
from .forms import CustomerInfoForm,BookedInfoForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'personal/home.html')

def index1(request,list_id):
	form_booked = BookedInfoForm(request.POST or None, initial={'annual_income': request.session['annual_income'],'occupation_type': request.session['occupation_type'],'pincode': request.session['pincode'],'firstName': request.session['firstName'],'mobile': request.session['mobile'],'offer_id': list_id})
	#form_booked.fields['firstName'].initial = 'Agamya'
	if form_booked.is_valid():
		form_booked.save()
		return redirect('index')
	
	return render(request, 'personal/index1.html', {'form': form_booked})

def contact(request):
    return render(request, 'personal/basic.html', {'content':['If you would like to contact me, please email me','hskinsley@gmail.com']})
	
def creditcardenquiry(request):
	form = CustomerInfoForm(request.POST or None)
	#request.session['test'] = form.firstName
	request.session.modified = True
	if form.is_valid():
		request.session['firstName'] = form.cleaned_data['firstName']
		request.session['occupation_type'] = form.cleaned_data['occupation_type']
		request.session['annual_income'] = form.cleaned_data['annual_income']
		request.session['pincode'] = form.cleaned_data['pincode']
		request.session['mobile'] = form.cleaned_data['mobile']
		
		#test = form.firstName
		#data = request.POST.copy()
		
		form.save()
		user_info = form.save()
		 #form.cleaned_data['firstName']
		#context = {'form':form}
		return redirect('creditcardenquirylist')
		#return creditcardenquirylist(request)
		#return render_to_response('creditcardenquirylist.html', context_instance=RequestContext(request,{'form':form}))
		
	return render(request, 'personal/creditcardenquiry.html', {'form': form})
	
def creditcardenquirylist(request):
	#customeinfolists = CustomerInfo.objects.all()
	#return render(request, 'personal/creditcardenquirylist.html', {'customeinfolists':customeinfolists})
	#username = '999' #request.session['username']
	#test = request.session['test']
	
	offerinfolists = OfferInfo.objects.all()
	return render(request, 'personal/creditcardenquirylist.html', {'offerinfolists':offerinfolists})


def login1(request):
	#customeinfolists = CustomerInfo.objects.all()
	return render(request, 'personal/login.html')
	
def register(request):
	#customeinfolists = CustomerInfo.objects.all()
	if request.method =='POST':
		form = UserCreationForm(request.POST)
		
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username= username, password =password)
			login(request,user)
			return render(request,'landing.html')
	else:
		form = UserCreationForm()
			
	context = {'form':form}
	return render(request, 'registration/register.html', context) 
		
		
