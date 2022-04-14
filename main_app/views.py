from django.shortcuts import render
from .models import *
from orders.models import *
from busy_dates.models import *
from .forms import *
from datetime import datetime, date, time
from .utils import *


def main_page(request):
    photos = MainPhotos.objects.all().first()
    course_photos = CoursesPhoto.objects.all().first()
    description = Description.objects.filter(active=True).first()
    price = Prices.objects.all().first()
    context = {
        'price': price,
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
            check_in_date = datetime.strptime(check_in, '%d/%m/%Y')
            check_out_date = datetime.strptime(check_out, '%d/%m/%Y')
            days_count = int((check_out_date - check_in_date).days)
            price = Prices.objects.all().first()
            luxe_price = price.luxe_room_full_health * days_count
            standart_price = price.standart_room_full_health * days_count
            busy_rooms = get_busy_rooms(check_in_client=check_in_date, checkout_out_client=check_out_date)
            context_post = {
                'luxe_price': luxe_price,
                'standart_price': standart_price,
                'days_count': days_count,
                'check_in': check_in,
                'check_out': check_out,
                'adult': adult,
                'luxe_count': busy_rooms['luxe'].split('/')[-1],
                'luxe_free': int(busy_rooms['luxe'].split('/')[0]),
                'standart_count': busy_rooms['standart'].split('/')[-1],
                'standart_free': int(busy_rooms['standart'].split('/')[0]),
            }
            return render(request, 'main_app/book_step_2.html', context_post)
    price = Prices.objects.all().first()
    course = MainCourse.objects.all().first()
    context = {
        'price': price,
        'form': form,
        'course': course
    }
    return render(request, 'main_app/book.html', context)


def booking_personal_info(request):
    check_in = request.POST['check_in']
    check_out = request.POST['check_out']
    adult = request.POST['adult']
    type = request.POST['type']
    price = request.POST['price']
    if adult == '2':
        form = DuoPersonalInfoForm
    else:
        form = SinglePersonalInfoForm
    context = {
        'check_in': check_in,
        'check_out': check_out,
        'adult': adult,
        'type': type,
        'form': form,
        'price': price,
    }
    return render(request, 'main_app/book_step_3.html', context)


def booking_complete(request):
    check_in = request.POST['check_in']
    check_out = request.POST['check_out']
    adult = request.POST['adult']
    type = request.POST['type']
    price = request.POST['price']
    if adult == '2':
        form = DuoPersonalInfoForm(request.POST)
    else:
        form = SinglePersonalInfoForm(request.POST)
    print(form.errors)
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
        room_for_regist = str()
        if type == 'Комфорт':
            rooms_busy_id = get_busy_rooms(check_in_client=datetime.strptime(check_in, "%d/%m/%Y"),
                                           checkout_out_client=datetime.strptime(check_out, "%d/%m/%Y"))['luxe_busy_id']
            rooms = Rooms.objects.filter(room_type='1')
            for room in rooms:
                if room.id in rooms_busy_id:
                    continue
                else:
                    date_ = Dates.objects.create(
                        check_in=datetime.strptime(check_in, "%d/%m/%Y"),
                        check_out=datetime.strptime(check_out, "%d/%m/%Y"),
                        room=room
                    )
                    room_for_regist = room
                    date_.save()
                    break
        else:
            rooms_busy_id = get_busy_rooms(check_in_client=datetime.strptime(check_in, "%d/%m/%Y"),
                                           checkout_out_client=datetime.strptime(check_out, "%d/%m/%Y"))[
                'standart_busy_id']
            rooms = Rooms.objects.filter(room_type='2')
            for room in rooms:
                if room.id in rooms_busy_id:
                    continue
                else:
                    date_ = Dates.objects.create(
                        check_in=datetime.strptime(check_in, "%d/%m/%Y"),
                        check_out=datetime.strptime(check_out, "%d/%m/%Y"),
                        room=room
                    )
                    room_for_regist = room
                    date_.save()
                    break
        if adult == '2':
            order = Order.objects.create(
                check_in=datetime.strptime(check_in, "%d/%m/%Y"),
                check_out=datetime.strptime(check_out, "%d/%m/%Y"),
                room_type=type,
                clients_info=f'Имя: {first_name}, Фамилия: {last_name}, Дата рождения: {birth_date}, Город: {city}\n'
                             f'Имя: {first_name2}, Фамилия: {last_name2}, Дата рождения: {birth_date2}, Город: {city2}',
                phone=phone,
                email=email,
                room=room_for_regist,
                price=price
            )
        else:
            order = Order.objects.create(
                check_in=datetime.strptime(check_in, "%d/%m/%Y"),
                check_out=datetime.strptime(check_out, "%d/%m/%Y"),
                room_type=type,
                clients_info=f'Имя: {first_name}, Фамилия: {last_name}, Дата рождения: {birth_date}, Город: {city}\n',
                phone=phone,
                email=email,
                price=price,
                room=room_for_regist
            )
        order.save()

        context = {
            'check_in': check_in,
            'check_out': check_out,
            'adult': adult,
            'type': type,
            'price': price,
        }
        return render(request, 'main_app/booking_complete.html', context)


def book_osteopat(request):
    price = Prices.objects.all().first()
    form = OsteopatForm()
    course = OsteopatDescription.objects.all().first()
    context = {
        'price': price,
        'form': form,
        'course': course
    }
    return render(request, 'main_app/book_osteopat.html', context)

def book_day(request):
    price = Prices.objects.all().first()
    form = OsteopatForm()
    course = DayDescription.objects.all().first()
    context = {
        'price': price,
        'form': form,
        'course': course
    }
    return render(request, 'main_app/book_day.html', context)

def view_gallery(request):
    return render(request, 'main_app/gallery.html')


def view_doctors(request):
    return render(request, 'main_app/doctors.html')


def view_tourism(request):
    records = Tourism.objects.all()
    context = {
        'records': records,
    }
    return render(request, 'main_app/tourism.html', context)
