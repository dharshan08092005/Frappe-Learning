import frappe

def clear_cache():
    frappe.cache().hdel("app_specific_cache","test")
