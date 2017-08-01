from reportlab.pdfgen import canvas
from django.http import HttpResponseRedirect
from django.template import loader, RequestContext
from shutil import copyfile
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt

from .models import WagonDrawing

@csrf_exempt
def index(request):
	if request.method == 'POST':
		cid = request.POST.get('cid')
		wagtemp = WagonDrawing.objects.filter(iid=cid)
		oktemp = WagonDrawing.objects.filter(iid=cid)
		for e in wagtemp:
			wagnumber = e.wagon_number
		for f in oktemp:
			okdate = f.ok_date
		return HttpResponseRedirect('/commission/' + str(cid) + '/')
		#return HttpResponseRedirect('/commission/wagon/' + str(okdate) + '/' + str(wagnumber) + '/')
	else:	
		ok_date_list = WagonDrawing.objects.values('ok_date').distinct().order_by('ok_date')
		context = {'ok_date_list': ok_date_list}
		return render(request, 'commission/index.html', context)

def choosewagon(request, okdate):
	wagond_list = WagonDrawing.objects.filter(ok_date=okdate).values('wagon_number').distinct().order_by('wagon_number')
	context = {'wagond_list': wagond_list, 'okdate' : okdate}
	return render(request, 'commission/wagonlist.html', context)

def wagon(request, wagnumber, okdate):
	draw_list = WagonDrawing.objects.filter(ok_date=okdate, wagon_number=wagnumber).order_by('-link')
	context = {'draw_list': draw_list, 'okdate' : okdate}
	return render(request, 'commission/drawlist.html', context)

def product(request, pid):
	draw_list = WagonDrawing.objects.filter(iid = pid).order_by('-link')
	for drawing in draw_list:
		okdate = str(drawing.ok_date)
	context = {'draw_list': draw_list, 'okdate': okdate}
	return render(request, 'commission/productdrawing.html', context)
	
	
	
#def index(request):
	#ok_date_list = WagonDrawing.objects.values('ok_date').distinct()
	#context = {'ok_date_list': ok_date_list}
	#return render(request, 'commission/index.html', context)
