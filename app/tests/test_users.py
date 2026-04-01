def test_create_user(client):
    response = client.post(
        "/users",
        json={"name": "Test", "email": "test@example.com"},
    )

    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test"
    assert data["email"] == "test@example.com"


def test_create_user_invalid_email(client):
    response = client.post(
        "/users",
        json={"name": "Test", "email": "invalid-email"},
    )

    assert response.status_code == 422


def test_create_user_duplicate(client):
    first_response = client.post(
        "/users",
        json={"name": "Test", "email": "dup@example.com"},
    )
    assert first_response.status_code == 200

    second_response = client.post(
        "/users",
        json={"name": "Test", "email": "dup@example.com"},
    )

    assert second_response.status_code == 409
    assert second_response.json() == {"detail": "Email already exists"}


def test_list_users(client):
    client.post(
        "/users",
        json={"name": "Alice", "email": "alice@example.com"},
    )

    response = client.get("/users")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["email"] == "alice@example.com"