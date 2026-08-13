# Copyright (c) 2026, SD and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class SampleCalendar(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		completion_date: DF.Date | None
		start_date: DF.Date | None
		status: DF.Literal["Pending", "Started", "Completed"]
		task_name: DF.Data | None
	# end: auto-generated types

	
