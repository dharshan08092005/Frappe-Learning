# Copyright (c) 2026, SD and Contributors
# See license.txt

import frappe
from frappe.tests import IntegrationTestCase


# On IntegrationTestCase, the doctype test records and all
# link-field test record dependencies are recursively loaded
# Use these module variables to add/remove to/from that list
EXTRA_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]
IGNORE_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]



class IntegrationTestArticle(IntegrationTestCase):
	"""
	Integration tests for Article.
	Use this class for testing interactions between multiple components.
	"""

	def testArticleCreation(self):
		article = frappe.get_doc({
			"doctype":"Article",
			"title":"My First Test",
			"status":"Published"
		})

		article.insert(ignore_permissions=True)

		self.assertEqual(article.title, "My First Test")

		self.assertTrue(frappe.db.exists("Article", article.name))