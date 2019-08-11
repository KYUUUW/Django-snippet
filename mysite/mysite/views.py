from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def echo(req):
    x = req.POST['x']
    return HttpResponse(x)
