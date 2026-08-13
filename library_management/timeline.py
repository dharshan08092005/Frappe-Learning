import frappe

def view_timeline(doctype, docname):
    return [
        {
            "creation": frappe.utils.now(),
            "content": """
                <div>Document Opened!!</div>
            """,
            # "template_data": {
            #     "message": f"{docname} was opened!"
            # }
        }
    ]