import frappe

current_user = frappe.session.user

user_doc = frappe.get_doc("User", frappe.session.user)
first_name = user_doc.first_name

def get_context(context):
    context.http_status_code = 405
    context.user_message = f"Hello {first_name}, you are not authorized to access this page."