from pydantic import BaseModel



class Base(BaseModel):
    pass


class AuthenticationData(Base):

    login: str
    password: str