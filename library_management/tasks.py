import frappe

def daily_maintanence():
    frappe.log_error("Daily Maintanence scheduler is Running...")

def resolver_website_path(path):
    if path == "test":
        return  "path_resolve"

    return path

# def message_print():
#     frappe.log_error(
#         title="Scheduler Test",
#         message="Scheduler executed"
#     )