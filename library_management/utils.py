import frappe
from frappe.utils import add_days, today

def get_fullname(user):
    first_name = frappe.db.get_value("User", user, "first_name")
    return first_name

def format_currency(value, currency):
    return currency + " " + str(value)

def before_job(**kwargs):
    print("Background job is starting")
    frappe.logger("library_management").info(
        "Background job is starting"
    )


def after_job(**kwargs):
    frappe.logger("library_management").info(
        "Background job has finished"
    )
    print("Background job has finished")


def send_book_return_reminder():

    frappe.logger("library_management").info(
        "Checking book issues for reminders..."
    )

    # Find Book Issue records older than 14 days
    book_issues = frappe.get_all(
        "Book Issue",
        filters={
            "issue_date": ["<=", add_days(today(), -14)]
        },
        fields=["name", "member", "issue_date"]
    )

    for issue in book_issues:

        # Get the Member document
        member = frappe.get_doc("Members", issue.member)

        # Get books from the child table
        book_issue = frappe.get_doc("Book Issue", issue.name)

        for book in book_issue.books:

            frappe.logger("library_management").info(
                f"Reminder required for book {book.book} "
                f"issued to {member.member_name}"
            )

        # Send email if member has an email
        if member.email:
            frappe.sendmail(
                recipients=[member.email],
                subject="Book Return Reminder",
                message=f"""
                    <p>Hello {member.member_name},</p>
                    <p>
                        This is a reminder to return the books
                        issued on <b>{issue.issue_date}</b>.
                    </p>
                    <p>Thank you.</p>
                """
            )


def start_reminder():

    job = frappe.enqueue(
        "library_management.utils.send_book_return_reminder"
    )

    return job.id


def before_request():
    if frappe.local.request.path == "/api/method/library_management.api.add":
        frappe.log_error(
            title="Before Request",
            message=frappe.local.request.path
        )


def after_request(response):
    if frappe.local.request.path == "/api/method/library_management.api.add":
        frappe.log_error(
            title="After Request",
            message="Worked!"
        )
