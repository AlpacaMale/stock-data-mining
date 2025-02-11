from sqlalchemy import (
    Column,
    String,
    Date,
    Integer,
    ForeignKey,
    BigInteger,
    DECIMAL,
    UniqueConstraint,
)
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


class StockPrice(Base):
    __tablename__ = "stock_prices"

    id = Column(Integer, primary_key=True, autoincrement=True)
    stock_id = Column(Integer, ForeignKey("stocks.id"))
    collected_date = Column(Date, nullable=False)
    price = Column(Integer, nullable=False)
    price_change = Column(DECIMAL(6, 2), nullable=False)
    volume = Column(BigInteger, nullable=False)
    trade_value = Column(BigInteger, nullable=False)

    __table_args__ = (
        UniqueConstraint("stock_id", "collected_date", name="unique_stock_price"),
    )

    def __init__(
        self, stock_id, collected_date, price, price_change, volume, trade_value
    ):
        self.stock_id = stock_id
        self.collected_date = collected_date
        self.price = int(price.replace(",", ""))
        self.price_change = float(price_change)
        self.volume = int(volume.replace(",", ""))
        self.trade_value = int(trade_value.replace(",", ""))

    def __repr__(self):
        return f"<StockPrice(collected_date={self.collected_date}, price={self.price}, change={self.change}, volume={self.volume}, trade_value={self.trade_value})>"
