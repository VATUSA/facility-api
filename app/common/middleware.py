import datetime
import uuid
from app.database.lightning.models import APIRequestLog
from app.helpers.FacilityHelper import FacilityHelper
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware


class APILogMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        request.state.request_id = str(uuid.uuid4())
        log = APIRequestLog(
            request_id=request.state.request_id,
            request_method=request.method,
            request_path=request.url.path,
            request_query_params=str(request.query_params),
            api_key=None,
            user_cid=None,
            status_code=0,
            request_date=datetime.datetime.now()
        )

        response = await call_next(request)

        log.status_code = response.status_code
        if request.method in ['PUT', 'POST', 'DELETE'] or response.status_code >= 400:
            await log.save()
        return response


class HelperPreCacheMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        await FacilityHelper.preload_records()
        return await call_next(request)
