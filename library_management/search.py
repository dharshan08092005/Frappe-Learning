import frappe

from frappe.search.sqlite_search import SQLiteSearch


class MyAppSearch(SQLiteSearch):

    INDEX_NAME = "library_management_search.db"

    INDEX_SCHEMA = {
        "metadata_fields": [
            "name",
            "author",
            "aadhar",
            "price"
        ],
        "tokenizer": "unicode61 remove_diacritics 2 tokenchars '-_'",
    }

    INDEXABLE_DOCTYPES = {
        "Books": {
            "fields": [
                "name",
                {"title": "title"},
                {"content": "title"},
                "author",
                "aadhar",
                "price",
            ],
        },
    }

    def get_search_filters(self):
        accessible_books = frappe.get_all(
            "Books",
            pluck="name",
        )

        if not accessible_books:
            return {
                "name": []
            }

        return {
            "name": accessible_books
        }