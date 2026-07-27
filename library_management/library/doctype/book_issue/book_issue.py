# Copyright (c) 2026, SD and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import today, add_days


class BookIssue(Document):
      def before_insert(self):
        if not self.issue_date:
             self.issue_date = today()	
                
      def validate(self):
        self.validate_book_in_list()
        self.validate_due_date()
        
      def validate_due_date(self):
         for row in self.books:
            if not row.due_date:
                 row.due_date = add_days(self.issue_date, 7)
          

      def validate_book_in_list(self):

        selected_books = set()

        for row in self.books:

            if row.book in selected_books:
                frappe.throw(f"{row.book} is already added.")

            selected_books.add(row.book)

      def on_update(self):

        for row in self.books:

            frappe.db.set_value(
                "Books",
                row.book,	
                "available",
                row.returned
            )

