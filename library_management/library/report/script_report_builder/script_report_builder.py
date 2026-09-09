# Copyright (c) 2026, SD and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    columns = [
        {
            "label": "Email",
            "fieldname": "email",
            "fieldtype": "Data",
            "width": 250,
        },
        {
            "label": "Membership Type",
            "fieldname": "membership_type",
            "fieldtype": "Data",
            "width": 180,
        },
        {
            "label": "Amount",
            "fieldname": "amount",
            "fieldtype": "Currency",
            "width": 120,
        },
        {
            "label": "Status",
            "fieldname": "status",
            "fieldtype": "Data",
            "width": 120,
        },
    ]

    data = [
        {
            "email": "alice@example.com",
            "membership_type": "Premium",
            "amount": 1500,
            "status": "Active",
        },
        {
            "email": "bob@example.com",
            "membership_type": "Basic",
            "amount": 500,
            "status": "Inactive",
        },
        {
            "email": "charlie@example.com",
            "membership_type": "Premium",
            "amount": 1500,
            "status": "Active",
        },
    ]

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