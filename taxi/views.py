from django.shortcuts import render

from taxi.models import Driver, Car, Manufacturer

from django.views.generic import ListView


def index(request):
    """View function for the home page of the site."""

    context = {
        "num_drivers": Driver.objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
    }

    return render(request, "taxi/index.html", context=context)


class ManufacturerListView(ListView):
    model = Manufacturer
    queryset = Manufacturer.objects.all().order_by("name")
    paginate_by = 5


class CarListView(ListView):
    model = Car
    queryset = Car.objects.select_related("manufacturer").all()
    paginate_by = 5


class CarDetailView(ListView):
    model = Car


class DriverListView(ListView):
    model = Driver
    paginate_by = 5


class DriverDetailView(ListView):
    model = Driver
    queryset = Driver.objects.prefetch_related("car_set__manufacturer")
