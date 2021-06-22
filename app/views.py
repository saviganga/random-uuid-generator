from django.shortcuts import render
from .models import UUIDModel
import uuid


# Create your views here.
def home(request):

    ''' displays timestamp and uuid generated '''

    # on request, create a new uuid object
    UUIDModel.objects.create(UUID=uuid.uuid4())

    template = 'app/home.html'
    uuids = UUIDModel.objects.all()
    context = {'uuids': uuids}

    return render(request, template, context)
