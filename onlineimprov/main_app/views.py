from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Suggestion 
from .forms import SuggestionForm
from django.urls import reverse


def index(request):
		suggestions = Suggestion.objects.all()
		form = SuggestionForm()
		return render(request, 'index.html', {'suggestions': suggestions, 'form': form})

def post_suggestion(request):
	#breakpoint()
	form = SuggestionForm(request.POST)
	if form.is_valid():
		suggestion = Suggestion(famePerson = form.cleaned_data['famePerson'],
								place = form.cleaned_data['place'],
								weapon = form.cleaned_data['weapon'],
								guardian = form.cleaned_data['guardian'],
								audience = form.cleaned_data['audience'])
		suggestion.save()
	return HttpResponseRedirect(reverse("thanks"))

def result(request):
		suggestions = Suggestion.objects.all()
		form = SuggestionForm()
		return render(request, 'result.html', { 'suggestions' : suggestions, 'form' : form })

def thanks(request):
		suggestions = Suggestion.objects.all()
		form = SuggestionForm()
		return render(request, 'thanks.html', { 'suggestions' : suggestions, 'form' : form })

	
