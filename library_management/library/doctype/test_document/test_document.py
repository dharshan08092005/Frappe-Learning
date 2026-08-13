# Copyright (c) 2026, SD and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class TestDocument(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		description: DF.Data | None
	# end: auto-generated types

	def before_save(self):
		if not self.description:
			self.description = "Default Description"


	def on_update(self):
		#NOTE: DIALOG API 

		"""
		title - Title of the dialog : "Success"
		ex:
			┌──────────────────────────────┐
			│ Success                      │
			├──────────────────────────────┤
			│ Book issued successfully     │
			└──────────────────────────────┘
		-------------------------------------
		indicators - red, blue, green, orange
		-------------------------------------
		as_table - send multiple messages and show as table
			msg = [["msg1","val","val"], ["msg2"]]
			ex:
				| Name  | Age |
				| ----- | --: |
				| John  |  20 |
				| David |  22 |
				| Sam   |  21 |

		-------------------------------------
		as_list - send multiple messages and show as list
			msg = ["msg1","msg2"]
			ex:
				Available Books

                • Harry Potter
				• Atomic Habits
				• Clean Code
		-------------------------------------
		as_dict - send messages and show as table
			msg = [{"msg1":"val","val":"val"}, ["msg2"]]
			ex:
		-------------------------------------

		raise_exception: raises an exception and stops the further execution of the code

		-------------------------------------

		primary_action: we can set client/server side actions to be performed

		-------------------------------------

		alert: makes the modal to become alert at left corner and overrides primary_acition
		ex:
		                            ┌──────────────────────────┐
									│ ✓ Document inserted      │
									│   successfully           │
									└──────────────────────────┘

		-------------------------------------

		allow_dangerous_html: 
		"""
		message = """
			<h3>Library Rules</h3>

			<ul>
			<li>Books must be returned within 14 days.</li>
			<li>Damaged books will incur a fine.</li>
			<li>Students can borrow a maximum of 3 books.</li>
			<li>Books cannot be transferred to another student.</li>
			</ul>
		"""
		# data = ["Document Inserted successfully","Very Good","Do it so good"]

		data = [
			["Book", "Author", "Category", "Status", "Issued To", "Category", "Status", "Issued To"],
			["Clean Code", "Robert Martin", "Programming", "Issued", "John", "Category", "Status", "Issued To"],
			["Atomic Habits", "James Clear", "Self Help", "Available", "", "Category", "Status", "Issued To", "Category", "Status", "Issued To"]
		]
		frappe.msgprint(
			msg = message, 
			title = "Success",
			raise_exception = False, 
			as_table = True, 
			as_list = False,
			indicator = "green", 
			primary_action = {
				"label":"View Test",
				"client_action":"view_test",
				"args":{
					"name":"llvv8b05eb"
				}
			},
			alert = False,
			is_minimizable = False, 
			wide = False, 
			realtime = False,
			allow_dangerous_html = False
		)