from fastapi import APIRouter, HTTPException
from app.booking.dao import BookingDao
from app.schema import SBooking, SBookingResponse

router = APIRouter(
    prefix='/bookings', 
    tags=['Бронирования']
)

@router.get('', response_model=SBookingResponse)
async def get_bookings():
    booking = await BookingDao.find_one_or_none(room_id=12)
    if booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking


