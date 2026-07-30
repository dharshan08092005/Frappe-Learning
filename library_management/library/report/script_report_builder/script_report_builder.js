// Copyright (c) 2026, SD and contributors
// For license information, please see license.txt

frappe.query_reports["Script Report Builder"] = {
	filters: [
		{
			fieldname: "status",
			label: __("Status"),
			fieldtype: "Select",
			options: "\nDraft\nActive",
			default: ""
		}
	]
};
