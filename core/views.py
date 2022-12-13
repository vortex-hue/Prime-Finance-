from django.shortcuts import render
from user_core.models import Site, InvestmentPlan

# Create your views here.

def about(request):
    try:
        site = Site.objects.get(pk=1)
    except Site.DoesNotExist:
        site = Site.objects.create(pk=1)
        site.save()
    
    context ={
        'site':site
    }
    return render(request,'about.html',context)
                
def banner(request):
    try:
        site = Site.objects.get(pk=1)
    except Site.DoesNotExist:
        site = Site.objects.create(pk=1)
        site.save()
    
    context ={
        'site':site
    }
    return render(request,'banner.html',context)
                
def contact(request):
    try:
        site = Site.objects.get(pk=1)
    except Site.DoesNotExist:
        site = Site.objects.create(pk=1)
        site.save()
    
    context ={
        'site':site
    }
    return render(request,'contact.html',context)
                
def faq(request):
    try:
        site = Site.objects.get(pk=1)
    except Site.DoesNotExist:
        site = Site.objects.create(pk=1)
        site.save()
    
    context ={
        'site':site
    }
    return render(request,'faq.html',context)
                
                
def index(request):
    try:
        site = Site.objects.get(pk=1)
    except Site.DoesNotExist:
        site = Site.objects.create(pk=1)
        site.save()
    plans = InvestmentPlan.objects.all()
    context ={
        'site':site,
        'plans':plans
    }
    return render(request,'index.html',context)
                
                
def payment(request):
    try:
        site = Site.objects.get(pk=1)
    except Site.DoesNotExist:
        site = Site.objects.create(pk=1)
        site.save()
    
    context ={
        'site':site
    }
    return render(request,'payment.html',context)
                
def plans(request):
    try:
        site = Site.objects.get(pk=1)
    except Site.DoesNotExist:
        site = Site.objects.create(pk=1)
        site.save()
    plans = InvestmentPlan.objects.all()
    context ={
        'site':site,
        'plans':plans
    }
    return render(request,'plans.html',context)
                
                
def terms(request):
    try:
        site = Site.objects.get(pk=1)
    except Site.DoesNotExist:
        site = Site.objects.create(pk=1)
        site.save()
    
    context ={
        'site':site
    }
    return render(request,'terms.html',context)
                #views created