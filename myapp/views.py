from django.shortcuts import render
import pyshorteners

# Create your views here.
def home(request):
    url = ""
    short_url = ""
    if request.method == "POST":
        url = request.POST.get('url')
        s = pyshorteners.Shortener()
        short_url = s.tinyurl.short(url)
        print(short_url)
    context = {
     'url' : url,
     'short_url' : short_url
    }
    return render(request,template_name='index.html', context=context)
