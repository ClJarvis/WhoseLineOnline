from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Suggestion 
from .forms import SuggestionForm

####STOP TRY slide 39


def index(request):
		suggestions = Suggestion.objects.all()
		form = SuggestionForm()
		return render(request, 'index.html', {'suggestions': suggestions, 'form': form})

# def result(request):
#		return render(request, 'result.html', {'suggestion': suggestions})
'''
class Suggestion:
	def __init__(self, famePerson, place, weapon, guardian, audience):
		self.famePerson = famePerson
		self.place = place
		self.weapon = weapon
		self.guardian = guardian
		self.audience = audience


suggestions = [
	Suggestion('Batman', 'Tokyo', 'notebook', 'donkey', 'BigFan001'),
	Suggestion('Eric Clapton', 'Kroger', 'candlestick', 'Frodo Baggins', 'Buddy2020'),
	Suggestion('The Queen', 'CVS', 'a book', 'a fly', 'Joey')
	]
'''
def post_suggestion(request):
	form = SuggestionForm(request.POST)
	if form.is_valid():
		suggestion = Suggestion(famePerson = form.cleaned_data['famePerson'],
								place = form.cleaned_data['place'],
								weapon = form.cleaned_data['weapon'],
								guardian = form.cleaned_data['guardian'],
								audience = form.cleaned_data['audience'])
		suggestion.save()
	return HttpResponseRedirect('/')

def result(request):
		suggestions = Suggestion.objects.all()
		form = SuggestionForm()
		return render(request, 'result.html', { 'suggestions' : suggestions, 'form' : form })

def thanks(request):
		suggestions = Suggestion.objects.all()
		form = SuggestionForm()
		return render(request, 'thanks.html', { 'suggestions' : suggestions, 'form' : form })

	
