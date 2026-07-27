# Copyright (c) 2026, SD and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname

class DemoController(Document):
	
	# def before_insert(self):
	# 	frappe.msgprint(f"Before insert {self.hired}") #Before insert 0

	# def before_naming(self):
	# 	frappe.msgprint(f"Before naming {self.name}") #Before naming None
	# 	self.prefix = self.hitman_name

	# def autoname(self):
	# 	seq = make_autoname(".#####")
	# 	self.name = "HITMAN-" + self.prefix + "-" +seq

	# def before_validate(self):
	# 	frappe.msgprint(f"Before validate {self.salary}") #Before validate HITMAN-sam-00001
	# 	if self.salary < 1000 or not self.salary:
	# 		frappe.throw("Minimum Salary Must be greater than 1000.")
	# 	else:
	# 		frappe.msgprint(f"After before_validate is used {self.salary}") #After before_validate is used 2000.0


	# def validate(self):
	# 	if self.salary > 2000:
	# 		frappe.throw("Salary is Must be below 2000.")
	# 	else:
	# 		frappe.msgprint(f"after validate is used {self.salary}")
		
	# def before_save(self):


	def on_update(self):
		frappe.msgprint("Document is updating..")

	def on_submit(self):
		frappe.msgprint("Document is submitting...")

	def on_cancel(self):
		frappe.msgprint("Document is cancelling...")

	def on_update_after_submit(self):
		frappe.msgprint("Document editted after submit...")

	def on_change(self):
		frappe.msgprint("On change running...")
		if not self.hired:
			self.not_hired = 1
