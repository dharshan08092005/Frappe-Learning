// Copyright (c) 2026, SD and contributors
// For license information, please see license.txt

frappe.ui.form.on("Villain", {
    onload(frm) {
        frm.ignore_doctypes_on_cacell_all = ["Heros"]
    },
});
