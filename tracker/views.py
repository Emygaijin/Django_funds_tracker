from django.shortcuts import render, redirect
from .models import Institutions
from django.shortcuts import render,redirect, get_object_or_404
from .forms import FormOne
from django.db.models import Count
from django.db.models import Sum
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request, 'index.html')



def update(request, name):
    data = get_object_or_404(Institutions, name=name)
    form1 = FormOne(instance=data)

    if request.method == 'POST':
        form1 = FormOne(request.POST, instance=data)

        if form1.is_valid():
            form1.save()
            return redirect('details', name=name)

    # This block ensures that the form is rendered when the page is requested with a GET request.
    return render(request, 'update.html', {'data': data, 'form1': form1})



def institution(request):
    data = Institutions.objects.all()
    return render(request, 'institutions.html', {'data':data})

def details(request, name):
    data = get_object_or_404(Institutions, name=name)
    return render(request, 'details.html', {'data': data})


def client_institution(request):
    data = Institutions.objects.all()
    return render(request, 'client_institutions.html', {'data': data})


def institution_total(request, institution_name):
    # Filter instead of get
    institutions_instances = Institutions.objects.filter(institution__iexact=institution_name)

    # Calculate total for all instances including income
    total_for_institution = institutions_instances.aggregate(total=Sum('total'))['total']

    # Calculate sum of all income for the institution
    sum_of_income = institutions_instances.aggregate(income_sum=Sum('income'))['income_sum']

    context = {
        'institution_instance': institutions_instances.first(),  # Just get the first instance for other context data
        'total_for_institution': total_for_institution,
        'sum_of_income': sum_of_income,
    }

    return render(request, 'institution_total.html', context)


def choice(request):
    unique_institutions = Institutions.objects.values('institution').annotate(total=Count('institution'))

    return render(request, 'choice.html', {'unique_institutions': unique_institutions})


def income_total(request):
    # Aggregate the sum of income across all institutions excluding None values
    total_income = Institutions.objects.exclude(income__isnull=True).aggregate(Sum('income'))['income__sum']

    context = {
        'total_income': total_income,
    }

    return render(request, 'income_total.html', context)


