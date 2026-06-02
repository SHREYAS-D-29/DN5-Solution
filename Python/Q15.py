def login(user, pwd):
    if not user or not pwd:
        return "Blank input"
    if user == "admin":
        if pwd == "pass123":
            return "Login Successful"
        return "Wrong Password"
    return "Invalid User"

print(login("admin", "pass123"))
