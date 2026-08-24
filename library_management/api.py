import frappe
from library_management.search import MyAppSearch
import random

@frappe.whitelist(allow_guest=True)
def new_sign_up(username, email, phone):
    doc = frappe.get_doc({
        "doctype": "New Sign Up",
        "user_name": username,
        "email": email,
        "phone": phone
    })

    doc.insert(ignore_permissions=True)
    frappe.db.commit()

    return {
        "status": "success",
        "message": "Student created successfully"
    }


@frappe.whitelist()
def add(a,b):
    a+b


# library_management/api.py

def has_app_permission():
    return frappe.session.user == "Administrator"


@frappe.whitelist()
def test_language():
    frappe.log_error(
        title="Form Dict",
        message=str(frappe.form_dict)
    )

    return {
        "form_dict": frappe.form_dict,
        "lang": frappe.lang
    }

@frappe.whitelist()
def search(query, filters=None):
    search = MyAppSearch()
    res = search.search(query, filters=filters)
    return res


# NOTE: Assignment 9
@frappe.whitelist()
def accept_task_subject(task_subject):
    doc = frappe.new_doc("ToDo")
    doc.description = task_subject
    
    doc.save()

    return doc.name


@frappe.whitelist()
def greet():
    return "hello"

def trigger_socket():
    frappe.publish_realtime(
        event="test_event",
        message={
            "label": frappe.utils.now_datetime().strftime("%H:%M"),
            "value": random.randint(1, 100)
        }
    )