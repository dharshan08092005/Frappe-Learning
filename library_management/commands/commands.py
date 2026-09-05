import frappe
import click


@click.command("get-site-apps")
@click.argument("site")
def get_site_apps(site):
    """Show all apps installed on a site."""

    frappe.init(site=site)
    frappe.connect()

    apps = frappe.get_installed_apps()

    for app in apps:
        click.echo(app)

    frappe.destroy()


#ASSIGNMENT CORRECT AH NA NUMBER THERIYALA BRO 1.....
#I PASSESD THIS IN INIT.PY
@click.command("hello-app")
def hello_app():
    """Say hello from this app."""
    
    click.echo("Hello from library_management app!")