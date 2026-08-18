frappe.listview_settings["Books"] = {
    add_fields: ["reference_type", "reference_name"],
    filters: [
        ["author", "=", "James Clear"]
    ],

    hide_name_column: true,

    formatters: {
        title(val) {
            return val.bold();
        },
        available(val) {
            return val ? true : false;
        }
    },
    button: {
        show(doc) {
            return true;
        },
        get_label() {
            return frappe.session.user;
        },
        get_description(doc) {
            return __("Description for the button")
        },
        action(doc) {
            frappe.set_route('Form', 'books', 'somu-story');
        }
    },
    dropdown_button: {
        get_label: __("Dropdown"),
        buttons: [{
            get_label: __("Button 1"),
            show: function (doc) {
                return true;
            },
            get_description: function (doc) {
                return "Open Button 1 " + doc.reference_name;
            },
            action: function (doc) {
                frappe.msgprint("Dropdown Button 1 Clicked " +
                    doc.reference_name);
            }
        },
        {
            get_label: __("Button 2"),
            show: function (doc) {
                return doc.status != "Closed";
            },
            get_description: function (doc) {
                return "Open Button 2 " + doc.reference_name;
            },
            action: function (doc) {
                frappe.msgprint("Dropdown Button 2 Clicked " +
                    doc.reference_name);
            }
        },
        {
            get_label: __("Button 3"),
            show: function (doc) {
                return doc.status != "Cancelled";
            },
            get_description: function (doc) {
                return "Open Button 3 " + doc.reference_name;
            },
            action: function (doc) {
                frappe.msgprint("Dropdown Button 3 Clicked " +
                    doc.reference_name);
            }
        }
        ]
    },
}