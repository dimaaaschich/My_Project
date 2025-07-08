from sqlalchemy import Date
from sqlalchemy.orm import Mapped, mapped_column

from db import db_session, engine, Base

class Deals(Base):
    __tablename__ = 'deals_list'
    id: Mapped[int] = mapped_column(primary_key=True)
    agent: Mapped[str]
    contractor: Mapped[ str]
    ds_create_date: Mapped[Date] = mapped_column(Date, nullable=True)
    ds_name: Mapped[str]
    deal_create_date: Mapped[Date] = mapped_column(Date, nullable=True)
    name_deal: Mapped[str]
    deal_subject: Mapped[str]
    ds_deal_subject: Mapped[str]
    price: Mapped[float]

if __name__ == '__main__':
    Base.metadata.create_all(engine)