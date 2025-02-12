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
        data = {
            "id": self.id,
            "name_kr": self.name_kr,
            "name_en": self.name_en,
            "code": self.code,
            "code_full": self.code_full,
            "listing_date": self.listing_date,
        }
        return data


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

    def to_dict(self):
        data = {
            "id": self.id,
            "stock_id": self.stock_id,
            "collected_date": self.collected_date,
            "price": self.price,
            "price_change": self.price_change,
            "volume": self.volume,
            "trade_value": self.trade_value,
        }
        return data


class StockFinancials(Base):
    __tablename__ = "stock_financials"

    id = Column(Integer, primary_key=True, autoincrement=True)
    stock_id = Column(Integer, ForeignKey("stocks.id"))
    collected_date = Column(Date, nullable=False)
    total_asset = Column(BigInteger, nullable=False)
    total_debt = Column(BigInteger, nullable=False)
    cap = Column(BigInteger, nullable=False)
    total_cap = Column(BigInteger, nullable=False)
    sales = Column(BigInteger, nullable=False)
    profit = Column(BigInteger, nullable=False)
    income = Column(BigInteger, nullable=False)
    forign_ratio = Column(DECIMAL(5, 2), nullable=False)
    pe_ratio = Column(DECIMAL(6, 2), nullable=True)
    pb_ratio = Column(DECIMAL(5, 2), nullable=True)
    div_yield = Column(DECIMAL(5, 2), nullable=False)
    total_shares = Column(BigInteger, nullable=False)

    def __init__(
        self,
        stock_id,
        collected_date,
        total_asset,
        total_debt,
        cap,
        total_cap,
        sales,
        profit,
        income,
        forign_ratio,
        pe_ratio,
        pb_ratio,
        div_yield,
        total_shares,
    ):
        self.stock_id = stock_id
        self.collected_date = collected_date
        self.total_asset = int(total_asset.replace(",", ""))
        self.total_debt = int(total_debt.replace(",", ""))
        self.cap = int(cap.replace(",", ""))
        self.total_cap = int(total_cap.replace(",", ""))
        self.sales = int(sales.replace(",", ""))
        self.profit = int(profit.replace(",", ""))
        self.income = int(income.replace(",", ""))
        self.forign_ratio = float(forign_ratio)
        self.pe_ratio = float(pe_ratio.replace(",", "")) if pe_ratio != "-" else None
        self.pb_ratio = float(pb_ratio) if pb_ratio != "-" else None
        self.div_yield = float(div_yield)
        self.total_shares = int(total_shares.replace(",", ""))

    def __repr__(self):
        return f"<StockFinancials(id={self.id}, stock_id={self.stock_id}, collected_date={self.collected_date}, total_asset={self.total_asset}, total_debt={self.total_debt}, cap={self.cap}, total_cap={self.total_cap}, sales={self.sales}, profit={self.profit}, income={self.income}, forign_ratio={self.forign_ratio}, pe_ratio={self.pe_ratio}, pb_ratio={self.pb_ratio}, div_yield={self.div_yield})>"

    def to_dict(self):
        data = {
            "id": self.id,
            "stock_id": self.stock_id,
            "collected_date": self.collected_date,
            "total_asset": self.total_asset,
            "total_debt": self.total_debt,
            "cap": self.cap,
            "total_cap": self.total_cap,
            "sales": self.sales,
            "profit": self.profit,
            "income": self.income,
            "forign_ratio": self.forign_ratio,
            "pe_ratio": self.pe_ratio,
            "pb_ratio": self.pb_ratio,
            "div_yield": self.div_yield,
            "total_shares": self.total_shares,
        }
        return data
