from busy_dates.models import *
import pandas as pd
from datetime import datetime, date, time


def get_busy_rooms(check_in_client, checkout_out_client):
    client_range = pd.date_range(start=check_in_client, end=checkout_out_client)
    format_client_range = set([datetime.strftime(i, '%d/%m/%Y') for i in client_range])
    busy_dates = Dates.objects.filter(course_type='1')
    luxe_count = Rooms.objects.filter(room_type='1').count()
    luxe_count_ = luxe_count
    standart_count = Rooms.objects.filter(room_type='2').count()
    standart_count_ = standart_count
    standart_busy_id = []
    luxe_busy_id = []
    for busy_date in busy_dates:
        busy_range = pd.date_range(start=busy_date.check_in, end=busy_date.check_out)
        format_busy_range = set([datetime.strftime(i, '%d/%m/%Y') for i in busy_range])
        if format_client_range.isdisjoint(format_busy_range):
            continue
        else:
            if busy_date.room.room_type == '1':
                if busy_date.room.id in luxe_busy_id:
                    continue
                luxe_busy_id.append(busy_date.room.id)
                luxe_count -= 1
            else:
                if busy_date.room.id in standart_busy_id:
                    continue
                standart_busy_id.append(busy_date.room.id)
                standart_count -= 1

    print({'luxe': f'{luxe_count}/{luxe_count_}',
           'standart': f'{standart_count}/{standart_count_}',
           'standart_busy_id': standart_busy_id,
           'luxe_busy_id': luxe_busy_id})

    return {'luxe': f'{luxe_count}/{luxe_count_}',
            'standart': f'{standart_count}/{standart_count_}',
            'standart_busy_id': standart_busy_id,
            'luxe_busy_id': luxe_busy_id
            }
