from django.shortcuts import render
from home.models import *
from .forms import ContactECD



# --------------- VIEW DA PÁGINA INICIAL ------------------# 


def index(request):
    
    banners = Banner.objects.all()
    courses = Course.objects.all()
    professors = Professor.objects.all()
    disciplines = Discipline.objects.all()
    templates = Template.objects.all()
    links = Link.objects.all()
    contacts = Contact.objects.all()
    
    
    context = {
        'banners': banners, 
        'courses': courses,
        'professors': professors,
        'disciplines': disciplines,
        'templates': templates,
        'links': links,
        'contacts': contacts,
    }
    
    if request.method == 'POST': 
        form = ContactECD(request.POST or None)
        if form.is_valid():
            context['is_valid'] = True
            form.send_mail()
            form = ContactECD()	

    else:
        form = ContactECD()
    context ['form'] = form


    return render(request, 'index.html', context)
 



# --------------- VIEW DA PÁGINA DISCIPLINA ------------------# 



def disciplinas(request):
    
    infos = Infos.objects.all()
    references = Reference.objects.all()
    contacts = Contact.objects.all()
    
    context = {
        'infos': infos,
        'references': references,
        'contacts': contacts,
    }
    
    if request.method == 'POST': 

    	form = ContactECD(request.POST, request.FILES)
    	if form.is_valid():
    		context['is_valid'] = True
    		form.send_mail()
    		
    else:
    	form = ContactECD()
        
    context ['form'] = form
    return render(request, 'disciplinas.html', context)
    
