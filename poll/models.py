from django.db import models
from django.forms import ModelForm 

class Poll(models.Model):
	question = models.CharField(max_length=255)
	date = models.DateTimeField(auto_now_add=True)
    
	def __str__(self):
		return self.question

class Choice(models.Model):
	poll = models.ForeignKey(Poll)
	choice = models.CharField(max_length=255)

class Votes(models.Model):
	poll = models.ForeignKey(Poll)
	choiceVote = models.ForeignKey(Choice)

class PollForm(ModelForm):
	class Meta:
		model = Poll
		fields = '__all__'

class ChoiceForm(ModelForm):
	class Meta:
		model = Choice
		fields = ('choice',)