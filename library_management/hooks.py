app_name = "library_management"
app_title = "library_management"
app_publisher = "SD"
app_description = "library management system"
app_email = "voicepython1@gmail.com"
app_license = "mit"

export_python_type_annotations = True

#---------------------------------

# Only the last declared app_include_js works SO DECLRAE IN LIST
# app_include_js = "custom.bundle.js"
# app_include_js = "custom_deck.bundle.js"

#NOTE: JS FILE SHOULD END WITH .bundle.js

app_include_js = [
    'custom.bundle.js',
    'custom_deck.bundle.js'
]

# ---------------------------------------------

#NOTE: app_include_css
#NOTE: CSS FILE SHOULD END WITH .bundle.css

app_include_css = "custom.bundle.css"

# ---------------------------------------------

#NOTE: web_include_js
#NOTE: CSS FILE SHOULD END WITH .bundle.css

# web_include_js = "web_demo.bundle.js"

# ---------------------------------------------

#NOTE: web_include_cs
#NOTE: CSS FILE SHOULD END WITH .bundle.css

# web_include_css = "web_demo.bundle.css"

# ---------------------------------------------

#NOTE: webform_include_js

# webform_include_js = {
#     'Members': 'public/js/web_demo.bundle.js'
# }

# ---------------------------------------------

#NOTE: webform_include_css

# webform_include_css = {
#     'Members': 'public/css/web_demo.bundle.css'
# }

# ---------------------------------------------

#NOTE: page_js

# page_js = {
#     'demo-page': 'public/js/demo_page.bundle.js'
# }

# ---------------------------------------------

#NOTE: sounds

sounds = [
    {"name":"eagle", "src":"/assets/library_management/sounds/koiroylers-eagle-355831.mp3", "volume":0.1}
]


# ---------------------------------------------

#NOTE: override_email_send

override_email_send = "library_management.custom_email.send"
get_sender_details = "library_management.custom_email.get_sender_details"



# ---------------------------------------------

#NOTE: extend_bootinfo

extend_bootinfo = "library_management.boot.boot_session"

# ---------------------------------------------

#NOTE: website_context see demo web page

# website_context = {
#     "company_name" : "SD enterprise",
#     "favicon1" : "/assets/library_management/images/favicon.png",
# }

# ---------------------------------------------

#NOTE: update_website_context - For add dynamic value to website pages

# update_website_context = "library_management.overrides.overrides.update_website_context"

# ---------------------------------------------

#NOTE: extend_website_page_controller_context

# extend_website_page_controller_context = {
#     "frappe.www.404" : "library_management.www.404"
# }

#NOTE: get_web_pages_with_dynamic_routes

# get_web_pages_with_dynamic_routes = (
#     "library_management.scripts.get_web_pages_with_dynamic_routes"
# )

# ---------------------------------------------

#NOTE: get_web_pages_with_dynamic_routes

# website_clear_cache = (
#     "library_management.overrides.overrides.clear_website_cache"
# )

# ---------------------------------------------

#NOTE: website_redirects

# website_redirects = [
#     {"source":"/404","target":"frappe.utils.about"}
# ]

# ---------------------------------------------

#NOTE: website_route_rules

# website_route_rules = [
#     {
#         "from_route":"/test/<name>",
#         "to_route":"library_management.projects.project"
#     }
# ]

# ---------------------------------------------

#NOTE: website_path_resolver

# website_path_resolver = "library_management.tasks.resolver_website_path"

# ---------------------------------------------

#NOTE: website_catch_all -> all unknown paths are redirected to custom_404.html not working

# website_catch_all = "not_found"

# ---------------------------------------------

#NOTE: homepage -> website home page used to over ride default homepage refered as index.html not working

# home_page = "homepage"

# ---------------------------------------------

#NOTE: website user home page (by Role) not working
# role_home_page = {
# 	"Library Member": "test"
# }

# ---------------------------------------------

#NOTE: we can set home page for diff users
#NOTE:Priority: get_website_user_home_page > role_home_page > homepage

# get_website_user_home_page = "library_management.website.get_home_page"

# ---------------------------------------------

#NOTE: website user home page (by Role) not working
# standard_portal_menu_items = [
#     {
#         "title": "My Orders",
#         "route": "/sales-order",
#         "reference_doctype": "Sales Order",
#     }
# ]

# ---------------------------------------------

#NOTE: brand_html -> used when we need to version control navbar logo
brand_html = '''<div style = "display : flex; align-items: center;">
                    <img src="/assets/library_management/images/favicon.png" style = "width : 20px;height : 20px;">
                    <div style = "margin-left : 10px;">SD Enterprise</div>
                </div>'''


# ---------------------------------------------

#NOTE: in a WEB PAGE we can override default base.html using the base_template

# base_template = "library_management/templates/my_custom_base.html"


# ---------------------------------------------

#NOTE: we You can also customize base templates based on routes
# base_template_map = {
#     r"sales-order.*": "library_management/templates/base_template_map.html"
# }

# ---------------------------------------------

