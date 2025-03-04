from sqlalchemy import Column, Integer, String, JSON
from database.models import Base

class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    address = Column(String)
    phone_number = Column(String)
    email = Column(String)
    meta_data = Column(JSON, nullable=True)

    def to_dict(self):
        # def to_dict(self, show_meeting_room=True): TODO
        data = {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "phone_number": self.phone_number,
            "email": self.email,
            "meta_data": self.meta_data,
        }
        return data
