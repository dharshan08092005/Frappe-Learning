import frappe
from frappe.contacts.doctype.address.address import Address

class CustomAddress(Address):

    def validate(self):
        super().validate()

        print("Custom Address Validation")

        if self.city:
            self.city = self.city.title()