#NOTE: Used to remove app specific cache 
clear_cache = "library_management.cache.clear_cache"

# ---------------------------------------------

#NOTE: default_mail_footer add a footer to the mails sent via any email from frappe or app
default_mail_footer = """
                        <div>
                            Sent via <a href="https://voicepy.in" target="_blank">VoicePy</a>
                        </div>
                    """

# ---------------------------------------------

# Session Hooks
# on_login = "library_management.session.successful_login"
# on_session_creation = "library_management.session.allocate_free_credits"
# on_logout = "library_management.session.successful_logout"

# ---------------------------------------------

#NOTE: Scheduler -> run tasks at specific intervals
# Note: This will run all the tasks daily at 12:00 AM.
# The cron key is used to run tasks at specific intervals. ()

#NOTE: short worker -> hourly, daily, weekly, monthly
#NOTE: long worker -> hourly_long, daily_long, weekly_long, monthly_long
#NOTE: all -> Triggered every 60 seconds, This can be configured via the scheduler_tick_interval key in common_site_config.json

scheduler_events = {
    'daily': [
        'library_management.tasks.daily_maintanence'
    ],
    'cron':{
        "* * * * *":[
            "library_management.api.trigger_socket"
        ]
    }
}

# ---------------------------------------------

additional_timeline_content = {
    "*": [
        "library_management.timeline.view_timeline"
    ]
}

# ---------------------------------------------

#NOTE: override_whitelisted_methods -> 

# override_whitelisted_methods = {
#     "frappe.client.get_count":"library_management.library.api.custom_get_count"
# }

# ---------------------------------------------

#NOTE: DOCUMENT EVENTS

# doc_events = {
#     "ToDo" : {
#         "validate" : "library_management.library.api.validate"
#     }
# }

# ---------------------------------------------

#NOTE: include js in doctype views

# doctype_js = {
#     "Test Document": "public/js/test_document.js",
# }

# doctype_list_js = {"Members" : "public/js/doctype_list.bundle.js"}
# doctype_tree_js = {"Demo" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}



# ---------------------------------------------

#NOTE: send_sms

# send_sms = "library_management.overrides.sms.send_sms"

# override_doctype_class = {
#     "Address" : "library_management.overrides.address.CustomAddress" 
# }

# extend_doctype_class = {
#     "Address" : ["library_management.extensions.address.AddressMixin"]
# }

# ---------------------------------------------

#NOTE:Fixtures

# fixtures = [
#     "ToDo",
#     {"dt":"Test Document", "filters":[["description","like","D%"]]}
# ]

#NOTE: permission_query_conditions

permission_query_conditions = {
    "ToDo": "library_management.permissions.todo_query"
}

# auto_cancel_exempted_doctypes = ["Heros"]

#NOTE: JINJA

jinja = {
    "methods":[
        "library_management.jinja.methods",
        "library_management.utils.get_fullname"
    ],

    "filters":[ 
        "library_management.jinja.filters",
        "library_management.utils.format_currency",

    ]
}

#NOTE: Notification config

notification_config = "library_management.notification.get_config"


#NOTE:user_data_fields

user_data_fields = [
    {
        "doctype" : "Student",
        "filter_by" : "email",
        "strict" : True,
        "redact_fields":["phone", "name"]
    }
]


#NOTE: signup_form_template

signup_form_template = "library_management/templates/signup-form.html"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
add_to_apps_screen = [
    {
        "name": "Library",
        "logo": "/assets/library_management/images/favicon.png",
        "title": "Library Management",
        "route": "/library_management",
        "has_permission": "library_management.api.has_app_permission"
    }
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/library_management/css/library_management.css"
# app_include_js = "/assets/library_management/js/library_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/library_management/css/library_management.css"
# web_include_js = "/assets/library_management/js/library_management.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "library_management/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}



# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "library_management/public/images/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"


# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Books"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "library_management.utils.jinja_methods",
# 	"filters": "library_management.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "library_management.install.before_install"
# after_install = "library_management.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "library_management.uninstall.before_uninstall"
# after_uninstall = "library_management.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "library_management.utils.before_app_install"
# after_app_install = "library_management.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "library_management.utils.before_app_uninstall"
# after_app_uninstall = "library_management.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "library_management.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "library_management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"library_management.tasks.all"
# 	],
# 	"daily": [
# 		"library_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"library_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"library_management.tasks.weekly"
# 	],
# 	"monthly": [
# 		"library_management.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "library_management.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "library_management.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "library_management.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "library_management.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# when you link a doctype with another
# ex: book and book_review is cretated and you link book with review book_review doctype
# when you try to delete a book normally it will throw error as referred in book_review doctype
# when u use this hook it get overrided

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
before_request = ["library_management.utils.before_request"]
after_request = ["library_management.utils.after_request"]

# Job Events
# ----------
# before_job = ["library_management.utils.before_job"]
# after_job = ["library_management.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"library_management.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

default_log_clearing_doctypes = {
	"Notification Log": 1  # days to retain logs
}

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

sqlite_search = ["library_management.search.MyAppSearch"]