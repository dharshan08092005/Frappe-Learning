// your_app/public/js/department_tree.js

frappe.treeview_settings['Demo'] = {
    onload: function (treeview) {
        treeview.page.add_inner_button(__('Expand All'), function () {
            treeview.tree.load_children(treeview.tree.root_node, true);
        });
    },

    // Customize node rendering safely
    get_label: function (node) {
        // Handle variations across Frappe versions safely
        const name = node.value || (node.data && node.data.value) || '';
        const isGroup = node.is_group || (node.data && node.data.is_group);

        if (isGroup) {
            return `😵 <b>${frappe.router.slug(name)}</b>`;
        } else {
            return `📁 ${name}`;
        }
    },

    // toolbar: [
    //     {
    //         label: __('Custom Action'),
    //         condition: function (node) {
    //             return node.is_group || (node.data && node.data.is_group);
    //         },
    //         click: function (node) {
    //             const name = node.value || node.data.value;
    //             frappe.msgprint(`Clicked node: ${name}`);
    //         }
    //     }
    // ]
};