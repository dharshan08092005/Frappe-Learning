import frappe

def get_context(context):
    context.name = frappe.form_dict.name
    print(context.name)