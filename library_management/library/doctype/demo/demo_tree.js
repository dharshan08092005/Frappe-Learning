// Copyright (c) 2026, SD and contributors
// For license information, please see license.txt

frappe.treeview_settings["Demo"] = {
    // Header
    breadcrumb: "Build",
    title: "Demo Tree",

    // Method that loads child nodes
    get_tree_nodes: "library_management.library.doctype.demo.demo.get_children",

    // Method called when adding a node
    add_tree_node: "library_management.library.doctype.demo.demo.add_node",

    // Dialog fields shown while creating a new node
    fields: [
        {
            fieldtype: "Data",
            fieldname: "demo_name",
            label: "Demo Name",
            reqd: true,
        },
        {
            fieldtype: "Data",
            fieldname: "description",
            label: "Description",
        },
        {
            fieldtype: "Check",
            fieldname: "is_group",
            label: "Is Group",
        },
    ],

    // Hide parent field (tree handles it automatically)
    ignore_fields: ["parent_demo"],

    // Extra menu item
    menu_items: [
        {
            label: "New Demo",
            action: () => frappe.new_doc("Demo"),
            condition: () =>
                frappe.boot.user.can_create.includes("Demo"),
        },
    ],

    // Triggered once when tree is loaded
    onload(treeview) {
        console.log("Demo Tree Loaded", treeview);
    },

    // After entire tree renders
    post_render(treeview) {
        console.log("Tree Render Complete");
    },

    // Called for every node rendered
    onrender(node) {
        console.log("Rendered:", node.label);
    },

    // After children are fetched from server
    on_get_node(nodes) {
        console.log("Fetched Nodes:", nodes);
    },

    // Show custom toolbar
    extend_toolbar: true,

    toolbar: [
        {
            label: "Add Child",
            btnClass: "hidden-xs",
            condition: node => node && node.expandable,
            click: node => frappe.treeview_settings["Demo"].add_node(node),
        },
    ],
};