# Create your views here.
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from forms import LightForm
from article.models import Light
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.contrib.auth import authenticate
import subprocess



@login_required
def articles(request):
			
		language = 'en-us'
		session_language = 'en-us'
		if 'lang' in request.COOKIES:
			language = request.COOKIES['lang']
		args = {}
		args.update(csrf(request))
		args['language'] = language
		args['views'] = Light.objects.all()
		args['session_language'] = session_language

		return render_to_response('articles.html', args,)
		
@login_required
def article(request, article_id=1):

	args = {}
	args.update(csrf(request))
	args['article'] = Light.objects.get(id = article_id )
	#args['form'] = form
	
	
	form = LightForm()
	args['form'] = form
	return render_to_response('article.html',args)

def language(request, language='en-us'):
	response = HttpResponse("setting language to %s" % language)
	response.set_cookie('lang',language)
	return response
	

def buttonPush(request):
	if request.method == "POST":
		article_id = request.POST['artID']
		a = Light.objects.get(id=article_id)
		buttonValue = request.POST['search_text']
		if buttonValue == 'True':
			p = subprocess.Popen(['sudo','/home/pi/on.sh'])
			a.onOff = True
			a.save()
			html = "<html><body>Light is now on</body></html>"

		else:
			p = subprocess.Popen(['sudo','/home/pi/off.sh'])
			a.onOff = False
			a.save()
			html = "<html><body>Light is now off</body></html>"
		return HttpResponse(html)



@login_required
def about(request):
	args = {}
	args.update(csrf(request))
	return render_to_response('about.html',args)

@login_required
def contact(request):
	args = {}
	args.update(csrf(request))
	return render_to_response('contact.html',args)
