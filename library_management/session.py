import frappe

#For on_login hook
def successful_login():
    current_user = frappe.get_doc("User", frappe.session.user)
    print("USER Type:", current_user)

#For on_session_creation hook
def allocate_free_credits():
    user = frappe.session.user
    if user  == "Administrator":
        credits = 100

    elif user == "Guest":
        credits = 20

    else:
        credits = 50
    print(f"{user} - Credits:{credits}")

#For on_login hook
def successful_logout():
    current_user = frappe.get_doc("User", frappe.session.user)
    print("USER Type after logout:", current_user.full_name)