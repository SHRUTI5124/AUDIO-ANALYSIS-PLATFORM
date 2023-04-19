from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import create_engine
from datetime import datetime

Base = declarative_base()

class audio(Base):
    __tablename__ = 'audio'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    audio_file = Column(String(250), nullable=False)
    date = Column(DateTime, default=datetime.utcnow)

    def __str__(self):
        return self.name
    

if __name__ == '__main__':
    engine = create_engine('sqlite:///project.sqlite')
    Base.metadata.create_all(engine)