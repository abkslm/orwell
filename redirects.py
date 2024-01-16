from flask import redirect


def linkedin(user: str):
    return redirect("https://linkedin.com/in/" + user)

def github(user: str):
    return redirect("https://github.com/" + user)