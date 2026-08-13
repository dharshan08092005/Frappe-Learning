import frappe

def todo_query(user, doctype=None):
    if user == "Administrator":
        return ""

    return f"`tabToDo`.`owner` = {frappe.db.escape(user)}"