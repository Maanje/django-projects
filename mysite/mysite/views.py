from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import datetime
# Alternative way to render page
from django.shortcuts import render_to_response


def current_datetime(request):
	current_date=datetime.datetime.now()
	return render_to_response('dateapp/current_datetime.html',locals())

def hours_ahead(request,offset):
	offset=int(offset)
	dt=datetime.datetime.now()+datetime.timedelta(hours=offset)
	t=get_template('dateapp/hours_ahead.html')		
	html=t.render({'current_date':dt,'hour_offset':offset}) 
	return HttpResponse(html)
