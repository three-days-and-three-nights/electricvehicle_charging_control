from fastapi import APIRouter, FastAPI

from electricvehicle_charging_control import views


def router_v1():
    router = APIRouter()
    router.include_router(views.router, tags=['Vehicle'])
    return router


def init_routers(app: FastAPI):
    app.include_router(router_v1(), prefix='/api/v1', tags=['v1'])
