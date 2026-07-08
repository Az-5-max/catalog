from django.shortcuts import render, get_object_or_404
from phones.models import Phone


def catalog(request):
    sort_param = request.GET.get('sort')
    phones = Phone.objects.all()

    if sort_param == 'name':
        phones = phones.order_by('name')
    elif sort_param == 'min_price':
        phones = phones.order_by('price')
    elif sort_param == 'max_price':
        phones = phones.order_by('-price')

    return render(request, 'catalog.html', {'phones': phones})


def phone_detail(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    return render(request, 'phone_detail.html', {'phone': phone})
