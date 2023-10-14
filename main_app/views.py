from django.shortcuts import render
from django.urls import reverse

from .models import *
from orders.models import *
from busy_dates.models import *
from .forms import *
from datetime import datetime, date, time


def main_page(request):
    photos = MainPhotos.objects.all().first()
    course_photos = CoursesPhoto.objects.all().first()
    description = Description.objects.filter(active=True).first()
    phone = MainPhone.objects.all().first()
    price = Prices.objects.all().first()
    offer = False
    if Offer.objects.all():
        offer = True
    context = {
        'phone': phone,
        'price': price,
        'photos': photos,
        'course_photos': course_photos,
        'description': description,
        'offer': offer
    }
    return render(request, 'main_app/index.html', context)


def book_health_back(request):
    price = Prices.objects.all().first()
    phone = MainPhone.objects.all().first()
    course = HealthBack.objects.all().first()
    context = {
        'phone': phone,
        'price': price,
        'course': course
    }
    return render(request, 'main_app/health_back.html', context)


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
            # price = Prices.objects.all().first()
            # luxe_price = price.luxe_room_full_health * days_count
            # standart_price = price.standart_room_full_health * days_count
            # busy_rooms = 1
            # rooms_images = NumberImages.objects.all().first()
            context_post = {
                # 'luxe_img': rooms_images.luxe.url,
                # 'standart_img': rooms_images.standart.url,
                # 'luxe_price': int(luxe_price) * int(adult),
                # 'standart_price': int(standart_price) * int(adult),
                'days_count': days_count,
                'check_in': check_in,
                'check_out': check_out,
                'adult': adult,
                # 'luxe_count': busy_rooms['luxe'].split('/')[-1],
                # 'luxe_free': int(busy_rooms['luxe'].split('/')[0]),
                # 'standart_count': busy_rooms['standart'].split('/')[-1],
                # 'standart_free': int(busy_rooms['standart'].split('/')[0]),
            }
            return redirect(f'{reverse(booking_personal_info)}?check_in={check_in}&check_out={check_out}&adult={adult}')
    price = Prices.objects.all().first()
    course = MainCourse.objects.all().first()
    context = {
        'form': form,
        'price': price,
        'course': course
    }
    return render(request, 'main_app/book.html', context)


def booking_mini(request):
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
            # price = Prices.objects.all().first()
            # luxe_price = price.luxe_room_full_health * days_count
            # standart_price = price.standart_room_full_health * days_count
            # busy_rooms = 1
            # rooms_images = NumberImages.objects.all().first()
            context_post = {
                # 'luxe_img': rooms_images.luxe.url,
                # 'standart_img': rooms_images.standart.url,
                # 'luxe_price': int(luxe_price) * int(adult),
                # 'standart_price': int(standart_price) * int(adult),
                'days_count': days_count,
                'check_in': check_in,
                'check_out': check_out,
                'adult': adult,
                # 'luxe_count': busy_rooms['luxe'].split('/')[-1],
                # 'luxe_free': int(busy_rooms['luxe'].split('/')[0]),
                # 'standart_count': busy_rooms['standart'].split('/')[-1],
                # 'standart_free': int(busy_rooms['standart'].split('/')[0]),
            }
            return redirect(f'{reverse(booking_personal_info)}?check_in={check_in}&check_out={check_out}&adult={adult}')
    price = Prices.objects.all().first()
    course = MainCourseMini.objects.all().first()
    context = {
        'form': form,
        'price': price,
        'course': course
    }
    return render(request, 'main_app/course_mini.html', context)


def booking_personal_info(request):
    check_in = request.GET['check_in']
    check_out = request.GET['check_out']
    adult = request.GET['adult']
    # type = request.POST['type']
    # price = request.POST['price']
    rooms_images = NumberImages.objects.all().first()
    if adult == '2':
        form = DuoPersonalInfoForm
    else:
        form = SinglePersonalInfoForm
    context = {
        'rooms_images': rooms_images,
        'check_in': check_in,
        'check_out': check_out,
        'adult': adult,
        'form': form,
    }
    return render(request, 'main_app/book_step_3.html', context)


