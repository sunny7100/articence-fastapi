from sqlalchemy import Column, String, Integer
from database import Base

class Call(Base):
    __tablename__ = "calls"

    id = Column(String, primary_key=True)
    state = Column(String, default="IN_PROGRESS")
    last_sequence = Column(Integer, default=0)

class Packet(Base):
    __tablename__ = "packets"

    id = Column(Integer, primary_key=True)
    call_id = Column(String)
    sequence = Column(Integer)
