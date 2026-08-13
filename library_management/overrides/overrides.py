import frappe
from frappe.utils import now

def update_website_context(context):
    context.favicon1 = "/assets/library_management/images/GitProfile.jpg"
    context.time = now()

def clear_website_cache(path):
    if not path:
        print("Website cache cleared")
    else:
        frappe.msgprint(f"Cleared path for Path = {path}")
    