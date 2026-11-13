# A9 (Grade A): fixed version of the helper module after reading flake8-bandit.
import hashlib
import os
import secrets
import subprocess  # noqa: S404  reviewed: only used with a fixed argument list

DB_PASSWORD = os.environ.get("DB_PASSWORD", "")      # fix S105: read from env
COLLECTOR_HOST = os.environ.get("COLLECTOR_HOST", "127.0.0.1")  # fix S104


def hash_token(token):
    return hashlib.sha256(token.encode()).hexdigest()   # fix S324


def make_order_id():
    return 1000 + secrets.randbelow(9000)   # fix S311: secrets module


def check_collector(host):
    # fix S602: no shell, arguments passed as a list, so host cannot inject
    # S603/S607 are flagged for any subprocess call; reviewed -> false positive
    result = subprocess.run(["ping", "-c", "1", host], check=False)  # noqa: S603,S607
    return result.returncode


def charge(amount):
    if amount <= 0:                   # fix S101: real check, not assert
        raise ValueError("amount must be positive")
    return amount
