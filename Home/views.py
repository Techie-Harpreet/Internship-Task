from django.shortcuts import render
import datetime
from quote import quote
from .models import Data
from django.contrib import messages
from django.http import HttpResponseRedirect


def Home(request):

    return render(request, "pages/index.html")


def dynamic_content(request):
    current_datetime = datetime.datetime.now()

    random_quote = quote('motivation',limit=1)
    

    for i in range(len(random_quote)):
        # print(random_quote[i]['quote'])
        random_quote_data = random_quote[i]['quote']
    print(random_quote_data)
    context = {
        'current_datetime': current_datetime,
        'random_quote_data': random_quote_data,
    }
    return render(request, 'pages/dynamic_content.html', context)


def Add_Form_Data(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phoneno = request.POST['phoneno']
        address = request.POST['address']

        if len(phoneno) != 10:
            messages.error(request, 'Phone no must be 10 digit')
        else:
            data_obj = Data(name=name, email=email, phoneno=phoneno, address=address)
            data_obj.save()
            messages.success(request, 'Details save successfully')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        

    return render(request, "pages/form.html")


def ShowData(request):
    form_data =  Data.objects.all()
    context = {
        'form_data' : form_data
    }
    return render(request, "pages/show-form-data.html", context)