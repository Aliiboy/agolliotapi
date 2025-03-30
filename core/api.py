import os

from ninja import NinjaAPI, Swagger

from apps.humid_air.api import humid_air_router
from apps.project.api import project_router

# TODO
api = NinjaAPI(
    title="agolliot API",
    version="1.0.0",
    description="API pour le projet agolliot",
    docs=Swagger(),
    docs_url="/docs/",
    servers=[
        {
            "url": os.getenv("API_URL"),
            "description": os.getenv("API_SERVER_DESCRIPTION"),
        }
    ],
)


api.add_router("/project", project_router)
api.add_router("/humid_air", humid_air_router)
