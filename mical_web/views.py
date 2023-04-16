from django.shortcuts import render
from django.http import HttpResponseRedirect
from .form import WorkForm

def index(request):
    return render(request,'mical_web/index.html')


def get_request(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = WorkForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('mical_web/thank.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = WorkForm()

    return render(request, 'mical_web/index.html', {'form': form})