from sqlalchemy import Column, String, Integer
from stamps_api import Base


class Stamp(Base):
    __tablename__ = 'stamp'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    origin = Column(String(100))
    rarity = Column(String(100))

    def __repr__(self):
        return '<Stamp %r>' % (self.name)
