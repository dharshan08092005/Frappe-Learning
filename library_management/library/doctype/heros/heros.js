// Copyright (c) 2026, SD and contributors
// For license information, please see license.txt

frappe.ui.form.on("Heros", {
    onload(frm) {
        frm.ignore_doctypes_on_cancel_all = ["Villain"]
    },
    // NOTE:Assignment 9
    refresh(frm) {
        let dialog = new frappe.ui.Dialog({
            title: "Assignment 9",
            fields: [
                {
                    label: "Task Subject",
                    fieldname: "task_subject",
                    fieldtype: "Data",
                    reqd: 1
                }
            ],
            primary_action_label: "Submit",
            primary_action(values) {
                frappe.call({
                    method: "library_management.api.accept_task_subject",
                    args: {
                        task_subject: values.task_subject
                    },
                    callback(r) {
                        dialog.hide();
                        frappe.msgprint({ message: "Submitted Successfully...", title: "Success", indicator: "green" });
                    }
                })
            }

        })

        dialog.show()
    }
});
