from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import home, contact

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts_hub.urls')),
    path('units/', include('units_center.urls')),
    path('bookings/', include('booking_flow.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
