from typing import Callable

from fastapi import FastAPI, Request, Response

from electricvehicle_charging_control.db import SessionFactory


async def db_session_middleware(request: Request, call_next: Callable) -> Response:
    # 作为备用的错误信息相应
    response = Response('Internal server error', status_code=500)
    try:
        # 为当前请求初始化一个数据库会话
        request.state.db = SessionFactory()
        # 使用 await 异步调用 call_next 函数
        # 将控制权传递给中间件链中的下一个中间件或请求的终端处理器
        response = await call_next(request)
    finally:
        # 关闭在 try 块中创建的数据库会话
        request.state.db.close()

    return response


def init_middleware(app: FastAPI) -> None:
    app.middleware('http')(db_session_middleware)
