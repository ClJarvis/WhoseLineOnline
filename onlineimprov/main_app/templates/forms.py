from django import forms

# Create your models here.
class SuggestionForm(forms.Form):
	famePerson = forms.CharField(label='Famous Person',max_length=100)
	place = forms.CharField(label='Place', max_length=100)
	weapon = forms.CharField(label='Weapon', max_length=100)
	guardian = forms.CharField(label='Guardian', max_length=100)
	audience = forms.CharField(label='Your Name', max_length=100)