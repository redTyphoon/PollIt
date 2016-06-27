from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response
from django.template import RequestContext
from .forms import UserForm
from django.http import HttpResponseRedirect,HttpResponse

def register(request):
    context = RequestContext(request)
    #
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
	        user = user_form.save()
	        user.set_password(user.password)
	        user.save()
	        registered = True
        else:
        	print(user_form.errors)
    else:
        user_form = UserForm()
    return render_to_response(
            'polls/register.html',
            {'user_form': user_form, 'registered': registered},
            context)


def user_login(request):
	context = RequestContext(request)
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/polls/')
			else:
				return HttpResponse("Your Poll It account is disabled.")
		else:
			print("Invalid login details: {0}, {1}".format(username, password))
			return HttpResponse("Invalid login details supplied.Login Again")
	else:
		return render_to_response('polls/login.html', {}, context)



