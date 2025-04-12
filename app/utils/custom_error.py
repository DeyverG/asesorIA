from fastapi.responses import JSONResponse


def custom_error(exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status": "error",
            "data": exc.detail
        },
    )
