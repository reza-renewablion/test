from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
# from django.core.urlresolvers import reverse
# from django.shortcuts import render_to_response
# from django.shortcuts import render_to_response,RequestContext

# Create your views here.


def SignUpcontroller(request):
    return render(request, 'SignUpPage.html')


def SignIncontroller(request):
    return render(request, 'SignInPage.html')