from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
    # template = loader.get_template('myfirst.html')
    # return HttpResponse(template.render())
    
    mymembers = Member.objects.all().values() # get all members from model
    template = loader.get_template('all_members.html')
    # pass the members to the template
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))