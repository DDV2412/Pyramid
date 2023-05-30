import datetime

from sqlalchemy import BigInteger, Column, String, DateTime

from app.models.metadata import Base


class Contact(Base):
    __tablename__ = 'contact'

    id = Column(BigInteger, primary_key=True)
    email = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.datetime.utcnow())
