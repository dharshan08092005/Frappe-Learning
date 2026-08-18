# Copyright (c) 2026, SD and contributors
# For license information, please see license.txt

import frappe
from frappe.utils.nestedset import NestedSet


class Demo(NestedSet):
	pass


@frappe.whitelist()
def get_children(parent=None, **kwargs):
	return frappe.get_all(
		"Demo",
		filters={"parent_demo": parent},
		fields=["name as value", "is_group as expandable"],
		order_by="name"
	)
	

@frappe.whitelist()
def add_node():
	args = frappe.form_dict
	doc = frappe.get_doc({
		"doctype": "Demo",
		"demo_name": args.demo_name,
		"parent_demo": args.parent,
		"is_group": args.is_group,
	}).insert()
	
	return doc
