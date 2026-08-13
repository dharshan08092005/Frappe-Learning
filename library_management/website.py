import frappe

def get_home_page(user):
    print(user)
    if user == "Administrator":
        return "homepage"
    else:
        return "custom_404"