from sqlalchemy import Boolean, Column, Integer, String, Float
from sqlalchemy.orm import relationship

from database import Base


class Devises(Base):
    __tablenames__ = "devises"

    #id = Column(Integer, primary_key=True, index=True)
    Devise = Column(String)
    Achat = Column(Float)
    Vente = Column(Float)
    new_devise = Column(Float)
    XOF_conversion  = Column(Float)
    pays = Column(String)
    flag = Column(String)

    

    items = relationship("Devise", back_populates="owner")
 