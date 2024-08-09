from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.app_name.exceptions import response_404_video
from src.app_name.models import Video
from src.app_name.schemas import Videos
from src.database import get_async_session

appname = APIRouter()


@appname.get("/healthcheck_appname", tags=["healthcheck"])
async def healthcheck():
    return Response(status_code=200)


@appname.get(
    "/videos/{uid}",
    response_model=Videos,
    tags=["inquire"],
    status_code=200,
    responses=response_404_video,
)
async def read_video_uid(uid: str, session: AsyncSession = Depends(get_async_session)):
    """Вывод информации видео по uid"""

    async with session:
        query = select(Video).where(Video.uid == uid)
        result = await session.execute(query)
        video_data = result.scalars().first()

        if video_data is None:
            raise HTTPException(status_code=404, detail="video_uid not found")

        return video_data
