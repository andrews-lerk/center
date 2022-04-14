from django.urls import path
from .views import main_page, booking, booking_personal_info, \
    booking_complete, view_gallery, view_doctors, view_tourism, book_osteopat, book_day

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', main_page, name='home'),
    path('book/', booking, name='booking'),
    path('book/personal-info/', booking_personal_info, name='booking_personal_info'),
    path('book/complete/', booking_complete, name='booking_complete'),
    path('gallery/', view_gallery, name='gallery'),
    path('specialists/', view_doctors, name='doctors'),
    path('tourism-and-dosug/', view_tourism, name='tourism'),
    path('book-osteopat/', book_osteopat, name='book-osteopat'),
    path('book-day/', book_day, name='book-day')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)