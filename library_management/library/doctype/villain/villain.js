// Copyright (c) 2026, SD and contributors
// For license information, please see license.txt

frappe.ui.form.on("Villain", {
    // onload(frm) {
    //     frm.ignore_doctypes_on_cacell_all = ["Heros"]
    // },
    //ASSIGNMENT 10
    //js-frappe-realtime Assignment
    setup(frm) {
        let dialog = new frappe.ui.Dialog({
            title: "Get First Name",
            fields: [
                {
                    label: "First Name",
                    fieldname: "first_name",
                    fieldtype: "Data"
                }
            ],
            primary_acton_label: "Submit",
            primary_action(values) {
                frappe.new_doc('Villain', { "villain_name": values.first_name });
                dialog.hide();
            }
        })
        dialog.show();
    },
});
