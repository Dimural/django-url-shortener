

from django.shortcuts import render, redirect, get_object_or_404
from django.utils.timezone import now
from .models import ShortenedURL
from .forms import URLForm
import uuid #special import, this is to generate a unique id for each device. This was new for me I had no prior experience with this module
from django.utils.timezone import localtime

#this function assigns a unique id to each device using a session-based identifier
def get_device_id(request):
    """Assigns a unique ID to each device using a session-based identifier."""
    if not request.session.get('device_id'):
        request.session['device_id'] = str(uuid.uuid4()) 
    return request.session['device_id']


#this function is the home page of the website, it allows the user to input a url to be shortened
def home(request):
    form = URLForm()
    short_url = None
    device_id = get_device_id(request)  
    urls = ShortenedURL.objects.filter(device_id=device_id)  # Get all URLs created by this device

    for url in urls:
        if url.last_clicked:
            url.last_clicked = localtime(url.last_clicked) #convert to local timezone

    if request.method == 'POST': #when the form is submitted, the url is shortened and saved to the database
        form = URLForm(request.POST)
        if form.is_valid():
            short_url = form.save(commit=False)
            short_url.device_id = device_id  
            short_url.save()
            request.session['last_shortened_url'] = short_url.short_code  # Store it in session
            return redirect('home')

    #allow for the last shortened url to be displayed on the home page (i had a huge issue with this, the copy button was not appearing as it refreshed to the home page after a url was shortened. this code chunk fixes that)
    short_url_code = request.session.pop('last_shortened_url', None)  
    short_url = ShortenedURL.objects.filter(short_code=short_url_code).first() if short_url_code else None
    return render(request, 'shortener/home.html', {'form': form, 'short_url': short_url, 'urls': urls})

#this function redirects the user to the original url when the shortened url is clicked (crucial function)
def redirect_url(request, short_code):
    url_entry = ShortenedURL.objects.filter(short_code=short_code).first()
    if url_entry:
        url_entry.click_count += 1
        url_entry.last_clicked = now()
        url_entry.save()
        return redirect(url_entry.original_url)
    return render(request, 'shortener/home.html', {'error': 'URL not found'})

#this function allows for deletion of a shortened url from the database
def delete_url(request, short_code):
    url_entry = get_object_or_404(ShortenedURL, short_code=short_code)
    url_entry.delete()
    return redirect('home')
