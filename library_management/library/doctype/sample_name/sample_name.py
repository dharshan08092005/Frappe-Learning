# Copyright (c) 2026, SD and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class SAmpleNAme(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		sample: DF.Data | None
		sample_link_to_test_document: DF.Link | None
	# end: auto-generated types

	pass
