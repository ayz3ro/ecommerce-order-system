from .base import AppException


class AuthenticationError(AppException):
    """Base exception for authentication failures."""

    def __init__(self, message: str = "Authentication failed.", *, code: str = "AUTHENTICATION_ERROR",
            status_code: int = 401, ) -> None:
        super().__init__(message, code=code, status_code=status_code, )


class InvalidCredentials(AuthenticationError):
    """Raised when login credentials are invalid."""

    def __init__(self) -> None:
        super().__init__(message="Invalid email or password.", code="INVALID_CREDENTIALS", status_code=401, )


class AccountDisabled(AuthenticationError):
    """Raised when a disabled account attempts authentication."""

    def __init__(sexslf) -> None:
        super().__init__(message="This account is disabled.", code="ACCOUNT_DISABLED", status_code=403, )


class InvalidToken(AuthenticationError):
    """Raised when an access token is invalid or malformed."""

    def __init__(self) -> None:
        super().__init__(message="Invalid authentication token.", code="INVALID_TOKEN", status_code=401, )


class TokenExpired(AuthenticationError):
    """Raised when an access token has expired."""

    def __init__(self) -> None:
        super().__init__(message="Authentication token has expired.", code="TOKEN_EXPIRED", status_code=401, )
