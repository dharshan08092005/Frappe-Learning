import frappe

def get_context(context):
    # Redirect guest users to login
    if frappe.session.user == "Guest":
        frappe.throw("Please log in to access this page", frappe.PermissionError)

    context.no_cache = 1
    context.show_sidebar = 1  # Renders the default portal sidebar

    # Fetch documents belonging to the logged-in user
    context.orders = frappe.get_all(
        "Sales Order",
        filters={"owner": frappe.session.user},
        fields=["name", "transaction_date", "grand_total", "status"]
    )

    return context