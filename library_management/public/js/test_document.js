frappe.ui.form.on("Test Document", {
    refresh: function (frm) {
        frappe.msgprint(frm.doc.name);
    }
})