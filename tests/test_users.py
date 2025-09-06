access_token = None


# test for user registration
def test_user_register(client_instance):

    response = client_instance.post(
        "account/register",
        json={
            "username": "mahdijf",
            "first_name": "Mahdi",
            "last_name": "Jahanfar",
            "password": "123456",
        },
    )

    data = response.json()

    assert response.status_code == 201
    print(data)


# test for user list route
def test_users_list(client_instance):

    response = client_instance.get("/account/users/list")

    assert response.status_code == 200


# test for user login route with ok status
def test_user_login_ok(client_instance):

    response = client_instance.post(
        "/account/login", json={"username": "mahdijf", "password": "123456"}
    )

    data = response.json()
    access_token = data["access token"]

    assert response.status_code == 200


# test for user login route with 401 status
def test_user_login_username_faild(client_instance):

    response = client_instance.post(
        "/account/login", json={"username": "mahdisf", "password": "123456"}
    )

    assert response.status_code == 401


# test user login with wrong password
def test_user_login_password_faild(client_instance):

    response = client_instance.post(
        "/account/login", json={"username": "mahdijf", "password": "12345556"}
    )

    assert response.status_code == 401


# function for get access token with refresh token route
def test_get_access_token_ok(client_instance):

    response = client_instance.post(
        "/account/token/refresh", json={"refresh_token": access_token}
    )

    response.status_code == 201


# function for access token faild route
def test_get_access_token_faild(client_instance):

    response = client_instance.post(
        "account/token/refresh", json={"refresh_token": "1234"}
    )

    response.status_code == 401
