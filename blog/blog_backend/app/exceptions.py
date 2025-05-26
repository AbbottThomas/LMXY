from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from typing import Any

class CustomAPIException(HTTPException):
    def __init__(
        self,
        status_code: int = status.HTTP_400_BAD_REQUEST,
        detail: Any = "An error occurred",
        headers: dict[str, Any] | None = None,
    ):
        super().__init__(status_code=status_code, detail=detail, headers=headers)

class UniqueConstraintViolation(CustomAPIException):
    def __init__(self, field: str):
        detail = f"{field.capitalize()} already exists"
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail=detail
        )

class PermissionDeniedException(CustomAPIException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Permission denied"
        )

def handle_unique_constraint_error(exc: Exception):
    if "duplicate key" in str(exc).lower():
        field = "username" if "username" in str(exc) else "email"
        return JSONResponse(
            status_code=409,
            content={"detail": f"{field.capitalize()} already exists"}
        )
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"}
    )