def booking_complete(request):
    check_in = request.POST['check_in']
    check_out = request.POST['check_out']
    adult = request.POST['adult']
    # type = request.POST['type']
    # price = request.POST['price']
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
        if adult == '2':
            order = Order.objects.create(
                check_in=datetime.strptime(check_in, "%d/%m/%Y"),
                check_out=datetime.strptime(check_out, "%d/%m/%Y"),
                clients_info=f'Имя: {first_name}, Фамилия: {last_name}, Дата рождения: {birth_date}, Город: {city}\n'
                             f'Имя: {first_name2}, Фамилия: {last_name2}, Дата рождения: {birth_date2}, Город: {city2}',
                phone=phone,
                email=email,
                price=0
            )
        else:
            order = Order.objects.create(
                check_in=datetime.strptime(check_in, "%d/%m/%Y"),
                check_out=datetime.strptime(check_out, "%d/%m/%Y"),
                clients_info=f'Имя: {first_name}, Фамилия: {last_name}, Дата рождения: {birth_date}, Город: {city}\n',
                phone=phone,
                email=email,
                price=0,
            )
        order.save()
        context = {
            'check_in': check_in,
            'check_out': check_out,
            'adult': adult,
        }
        return render(request, 'main_app/booking_complete.html', context)


def book_osteopat(request):
    price = Prices.objects.all().first()
    phone = MainPhone.objects.all().first()
    form = OsteopatForm()
    if request.POST:
        form = OsteopatForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            form_ = OsteopatPersonalInfoForm()
            context_ = {
                'form': form_,
                'date': date,
                'price': price.osteopat,
            }
            return render(request, 'main_app/book_osteopat_personal_info.html', context_)
    course = OsteopatDescription.objects.all().first()
    context = {
        'phone': phone,
        'price': price,
        'form': form,
        'course': course
    }
    return render(request, 'main_app/book_osteopat.html', context)


def book_osteopat_complete(request):
    date = request.POST['date']
    price = request.POST['price']
    form = OsteopatPersonalInfoForm(request.POST)
    print(form.errors)
    if form.is_valid():
        busy_date = Dates.objects.create(
            course_type='3',
            course_date=datetime.strptime(date, '%d/%m/%Y')
        )
        busy_date.save()
        order = OrderOsteopat.objects.create(
            check_in=datetime.strptime(date, '%d/%m/%Y'),
            clients_info=f'Имя: {form.cleaned_data["first_name"]}, Фамилия: {form.cleaned_data["last_name"]}, '
                         f'Дата рождения: {form.cleaned_data["birth_date"]}, Город: {form.cleaned_data["city"]}',
            phone=form.cleaned_data['phone'],
            email=form.cleaned_data['email'],
            price=price
        )
        order.save()
        context = {
            'date': date,
            'price': price,
        }
        return render(request, 'main_app/book_osteopat_complete.html', context)


def book_day(request):
    price = Prices.objects.all().first()
    form = OsteopatForm()
    if request.POST:
        form = OsteopatForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            form_ = OsteopatPersonalInfoForm()
            context_ = {
                'form': form_,
                'date': date,
                'typeof': 'День здоровья',
            }
            return render(request, 'main_app/book_day_personal_info.html', context_)
    course = DayDescription.objects.all().first()
    context = {
        'price': price,
        'form': form,
        'course': course
    }
    return render(request, 'main_app/book_day.html', context)


