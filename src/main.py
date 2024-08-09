from fastapi import FastAPI, Response

from src.app_name.router import appname

app = FastAPI()

app.include_router(appname)


@app.get("/healthcheck", tags=["healthcheck"])
async def healthcheck():
    return Response(status_code=200)
