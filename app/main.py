from datetime import date

from fastapi import FastAPI, Query
from typing import Optional

from app.schema import SBooking, SHotel
from app.booking.router import router as router_booking

app = FastAPI()
app.include_router(router_booking)


list[SHotel]

@app.get('/hotels')
def get_hotels(
		location,
		date_from: date,
		date_to: date,
		stars: Optional[int] = Query(None, ge=1, le=5),
		has_spa: Optional[bool] = None,
	) -> list[SHotel]:
	hotels = [
		{
		'adress': 'ул 1 Мая, 12, Уфа',
		'name': 'Отель Редиссон',
		'stars': 5,

	}
	]

	return hotels


@app.post('/booking')
def add_booking(booking: SBooking):
	pass

