// Copyright (c) 2026, SD and contributors
// For license information, please see license.txt

frappe.ui.form.on("Books", {
    // 	refresh(frm) {

    // 	},
    validate: function (frm) {
        if (frm.doc.author && frm.doc.author.length < 3) {
            frappe.msgprint("Author name is too short")
            frappe.validated = false;
        }
    }
});
