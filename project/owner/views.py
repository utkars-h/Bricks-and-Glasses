from django.shortcuts import render
from .models import Owner

# Create your views here.


def owner_detail_view(request):
    obj = Owner.objects.get(ownerID=1)
    # context = {
    #     'name': obj.oname,
    #     'contact': obj.contact
    # }

    context = {
        'object': obj
    }
    return render(request, 'Owner/details.html', context)
