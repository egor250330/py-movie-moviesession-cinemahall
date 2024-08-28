from django.db.models import QuerySet
from db.models import CinemaHall


def get_cinema_halls() -> QuerySet:

    return CinemaHall.objects.all()

def create_cinema_hall(
        hall_name: str,
        hall_rows: str,
        hall_seats_in_row: int
) -> CinemaHall:
    cinema_hall = CinemaHall.objects.create(
        hall_name=hall_name,
        hall_rows=hall_rows,
        seats_in_row=hall_seats_in_row
    )
    return cinema_hall
