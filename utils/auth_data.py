testing_data = [
    # test one user block Correct password
    ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),

    # without username and password
    ("", "", "Epic sadface: Username is required"),
    # user not correct without password
    ("wrong_username", "", "Epic sadface: Password is required"),

    # user and password not correct
    ("wrong_username", "wrong_password", "Epic sadface: Username and password do not match any user in this service"),
    # user correct password not correct
    ("standard_user", "Test12345", "Epic sadface: Username and password do not match any user in this service"),
    # user not correct password correct
    ("Test12345", "secret_sauce", "Epic sadface: Username and password do not match any user in this service")
]
