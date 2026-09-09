import frappe

def get_context(context):
    context.no_cache = True
    context.title = "Our Team"

    context.users = frappe.get_all(
        "User",
        filters={"enabled": 1},
        fields=["full_name", "name"]
    )