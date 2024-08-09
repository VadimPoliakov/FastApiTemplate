from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON
from src.database import Base


class Video(Base):
    __tablename__ = "video"

    id = Column(Integer, primary_key=True, index=True)
    uid = Column(String(50), index=True, nullable=False)
    path = Column(String(255))
    name_video = Column(String(50))
    date_creation = Column(DateTime)
    status = Column(String(15), default="idle")


class Result(Base):
    __tablename__ = "result"

    id = Column(Integer, primary_key=True, index=True)
    video_id = Column(ForeignKey("video.id"), nullable=False)
    name = Column(String(30))
    totalFrames = Column(Integer)
    emotions = Column(JSON)
