import frappe

from frappe.core.doctype.sms_settings.sms_settings import send_sms

send_sms(
    receiver_list=["+919080155375"],
    msg="Hello from Frappe!"
)