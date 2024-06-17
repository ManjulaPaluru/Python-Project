import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_first_Program():
    msg = "hello"
    assert msg == "hello", ("test failed because wrong message ")