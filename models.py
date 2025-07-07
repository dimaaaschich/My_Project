from sqlalchemy.orm import Mapped, mapped_column
from db import engine, Base


class Deals(Base):
    __tablename__ = 'deals_list'
    id: Mapped[int] = mapped_column(primary_key=True)
    agent: Mapped[str] =
    contractor: Mapped[int]
    create_date: Mapped[int]
    number_deal: Mapped[int]
    subject: Mapped[int]
    price: Mapped[int]