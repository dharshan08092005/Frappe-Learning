frappe.pages['demo-page'].on_page_load = function (wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Demo Page',
		single_column: true
	});
	page.set_title("Hello");
	page.set_title_sub("Subtitle"); //NW
	page.set_indicator("Pending", "red");
	// page.clear_indicator();

	let $btn = page.set_primary_action('New', () => create_new());

	let btn = page.set_secondary_action('New', () => {
		frappe.msgprint("Hello");
	}, 'octicon octicon-sync');

	// page.clear_primary_action();

	// page.clear_secondary_action();

	// add a normal menu item
	page.add_menu_item('Send Email', () => open_email_dialog())

	// add a standard menu item
	// page.add_menu_item('Send Email', () => open_email_dialog(), true)

	// page.clear_menu();

	// add a normal menu item
	page.add_action_item('Delete', () => delete_items())

	// page.clear_actions_menu()

	// add a dropdown button in a group
	page.add_inner_button('Update Posts');
	page.add_inner_button('New Post', () => new_post(), 'Make')
	page.add_inner_button('Old Post', () => new_post(), 'Make')

	// change type of ungrouped button
	// page.change_inner_button_type('New Post', 'Make', 'secondary');
	// page.change_inner_button_type('Update Posts', null, 'primary');

	page.remove_inner_button('New Post', 'Make');

	page.clear_inner_toolbar();

	//when you set mobile view and inside menu all the inner buttons are showing after page.clear_inner_toolbar()

	page.add_field(
		{
			label: "Name",
			fieldname: "name",
			fieldtype: "Data",
			default: "Sandeep",

		}
	);

	let values = page.get_form_values();
	console.log(values);

	// page.clear_fields();

}