# Copyright (c) 2026, SD and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Members(Document):
	
	def autoname(self):
		self.name = frappe.model.naming.make_autoname("MEM-.YYYY.-.#####")

	def before_insert(self):
		if not self.join_date:
			self.join_date = frappe.utils.today()

	def before_validate(self):
		if self.email:
			self.email = self.email.strip().lower()

	# def validate(self):
	# 	if self.phone and len(self.phone) != 12:
	# 		frappe.throw("Phone must be 12 chars")

	def before_submit(self):
		self.status = "Active"

	def after_insert(self):
		logger = frappe.logger("memberLogs")
		logger.info(f"New member profile created for {self.member_name}")

	# def on_update(self):
