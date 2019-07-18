from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from main.models import Tutorial

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data["email"]
		if commit:
			user.save()
		return user


class TutorialForm(ModelForm):
	class Meta:
		model = Tutorial
		fields = ['tutorial_title', 'tutorial_publish', 'tutorial_content', 'tutorial_series', 'tutorial_slug']


