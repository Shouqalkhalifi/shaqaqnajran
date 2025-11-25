from django.shortcuts import render


def units_collections(request):
    # صفحة قائمة الوحدات (كروت الوحدات)
    return render(request, "units_center/collections.html")


def unit_detail(request, unit_id):
    # صفحة تفاصيل وحدة واحدة (تصميم شبيه بصفحات Airbnb)
    # حالياً البيانات ثابتة وتجريبية، وسيتم ربطها بالموديل Unit لاحقاً.
    return render(request, "units_center/detail.html", {"unit_id": unit_id})