def book_day_complete(request):
    date = request.POST['date']
    typeof = request.POST['typeof']
    form = OsteopatPersonalInfoForm(request.POST)
    print(form.errors)
    if form.is_valid():
        busy_date = Dates.objects.create(
            course_type='2',
            course_date=datetime.strptime(date, '%d/%m/%Y')
        )
        busy_date.save()
        order = OrderDay.objects.create(
            check_in=datetime.strptime(date, '%d/%m/%Y'),
            clients_info=f'Имя: {form.cleaned_data["first_name"]}, Фамилия: {form.cleaned_data["last_name"]}, '
                         f'Дата рождения: {form.cleaned_data["birth_date"]}, Город: {form.cleaned_data["city"]}',
            phone=form.cleaned_data['phone'],
            email=form.cleaned_data['email'],
            typeof=typeof
        )
        order.save()
        context = {
            'date': date,
            'typeof': typeof
        }
        return render(request, 'main_app/book_day_complete.html', context)
    context = {
        'form': form,
        'date': date,
        'typeof': 'День здоровья',
    }
    return render(request, 'main_app/book_day_personal_info.html', context)


def book_day_mini(request):
    price = Prices.objects.all().first()
    form = OsteopatForm()
    if request.POST:
        form = OsteopatForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            form_ = OsteopatPersonalInfoForm()
            context_ = {
                'form': form_,
                'date': date,
                'typeof': 'День здоровья "мини"',
            }
            return render(request, 'main_app/book_day_personal_info.html', context_)
    course = DayMiniDescription.objects.all().first()
    context = {
        'price': price,
        'form': form,
        'course': course
    }
    return render(request, 'main_app/book-day-mini.html', context)


def book_health_tourism_3(request):
    price = Prices.objects.all().first().health_tourism_3
    phone = MainPhone.objects.all().first()
    course = HealthTourism3.objects.all().first()
    context = {
        'phone': phone,
        'price': price,
        'course': course,
        'title': 'Лечение и туризм 3 дня'
    }
    return render(request, 'main_app/health_tourism.html', context)


def book_health_tourism_5(request):
    price = Prices.objects.all().first().health_tourism_5
    phone = MainPhone.objects.all().first()
    course = HealthTourism5.objects.all().first()
    context = {
        'phone': phone,
        'price': price,
        'course': course,
        'title': 'Лечение и туризм 5 дней'
    }
    return render(request, 'main_app/health_tourism.html', context)


def book_health_tourism_7(request):
    price = Prices.objects.all().first().health_tourism_7
    phone = MainPhone.objects.all().first()
    course = HealthTourism7.objects.all().first()
    context = {
        'phone': phone,
        'price': price,
        'course': course,
        'title': 'Лечение и туризм 7 дней'
    }
    return render(request, 'main_app/health_tourism.html', context)


def book_health_tourism_10(request):
    price = Prices.objects.all().first().health_tourism_10
    phone = MainPhone.objects.all().first()
    course = HealthTourism10.objects.all().first()
    context = {
        'phone': phone,
        'price': price,
        'course': course,
        'title': 'Лечение и туризм 10 дней'
    }
    return render(request, 'main_app/health_tourism.html', context)


def view_gallery(request):
    photos = Gallery.objects.all()
    categories = GalleryCategory.objects.all()
    context = {
        'photos': photos,
        'categories': categories
    }
    return render(request, 'main_app/gallery.html', context)


def view_doctors(request):
    staff = Staff.objects.all()
    context = {
        'staff': staff,
    }
    return render(request, 'main_app/doctors.html', context)


def view_tourism(request):
    records = Tourism.objects.all()
    context = {
        'records': records,
    }
    return render(request, 'main_app/tourism.html', context)


def view_smi(request):
    records = Smi.objects.all()
    context = {
        'records': records,
    }
    return render(request, 'main_app/smi.html', context)


def view_rules(request):
    record = Rules.objects.all().first()
    context = {
        'record': record.rules,
    }
    return render(request, 'main_app/rules.html', context)


def view_rooms(request):
    records = Rooms.objects.all()
    context = {
        'rooms': records,
    }
    return render(request, 'main_app/rooms.html', context)


def view_procedures(request):
    records = Procedures.objects.all()
    context = {
        'procedures': records,
    }
    return render(request, 'main_app/procedures.html', context)


def view_offer(request):
    record = Offer.objects.all()
    context = {
        'offers': record,
    }
    return render(request, 'main_app/offer.html', context)
