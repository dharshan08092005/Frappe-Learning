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
def greett():
    return "hello"

@frappe.whitelist()
def trigger_socket():
    data = {
        "label": frappe.utils.now_datetime().strftime("%H:%M:%S"),
        "value": random.randint(1, 100)
    }

    frappe.publish_realtime(
        "temperature_event",
        message=data
    )

    return data
    
import frappe

logger = frappe.logger("student_api", allow_site=True)


@frappe.whitelist()
def greet(name):
    logger.info("===== GREET FUNCTION STARTED =====")
    logger.info(f"greet API called with name={name}")

    message = f"Hello {name}"

    logger.info(f"Returning message: {message}")

    return message

@frappe.whitelist(allow_guest=True, rate_limit=10)
def limited_greeting():
    logger = frappe.logger()
    logger.info("Endpoint Called")
    frappe.response['message'] = "Hello, Rate Limited World!"
