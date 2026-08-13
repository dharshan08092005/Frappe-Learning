# Copyright (c) 2026, SD and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class SalesOrder(WebsiteGenerator):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		order_item: DF.Data | None
		route: DF.Data | None
	# end: auto-generated types

	def before_save(self):
		# Automatically set the route field if not set
		if not self.route:
			self.route = f"sales-order/{self.name.lower()}"

	def has_website_permission(self, ptype="read", user=None):
		if not user:
			user = frappe.session.user

		return self.owner == user or user == "Administrator"

	def get_context(self, context):
		context.show_sidebar = True
		context.parents = [{"name": "My Portal", "route": "/me"}]