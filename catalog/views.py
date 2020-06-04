from django.shortcuts import render

# Create your views here.

from catalog.models import Measure, User, UsersMeasurement

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_measures = Measure.objects.all().count()
    num_measurements = UsersMeasurement.objects.all().count()
    
    # Available books (status = 'в')
    num_measurements_perform = UsersMeasurement.objects.filter(status__exact='p').count()
    
    # The 'all()' is implied by default.    
    num_users = User.objects.count()
    
    context = {
        'num_measures': num_measures,
        'num_measurements': num_measurements,
        'num_measurements_perform': num_measurements_perform,
        'num_users': num_users,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic

class MeasureListView(generic.ListView):
    model = Measure

class MeasureDetailView(generic.DetailView):
    model = Measure