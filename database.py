from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy import create_engine
from datetime import datetime

Base = declarative_base()

class audio(Base):
    __tablename__ = 'audio'
    id = Column(Integer, primary_key=True)
    # uid = Column(Integer, ForeignKey('user.uid'))
    name = Column(String(250), nullable=False)
    audio_file = Column(String(250), nullable=False)
    date = Column(DateTime, default=datetime.utcnow)

    def __str__(self):
        return self.name
    
class user(Base):
    __tablename__ = 'user'
    uid = Column(Integer, primary_key=True)
    user_id = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    

    def __str__(self):
        return self.name   


if __name__ == '__main__':
    engine = create_engine('sqlite:///project.sqlite')
    Base.metadata.create_all(engine)