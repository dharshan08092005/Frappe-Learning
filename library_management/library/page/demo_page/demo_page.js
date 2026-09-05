// frappe.pages['demo-page'].on_page_load = function (wrapper) {
// 	var page = frappe.ui.make_app_page({
// 		parent: wrapper,
// 		title: 'Demo Page',
// 		single_column: true
// 	});
// 	page.set_title("Hello");
// 	page.set_title_sub("Subtitle"); //NW
// 	page.set_indicator("Pending", "red");
// 	// page.clear_indicator();

// 	let $btn = page.set_primary_action('New', () => create_new());

// 	let btn = page.set_secondary_action('New', () => {
// 		frappe.msgprint("Hello");
// 	}, 'octicon octicon-sync');

// 	// page.clear_primary_action();

// 	// page.clear_secondary_action();

// 	// add a normal menu item
// 	page.add_menu_item('Send Email', () => open_email_dialog())

// 	// add a standard menu item
// 	// page.add_menu_item('Send Email', () => open_email_dialog(), true)

// 	// page.clear_menu();

// 	// add a normal menu item
// 	page.add_action_item('Delete', () => delete_items())

// 	// page.clear_actions_menu()

// 	// add a dropdown button in a group
// 	page.add_inner_button('Update Posts');
// 	page.add_inner_button('New Post', () => new_post(), 'Make')
// 	page.add_inner_button('Old Post', () => new_post(), 'Make')

// 	// change type of ungrouped button
// 	// page.change_inner_button_type('New Post', 'Make', 'secondary');
// 	// page.change_inner_button_type('Update Posts', null, 'primary');

// 	page.remove_inner_button('New Post', 'Make');

// 	page.clear_inner_toolbar();

// 	//when you set mobile view and inside menu all the inner buttons are showing after page.clear_inner_toolbar()

// 	page.add_field(
// 		{
// 			label: "Name",
// 			fieldname: "name",
// 			fieldtype: "Data",
// 			default: "Sandeep",

// 		}
// 	);

// 	let values = page.get_form_values();
// 	console.log(values);

// 	// page.clear_fields();


// 	$(wrapper).find(".layout-main-section").html(`
//         <div id="test-event" style="margin-top: 20px;"></div>
//     `);

// 	const data = {
// 		labels: [],
// 		datasets: [
// 			{
// 				name: "Temperature",
// 				values: []
// 			}
// 		]
// 	};

// 	const chart = new frappe.ui.RealtimeChart(
// 		document.getElementById("test-event"),
// 		"test_event",
// 		8,
// 		{
// 			title: "Realtime Test",
// 			data: data,
// 			type: "line",
// 			height: 300
// 		}
// 	);
// 	chart.start_updating();
// }
// frappe.pages["demo-page"].on_page_load = function (wrapper) {

//     let page = frappe.ui.make_app_page({
//         parent: wrapper,
//         title: "Realtime Chart Test",
//         single_column: true
//     });

//     $(wrapper).find(".layout-main-section").html(`
//         <div id="realtime-chart" style="margin-top: 20px;"></div>
//     `);

//     const data = {
//         datasets: [
//             {
//                 name: "Temperature",
//                 values: []
//             }
//         ]
//     };

//     const chart = new frappe.ui.RealtimeChart(
//         "#realtime-chart",
//         "temperature_event",
//         8,
//         {
//             title: "Realtime Temperature",
//             data: {
//                 datasets: [
//                     {
//                         name: "Temperature",
//                         values: []
//                     }
//                 ]
//             }
//         }
//     );

//     chart.start_updating();
// };
frappe.pages["demo-page"].on_page_load = function (wrapper) {

    let page = frappe.ui.make_app_page({
        parent: wrapper,
        title: "Realtime Chart Test",
        single_column: true
    });

    $(wrapper).find(".layout-main-section").html(`
        <div id="realtime-chart" style="margin-top: 20px;"></div>
    `);

    const data = {
        title: "Realtime Temperature",

        data: {
            labels: [
                "10:00",
                "10:01",
                "10:02",
                "10:03",
                "10:04"
            ],
            datasets: [
                {
                    name: "Temperature",
                    values: [22, 24, 23, 25, 27]
                }
            ]
        },

        type: "line"
    };

    const element = document.querySelector("#realtime-chart");

    const chart = new frappe.ui.RealtimeChart(
        element,
        "temperature_event",
        40,
        data
    );

    chart.start_updating();

    const datas = [["10:06", 22], ["10:07", 23], ["10:08", 24], ["10:09", 20], ["10:10", 24], ["10:11", 27], ["10:12", 23], ["10:13", 20], ["10:14", 24], ["10:15", 27]]

    for (let i = 0; i < datas.length; i++) {
        setTimeout(() => {
            chart.update_chart(
                datas[i][0],
                [datas[i][1]]
            );
        },(i+1) * 1000);
    }
};