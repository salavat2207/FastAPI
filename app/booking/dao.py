from app.database import SessionLocal
from app.booking.models import Bookings
from app.dao.base import BaseDao
from sqlalchemy import select




# Создаем в srvices.py класс BookingService передаем model = Bookings, тем самым наследуется все методы класса
class BookingDao(BaseDao):
    model = Bookings

