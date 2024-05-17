from sqlalchemy.orm import relationship


class State(BaseModel):
class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
