import frappe

def validate(doc, method):
    frappe.msgprint("Hook executed successfully")


@frappe.whitelist()
def update_member_status():

    members = frappe.qb.DocType("Members")
    book_issue = frappe.qb.DocType("Book Issue")

    records = (
        frappe.qb.from_(book_issue)
        .join(members)
        .on(book_issue.member == members.name)
        .select(
            book_issue.name,
            book_issue.member,
            members.member_name,
            members.status
        )
        .limit(3)
    ).run(as_dict=True)

    if not records:
        return "Empty....No records found!"


    # Document API
    if records:
        member_doc = frappe.get_doc(
            "Members",
            records[0]["member"]

        )

        member_doc.status = "Expired"
        member_doc.save()

    # Database API
    for row in records:
        frappe.db.set_value(
            "Members",
            row["member"],
            "status",
            "Bulk Updated",
            update_modified = False
        )

        frappe.db.commit()

        records = (
        frappe.qb.from_(book_issue)
        .join(members)
        .on(book_issue.member == members.name)
        .select(
            book_issue.name,
            book_issue.member,
            members.member_name,
            members.status
        )
        .limit(3)
    ).run(as_dict=True)

    return records

