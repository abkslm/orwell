from flask import redirect


def linkedin(user: str):
    return redirect("https://linkedin.com/in/" + user)


def github(user: str):
    return redirect("https://github.com/" + user)


def static(filename: str, type: str):
    link = "https://static.abkslm.com/objects/"
    if type == 'png' or type == 'svg':
        link = link + "img/" + type + "/" + filename
    elif type == 'pdf':
        link = link + "/pdf/" + filename
    return redirect(link)

