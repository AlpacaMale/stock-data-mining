from sqlalchemy import Column, String, Date, Integer
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class Stock(Base):
    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name_kr = Column(String(100), nullable=False)
    name_en = Column(String(100), nullable=False)
    code = Column(String(6), nullable=False)
    code_full = Column(String(12), nullable=False)
    listing_date = Column(Date, nullable=False)

    def __init__(self, name_kr, name_en, code, code_full, listing_date):
        self.name_kr = name_kr
        self.name_en = name_en
        self.code = code
        self.code_full = code_full
        self.listing_date = datetime.strptime(listing_date, "%Y/%m/%d").date()

    def __repr__(self):
        return f"<Stock(name_kr={self.name_kr}, name_en={self.name_en}, code={self.code}, code_full={self.code_full}, listing_date={self.listing_date})>"

    def to_dict(self):
        stock = {
            "id": self.id,
            "name_kr": self.name_kr,
            "name_en": self.name_en,
            "code": self.code,
            "code_full": self.code_full,
            "listing_date": self.listing_date,
        }
        return stock
