from django.shortcuts import render, redirect
from decouple import config
import time, hashlib
from .models import short_url

def index(request):
    return render(request, 'index.html')

def submitShortUrl(request):
    if request.method == 'POST':
        # Get url from POST
        url = request.POST["url"]

        # Validate if url has value
        if not url:
            return redirect('/')

        # Hash function to convert url
        slug = hashlib.md5(url.encode('utf-8')).hexdigest()

        # Short url
        new_url = short_url(old=url, slug=slug, new=config('HOSTDOMAIN')+slug)

        # See if already hashed submitted url before store into db
        old_url = short_url.objects.filter(new=config('HOSTDOMAIN')+slug).values_list('old', flat=True).first()
        if not old_url:
            new_url.save()

        # List all submitted urls
        return redirect('/showurls')

def showUrls(request):
    # Get all the urls from database
    allurls = short_url.objects.all()

    # Pass all urls to template
    return render(request, 'showurls.html', {'urls': allurls})

def originalUrl(request,slug):
    slug = request.path
    new_url = config('HOSTDOMAIN')+slug[1:]
    old_url = short_url.objects.filter(new=new_url).values_list('old', flat=True).first()
    if old_url:
        print(old_url)
        return redirect(old_url)
