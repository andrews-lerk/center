from django.urls import path
from .views import (main_page, booking, booking_personal_info,
                    booking_complete, view_gallery, view_doctors, view_tourism, book_osteopat, book_day,
                    book_osteopat_complete,
                    book_day_complete, book_day_mini, view_rules, booking_mini, view_rooms, view_procedures, view_offer,
                    view_smi,
                    book_health_back, book_health_tourism_3, book_health_tourism_5, book_health_tourism_7,
                    book_health_tourism_10)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', main_page, name='home'),
    path('book/', booking, name='booking'),
    path('book-mini/', booking_mini, name='booking-mini'),
    path('book/personal-info/', booking_personal_info, name='booking_personal_info'),
    path('book/complete/', booking_complete, name='booking_complete'),
    path('gallery/', view_gallery, name='gallery'),
    path('specialists/', view_doctors, name='doctors'),
    path('tourism-and-dosug/', view_tourism, name='tourism'),
    path('book-osteopat/', book_osteopat, name='book-osteopat'),
    path('book-day/', book_day, name='book-day'),
    path('book-osteopat-complete/', book_osteopat_complete, name='osteopat-complete'),
    path('book-day-complete/', book_day_complete, name='day-complete'),
    path('book-day-mini/', book_day_mini, name='book-day-mini'),
    path('rules/', view_rules, name='rules'),
    path('rooms/', view_rooms, name='rooms'),
    path('procedures/', view_procedures, name='procedures'),
    path('offer/', view_offer, name='offer'),
    path('smi/', view_smi, name='smi'),
    path('health-back/', book_health_back, name='health-back'),
    path('health-tourism-3/', book_health_tourism_3, name='health-tourism-3'),
    path('health-tourism-5/', book_health_tourism_5, name='health-tourism-5'),
    path('health-tourism-7/', book_health_tourism_7, name='health-tourism-7'),
    path('health-tourism-10/', book_health_tourism_10, name='health-tourism-10'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
