from fastapi import Request
from sqlalchemy.orm import Session


# 从 FastAPI 的 Request 对象中提取数据库会话
def get_db(request: Request) -> Session:
    return request.state.db


# 定义一个通用的查询参数模型
# 用于数据库查询中的分页处理
class CommonQueryParams:
    def __init__(self, offset: int = 1, limit: int = 10):
        self.offset = offset - 1
        if self.offset < 0:
            self.offset = 0
        self.limit = limit

        if self.limit < 0:
            self.limit = 10
