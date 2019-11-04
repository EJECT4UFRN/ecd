from django import forms
from django.core.mail import send_mail
from django.conf import settings 
from . import views




class ContactECD(forms.Form):
	name = forms.CharField(label = 'Nome', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome', 'required':'required'}))
	email = forms.EmailField(label = 'E-mail', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'seuemail@gmail.com', 'required':'required', 'type': 'email'}) )
	about = forms.ChoiceField(choices = ABOUT_CHOICES, label="Assunto", widget=forms.RadioSelect) 
	phone = forms.CharField(label = 'Telefone', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Telefone', 'required':'required'}))
    message = forms.CharField(label='Mensagem', widget=forms.Textarea(attrs={'class':'form-control', 'rows': 5, 'cols': 20 ,'placeholder':'Escreva sua mensagem', 'required':'required'}))
	document = forms.Field(label='Selecione um arquivo', widget=forms.FileInput)
	def send_mail(self):

		message = '--------------------------------------------------------------------------------\n'
		message += ' [SITE] Contato do Site ECD \n'
		message += '--------------------------------------------------------------------------------\n'
		message += 'NOME: %(name)s \n'
		message += 'E-MAIL: %(email)s \n'
        message += 'TELEFONE: %(phone)s \n'
		message += 'MENSAGEM: %(message)s \n'

		context = {
			'name': self.cleaned_data['name'],
			'email': self.cleaned_data['email'],
            'phone': self.cleaned_data['phone'],
			'about': self.cleaned_data['about'],
			'message': self.cleaned_data['message'],
		}
		subject = self.cleaned_data['about']
		
		message = message % context
		
		send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL])
