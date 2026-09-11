from datetime import datetime, timedelta, timezone
from typing import Any

from pwdlib import PasswordHash

from core.config import settings

password_hash = PasswordHash.recommended()


def create_access_token(subject: str, *, expires_delta: timedelta | None = None,
                        additional_claims: dict[str, Any] | None = None, ) -> str:
    """
    Create a signed JWT access token.

    Args:
        subject: Unique identifier of the authenticated user.
        expires_delta: Optional custom token lifetime.
        additional_claims: Optional claims such as role/permissions.

    Returns:
        Encoded JWT access token.
    """

    now = datetime.now(timezone.utc)

    expires_at = now + (
        expires_delta if expires_delta is not None else timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))

    payload: dict[str, Any] = {"sub": subject, "iat": now, "exp": expires_at, "type": "access", }

    if additional_claims:
        payload.update(additional_claims)

    return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM, )


from jose import JWTError, jwt


def decode_access_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM], )

        if payload.get("type") != "access":
            raise ValueError("Invalid token type")

        if not payload.get("sub"):
            raise ValueError("Token subject is missing")

        return payload

    except (JWTError, ValueError) as exc:
        raise ValueError("Invalid or expired access token") from exc


def hash_password(password: str) -> str:
    return password_hash.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return password_hash.verify(password, hashed_password)
