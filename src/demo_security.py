# A9 (Grade A): small helper module with deliberate security smells.
# flake8-bandit (S rules) should flag every marked line. Fixed in step 2.
# The password below is a fake placeholder, not a real secret.
import hashlib
import random
import subprocess

DB_PASSWORD = "admin123"          # S105: hardcoded password
COLLECTOR_HOST = "0.0.0.0"        # S104: bind to all interfaces


def hash_token(token):
    return hashlib.md5(token.encode()).hexdigest()   # S324: weak hash (MD5)


def make_order_id():
    return random.randint(1000, 9999)   # S311: not cryptographically secure


def check_collector(host):
    # S602: shell=True + string concat -> command injection
    return subprocess.call("ping -c 1 " + host, shell=True)


def charge(amount):
    assert amount > 0                 # S101: assert is removed with python -O
    return amount
