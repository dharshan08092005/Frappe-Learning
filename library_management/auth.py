import frappe

def validate():
    if frappe.session.user == "Administrator":
        frappe.throw("This user is not allowed")
        