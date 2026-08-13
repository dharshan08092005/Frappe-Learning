// your_app/public/js/event_task_calendar.js

frappe.views.calendar['Sample Calendar'] = {
    // 1. Specify which fields hold the date/time values
    field_map: {
        "start": "completion_date",  // Field name for start time
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

    // 3. Optional: Add custom filters default options
    // filters: [
    //     {
    //         "fieldtype": "Link",
    //         "fieldname": "user",
    //         "options": "User",
    //         "label": __("Assigned User")
    //     }
    // ],

    // 4. Custom action when clicking an event on the calendar
    // get_events_method: "frappe.desk.doctype.event.event.get_events" // Custom server method (optional)
};