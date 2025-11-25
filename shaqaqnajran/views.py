from django.shortcuts import render


def home(request):
    selected_unit_id = request.GET.get("unit_id")

    context = {
        "selected_unit_id": selected_unit_id,
        "checkin": request.GET.get("checkin", ""),
        "checkout": request.GET.get("checkout", ""),
        "adults": request.GET.get("adults", ""),
        "children": request.GET.get("children", ""),
    }

    return render(request, "home.html", context)


def contact(request):
    return render(request, "contact.html")
