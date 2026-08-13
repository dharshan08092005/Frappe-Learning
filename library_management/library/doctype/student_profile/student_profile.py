# Copyright (c) 2026, SD and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class StudentProfile(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		email: DF.Data | None
		name1: DF.Data | None
		pnone: DF.Phone | None
	# end: auto-generated types

	pass
