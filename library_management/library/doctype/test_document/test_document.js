// Copyright (c) 2026, SD and contributors
// For license information, please see license.txt

frappe.ui.form.on("Test Document", {
    refresh(frm) {
        console.log("eagle");
        frappe.utils.play_sound("eagle");
    },
});

window.view_test = function (args) {
    console.log("Opening:", args.name);

    frappe.set_route(
        "Form",
        "Test Document",
        args.name
    );
};