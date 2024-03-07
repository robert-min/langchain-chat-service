from shared.infra.database.model import Base
from sqlalchemy import Column, Integer, String, Boolean, LargeBinary


class Account(Base):
    __tablename__ = 'user_account'

    seq = Column(Integer, primary_key=True)
    email = Column(String(500), nullable=False)
    password = Column(LargeBinary, nullable=False)
    status = Column(Boolean, nullable=False, default=True)
