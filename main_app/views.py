from django.shortcuts import render
from .models import *
from .forms import *
from datetime import datetime, date, time


def main_page(request):
    photos = MainPhotos.objects.all().first()
    course_photos = CoursesPhoto.objects.all().first()
    description = Description.objects.filter(active=True).first()
    context = {
        'photos': photos,
        'course_photos': course_photos,
        'description': description
    }
    return render(request, 'main_app/index.html', context)


def booking(request):
    form = DateForm
    if request.POST:
        form = DateForm(request.POST)
        if form.is_valid():
            lst_of_dates = form.cleaned_data['check_in_out'].split(' - ')
            adult = form.cleaned_data['adult']
            check_in = lst_of_dates[0]
            check_out = lst_of_dates[-1]
            context_post = {
                'check_in': check_in,
                'check_out': check_out,
                'adult': adult
            }
            return render(request, 'main_app/book_step_2.html', context_post)
    course = MainCourse.objects.all().first()
    context = {
        'form': form,
        'course': course
    }
    return render(request, 'main_app/book.html', context)


def booking_personal_info(request):
    check_in = request.POST['check_in']
    check_out = request.POST['check_out']
    adult = request.POST['adult']
    type = request.POST['type']
    if adult == '2':
        form = DuoPersonalInfoForm
    else:
        form = SinglePersonalInfoForm
    context = {
        'check_in': check_in,
        'check_out': check_out,
        'adult': adult,
        'type': type,
        'form': form
    }
    return render(request, 'main_app/book_step_3.html', context)


def booking_complete(request):
    check_in = request.POST['check_in']
    check_out = request.POST['check_out']
    adult = request.POST['adult']
    type = request.POST['type']
    if adult == '2':
        form = DuoPersonalInfoForm(request.POST)
    else:
        form = SinglePersonalInfoForm(request.POST)
    if form.is_valid():
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        birth_date = form.cleaned_data['birth_date']
        city = form.cleaned_data['city']
        if adult == '2':
            first_name2 = form.cleaned_data['first_name2']
            last_name2 = form.cleaned_data['last_name2']
            birth_date2 = form.cleaned_data['birth_date2']
            city2 = form.cleaned_data['city2']
        phone = form.cleaned_data['phone']
        email = form.cleaned_data['email']
        if adult == '2':
            order = Order.objects.create(
                check_in=datetime.strptime(check_in, "%d/%m/%Y"),
                check_out=datetime.strptime(check_out, "%d/%m/%Y"),
                room_type=type,
                clients_info=f'Имя: {first_name}, Фамилия: {last_name}, Дата рождения: {birth_date}, Город: {city}\n'
                             f'Имя: {first_name2}, Фамилия: {last_name2}, Дата рождения: {birth_date2}, Город: {city2}',
                phone=phone,
                email=email
            )
        else:
            order = Order.objects.create(
                check_in=datetime.strptime(check_in, "%d/%m/%Y"),
                check_out=datetime.strptime(check_out, "%d/%m/%Y"),
                room_type=type,
                clients_info=f'Имя: {first_name}, Фамилия: {last_name}, Дата рождения: {birth_date}, Город: {city}\n',
                phone=phone,
                email=email
            )
        order.save()
    context = {
        'check_in': check_in,
        'check_out': check_out,
        'adult': adult,
        'type': type,
    }
    return render(request, 'main_app/booking_complete.html', context)

def view_gallery(request):
    return render(request, 'main_app/gallery.html')
