import frappe

def get_context(context):
    context.no_cache = True
    context.title = "Article"
    articles = frappe.get_all("Article", filters={"status":"Published"},fields=["title", "name"])
    context.articles = articles

    return context
    