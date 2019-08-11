import helpers.authenticator as auth


def test_get_peppers_list():
    peppers = auth.get_peppers_list()
    assert len(peppers) > 0
    for pepper in peppers:
        assert type(pepper) is str
        assert len(pepper) > 0


def test_hash_password():
    hashed = auth.hash_password("sekret")
    assert type(hashed) is str
    assert len(hashed) > 10


def test_verify_password_correct():
    hashed = auth.hash_password("sekret")
    assert auth.verify_password(hashed, "sekret") is True


def test_verify_password_wrong():
    hashed = auth.hash_password("sekret")
    assert auth.verify_password(hashed, "wrong") is False


def test_create_token():
    token = auth.create_token("bob@bob.com")
    assert type(token) is str
    assert len(token) > 20


def test_verify_token_correct():
    token = auth.create_token("bob@bob.com")
    user_id = auth.verify_token(token)
    assert type(user_id) is str
    assert user_id == "bob@bob.com"


def test_verify_token_wrong():
    token = auth.create_token("bob@bob.com")
    token += "34343tregr"
    assert auth.verify_token(token) is None
