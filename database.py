from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime


Base = declarative_base()
class Feedback(Base):
    __tablename__ = 'feedback'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(64))
    message = Column(String(256))
    created_on = Column(DateTime, default=datetime.now)

    def __str__(self):
        return f'Feedback : {self.name}'
    
if __name__=='__main__':
    engine = create_engine('sqlite:///app.sqlite', echo=True)
    Base.metadata.create_all(engine)