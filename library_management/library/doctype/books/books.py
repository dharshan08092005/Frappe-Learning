# Copyright (c) 2026, SD and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.naming import make_autoname

class Books(WebsiteGenerator):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		aadhar: DF.Autocomplete | None
		author: DF.Data | None
		available: DF.Check
		price: DF.Currency
		route: DF.Data | None
		title: DF.Data
	# end: auto-generated types

		def before_insert(self):
			# self.name = make_autoname("BOOK-.#####")
			name = self.title.lower()
			self.route = f"books/{name}"
