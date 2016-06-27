from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, render
from .models import Poll, Choice, Votes, PollForm, ChoiceForm

def home(request):
	polls = Poll.objects.all().order_by('date')
	return render_to_response('poll/home.html', 
			{'user': request.user,
			 'polls':polls}, 
		context_instance = RequestContext(request),)

def view_poll(request, poll_id):
	poll = Poll.objects.get(id=poll_id)
	choices = poll.choice_set.all()
	return render_to_response('poll/info.html', 
		{'poll': poll, 'choices':choices,'share':request.build_absolute_uri(request.path)}, 
		context_instance = RequestContext(request),)

def add(request):
	if request.method == 'POST':
		form = PollForm(request.POST)
		import pdb;pdb.set_trace()
		if form.is_valid():
			form.fields['publisher']=request.user.username
			form.save() 
			return HttpResponseRedirect(reverse('home'))
	else:
	    form = PollForm()
	return render_to_response ('poll/poll.html', 
		{'form': form,'user': request.user,}, 
		context_instance = RequestContext(request),)

def add_choice(request, poll_id):
    poll = Poll.objects.get(id = poll_id)
    if request.method =='POST':
        form = ChoiceForm(request.POST)
        if form.is_valid():
            add_poll = form.save(commit = False)
            add_poll.poll = poll
            add_poll.vote = 0
            add_poll.save()         
            form.save()
        return HttpResponseRedirect('../')
    else: 
        form = ChoiceForm()
    return render_to_response ('poll/choice.html', {'form': form, 'poll_id': poll_id,}, 
                            context_instance = RequestContext(request),)

def view_polls(request):
    poll_query = Poll.objects.all().order_by('date')
    return render_to_response('poll/vote.html',{'poll_query': poll_query, })


def add_vote(request, poll_id):
	poll = Poll.objects.get(id=poll_id) 
	choice = Choice.objects.filter(poll=poll_id).order_by('id')
	if request.method == 'POST':
		if request.user.is_authenticated():
		    vote = request.POST.get('choice')
		    if vote:
		        vote = Choice.objects.get(id=vote)  
		        v = Votes(poll=poll, choiceVote = vote)
		        v.save()
		        return HttpResponseRedirect('../')
		else:
			return HttpResponseRedirect('../../../pollit/login')
	return render_to_response('poll/votes_add.html',
		{'choice': choice, 'poll': poll,}, 
		context_instance=RequestContext(request))

def view_results(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    choices = poll.choice_set.all()
    return render_to_response('poll/info.html', vars())