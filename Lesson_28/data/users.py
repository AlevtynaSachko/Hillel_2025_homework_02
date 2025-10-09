from dataclasses import dataclass
from datetime import datetime, timezone
import secrets
import string

@dataclass
class User:
    name: str
    last_name: str
    email: str
    password: str

def rand_email(domain="example.com"):
    ts = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S%f")
    return f"auto_{ts}@{domain}"

def rand_password(length=12):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def make_user():
    return User(
        name="Ala",
        last_name="Test",
        email=rand_email("mailinator.com"),
        password=rand_password(14),
    )
