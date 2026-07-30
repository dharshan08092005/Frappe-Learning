# Copyright (c) 2026, SD and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    filters = filters or {}

    report = frappe.get_doc("Report", "Script Report Builder")

    columns = get_columns(report)
    data = get_data(report, filters)

    return columns, data


def get_columns(report):
    columns = []

    for col in report.columns:
        columns.append({
            "label": col.label,
            "fieldname": col.fieldname,
            "fieldtype": col.fieldtype,
            "width": 180,
        })

    return columns


def get_data(report, filters):
    conditions = {}

    # Read all filters dynamically
    for f in report.filters:
        value = filters.get(f.fieldname)

        if value not in (None, "", []):
            conditions[f.fieldname] = value

    # Read all columns dynamically
    fields = [c.fieldname for c in report.columns]

    if not fields:
        fields = ["name"]

    return frappe.get_all(
        report.ref_doctype,
        filters=conditions,
        fields=fields,
    )