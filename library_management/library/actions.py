import frappe

def on_assign(doc, method=None):
    frappe.throw(f"{doc.doctype} {doc.name} was assigned.")