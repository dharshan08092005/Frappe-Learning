// Copyright (c) 2026, SD and contributors
// For license information, please see license.txt

frappe.ui.form.on("Sample Calendar", {
    refresh(frm) {
        frappe.views.calendar['Sample Calendar'] = {
            // 1. Specify which fields hold the date/time values
            field_map: {
                "start": "start_date",  // Field name for start time
                "end": "completion_date",      // Field name for end time
                "id": "name",              // Document ID
                "title": "task_name",        // Label to display on the calendar box
                "allDay": "all_day",       // (Optional) Checkbox field if it's an all-day event
            },

            // 2. Set dynamic colors based on document fields/status
            get_css_class: function (data) {
                if (data.status === "Completed") {
                    return "success"; // Applies green styling
                } else if (data.status === "Pending") {
                    return "danger";  // Applies red styling
                }
                return "warning";     // Default orange/yellow styling
            },
        };
    },
});



