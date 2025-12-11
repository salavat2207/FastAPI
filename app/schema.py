from pydantic import BaseModel
from datetime import date

class SBooking(BaseModel):
	room_id: int
	date_from: date
	date_to: date


class SBookingResponse(BaseModel):
    id: int
    room_id: int | None
    user_id: int | None
    date_from: date
    date_to: date
    price: int
    total_cost: int | None
    total_days: int | None

    class Config:
        from_attributes = True  # Позволяет создавать из SQLAlchemy моделей


class SHotel(BaseModel):
	adress: str
	name: str
	stars: int