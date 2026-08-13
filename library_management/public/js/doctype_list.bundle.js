frappe.listview_settings['Members'] = {
    onload: function (listview) {
        // Custom button on the list view
        listview.page.add_inner_button(__('Send Notification'), function () {
            frappe.msgprint(__('Notification sent to selected members!'));
        });
    },

    // Format row indicators (e.g., status colors)
    get_indicator: function (doc) {
        if (doc.status === "Active") {
            return [__("Active"), "green", "status,=,Active"];
        } else {
            return [__("Draft"), "red", "status,=,Draft"];
        }
    }
};