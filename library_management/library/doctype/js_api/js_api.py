# Copyright (c) 2026, SD and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class JSAPI(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from library_management.library.doctype.js_child.js_child import JSChild
		from library_management.library.doctype.js_multichild.js_multichild import JSMULTICHILD

		amended_from: DF.Link | None
		email: DF.Data | None
		list: DF.Table[JSChild]
		members: DF.TableMultiSelect[JSMULTICHILD]
		phone: DF.Phone | None
		user_name: DF.Data | None
	# end: auto-generated types

	@frappe.whitelist()
	def get_count(self):
		count = frappe.db.count("JS API")
		# frappe.msgprint(count)
		return {
			"count" : count
		}
