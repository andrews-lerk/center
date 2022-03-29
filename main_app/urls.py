from django.urls import path
from .views import main_page, booking, booking_personal_info, booking_complete, view_gallery

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', main_page, name='home'),
    path('book/', booking, name='booking'),
    path('book/personal-info/', booking_personal_info, name='booking_personal_info'),
    path('book/complete/', booking_complete, name='booking_complete'),
    path('gallery/', view_gallery, name='gallery')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)