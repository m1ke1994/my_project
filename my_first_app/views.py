from django.shortcuts import render, get_object_or_404
from my_first_app.models import Аpartments  # Поменяйте "Apartments" на "Аpartments"
from orders.forms import OrderForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from my_first_app.forms import ApartamentsFilterForms




def my_first_app_list(request):
    apartments = Аpartments.objects.all()
    form=ApartamentsFilterForms(request.GET)
    if form.is_valid():
        if form.cleaned_data["min_price"]:
            apartments=apartments.filter(price__gte=form.cleaned_data["min_price"])
            if form.cleaned_data["max_price"]:
                apartments=apartments.filter(price__lte=form.cleaned_data["max_price"])

    return render(request, "my_first_app/my_first_app_list.html", {"apartments": apartments,"form":form})



""" def my_first_app_detail(request, apart_id):
    form=OrderForm(request.POST or None)
    if request.method=="POST":
    
      if form.is_valid():
          form.save
    apart = get_object_or_404(Аpartments, id=apart_id)
    return render(request, "my_first_app/my_first_app_detail.html", {"apart": apart,"form":form})
    
 """




def my_first_app_detail(request, apart_id):
    apart = get_object_or_404(Аpartments, id=apart_id)
    form = OrderForm(request.POST or None, initial={"apart": apart})
    
    if request.method == "POST":
        if form.is_valid():
            form.save()
            url=reverse("apartament", kwargs={"apart_id": apart.id})
            return HttpResponseRedirect(f"{url}?sent=1")
    
    return render(request, "my_first_app/my_first_app_detail.html",
                   {"apart": apart,
                     "form": form,
                     "sent":request.GET.get("sent")
                     })




def my_first_app_company(request):
    return render(request, "my_first_app/my_first_app_company.html")