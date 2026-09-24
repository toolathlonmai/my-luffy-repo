from src.utils import hash_password


def test_hash_password():
    h = hash_password('password')
    assert isinstance(h, str)
    assert len(h) == 64  # SHA-256 hex


def test_integration():
    # Basic integration test
    h = hash_password('test123')
    assert h is not None
