from pydantic import BaseModel


class DeviseBase(BaseModel):
    Devise: str
    Achat: float
    Vente: float
    new_devise: float
    XOF_conversion: float
    pays: str
    flag: str



    class Config:
        orm_mode = True