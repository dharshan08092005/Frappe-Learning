frappe.ui.form.on("JS API", {
    // setup(frm){
    //     frappe.msgprint(`Doc ${frm.doc.name} has been setup`);
    // },
    // before_load(frm){
    //     frappe.msgprint("New Doc is going to be loaded!");
    // }
    // on_load(frm) {
    //     frappe.msgprint(frm.doc.title);
    // }
    // onload_post_render(frm) {
    //     frappe.msgprint("Form has been loaded and rendered and this message is available!");
    // }
    // refresh(frm){
    // frm.email_doc(`Hello ${frm.doc.user_name}`);
    // frappe.msgprint("Hello !");
    // }    
    // validate(frm) {
    //     if (frm.doc.email.length != 12) {
    //         frappe.msgprint({ message: `${frm.doc.email}`, title: "Error ye!", raise_exception: true, indicator: "red" });
    //     }
    // }
    // before_save(frm) {
    //     if (frm.doc.email.length == 0) {
    //         frappe.throw("Give email ID");
    //     }
    // }
    // after_save(frm) {
    // frappe.msgprint("Hello worlds !");
    // frm.reload_doc();
    // frm.doc.email = "Hello world";
    // frm.refresh_field('email');
    // }
    // timeline_refresh(frm){
    //     frappe.msgprint("Time line success...");
    // }
    // list_on_form_rendered(frm){
    //     frappe.msgprint("List on form rendered...");
    // }
    // email(frm) {
    // frappe.msgprint(`Value is changed ${frm.doc.email}`);
    // frm.reload_doc();
    // frm.refresh_field('email');
    // }

    // CHILD DOC EVENTS
    // before_list_remove(frm, cdt, cdn) {
    //     console.log(`Child doc ${cdn} is removed`);
    // },
    // list_add(frm, cdt, cdn) {
    //     let row = frappe.get_doc(cdt, cdn);

    //     frappe.msgprint(
    //         `New row added. Row name: ${row.name}`
    //     );
    // },
    // list_remove(frm, cdt, cdn) {
    //     frappe.msgprint(`Child doc ${frm.doc.list[0].name} is removed`);
    // },
    // list_move(frm, cdt, cdn){
    //     frappe.msgprint("Moving....");
    // }

    //FORM API
    // after_save(frm) {
    //     frm.set_value("email", "sd@ex.com").then(
    //         () => {
    //             frappe.msgprint("email changed");
    //             if (frm.doc.docstatus === 1) {
    //                 frm.save('Cancel');
    //             }
    //         }
    //     )
    // }

    // refresh(frm){
    // frm.email_doc(`Hello ${frm.doc.user_name}`);
    // },

    // refresh(frm) {
    //     toggle_save_button(frm);
    // },
    // user_name(frm){
    //     toggle_save_button(frm);
    // }

    // email(frm){
    //     if (frm.is_dirty()) {
    //         frappe.show_alert('Please save form before attaching a file');
    //     }
    // }

    // refresh(frm) {
    //     frm.doc.email = "hello";
    //     frm.dirty();
    //     frm.save();
    // }

    // onload_post_render(frm) {
    //     // add custom button only if form is not new
    //     if (frm.is_new()) {
    //         frm.add_custom_button('Click me', () => frappe.show_alert("Click me clicked!!!"));
    //     }
    // }

    // onload(frm) {
    //     if (!frm.doc.user_name) {
    //         frm.set_intro('Please set the value of description', 'orange');
    //     }
    // }

    // before_save(frm) {
    //     frm.set_df_property("user_name", "reqd", 1);
    //     frm.refresh_field("user_name");
    // },

    onload_post_render(frm) {

        frm.add_custom_button('Add Name', () => {
            frm.set_value("user_name", "Sandeep");
        }, 'Set Value');
        frm.add_custom_button('Add Address', () => {
            frm.set_value("email", "Sandeep@ex.com");
        }, 'Set Value');
        frm.add_custom_button('Add Phone', () => {
            frm.set_value("phone", "7348075914");
        }, 'Set Value');
        frm.add_custom_button('Add Details', () => {
            frm.set_value("user_name", "Sandeep");
            frm.set_value("email", "Sandeep@ex.com");
            frm.set_value("phone", "7348075914");
        }, 'Set Value');

        frm.change_custom_button_type('Add Details', 'Set Value', 'primary');
        // frm.change_custom_button_type('Add Address', 'Set Value', 'primary');
        // frm.change_custom_button_type('Add Phone', 'Set Value', 'success');

        frm.add_custom_button("Go to", () => {
            // frappe.set_route("List", "JS API", "List", { "user_name": "Dharshan" });
            frappe.set_route("List/Demo/Calendar");
        })
    },

    // email(frm) {
    //     let email = frm.doc.email
    //     frm.toggle_enable("phone", (!email) ? false : true);
    // },
    // refresh(frm) {
    //     let email = frm.doc.email
    //     frm.toggle_enable("phone", (!email) ? true : false);
    // }

    // refresh(frm) {
    //     frm.toggle_reqd('email', !frm.doc.user_name);
    // }


    //setup or onload only......
    // setup(frm) {
    //     frm.set_query("members", () => {
    //         return {
    //             filters: {
    //                 membership_type: "Free",
    //                 status:"Active"
    //             }
    //         }
    //     })
    // }

    // onload_post_render(frm) {
    //     frm.add_child("list", {
    //         product: "item1",
    //         price: 120,
    //     });
    //     frm.refresh_field("list");
    // }

    // onload(frm) {
    //     frm.call("get_count", { throw_if_missing: true }).then((val) => {
    //         // frappe.msgprint(val);
    //         console.log(val)
    //         frm.add_child("list", {
    //             product: "Total Records",
    //             price: val.message.count
    //         }); 
    //         frm.refresh_field("list");
    //     })
    // }

    // refresh(frm) {
    //     frm.add_custom_button("Get selected", () => {
    //         let selected = frm.get_selected();
    //         console.log("selected : ", selected);
    //     })
    // }

    // refresh(frm) {
    //     let dialog = new frappe.ui.Dialog({
    //         title: "Form dialog",
    //         fields: [
    //             {
    //                 label: "User Name",
    //                 fieldname: "user_name",
    //                 fieldtype: "HTML"
    //             },
    //         ]
    //     })
    //     dialog.show();

    //     let wrapper = $(dialog.fields_dict.user_name.wrapper);
    //     wrapper.html(`<div class = "new-class" style = "background-color:red;"></div>`);

    //     let name = frappe.ui.form.make_control({
    //         parent: wrapper.find(".new-class"),
    //         df: {
    //             label: "User Name",
    //             fieldname: "new_user_name",
    //             fieldtype: "Data",
    //             reqd: true
    //         },
    //         render_input: true
    //     })
    // }

    // on_submit(frm) {
    //     frappe.meta.docfield_map["JS API"].email.formatter = (value) => {
    //         if (value === "Sandeep@ex.com") {
    //             return 'User Details Break';
    //         }
    //         else return value;
    //     }
    // },
    // refresh(frm) {
    //     frappe.add_custom_button("NEw", () => {
    //         frappe.require("/assets/library_management/js/utils.js", () => {
    //             console.log("Loaded!");
    //             hello_world();
    //             hello_world();
    //         });
    //         console.log("This runs immediately");
    //     })
    // },

    // refresh(frm){
    //     // console.log("Route:",frappe.get_route());
    //     frappe.prompt([
    //         {
    //             label:"Name",
    //             fieldname:"username",
    //             fieldtype:"Data"
    //         },
    //         {
    //             label:"Email",
    //             fieldname:"email",
    //             fieldtype:"Data"
    //         }
    //     ],(values) => {
    //         frappe.msgprint(values.username + "\n" + values.email);
    //     })
    // },

    // refresh(frm) {
    // frappe.confirm("Are you sure?",
    //     ()=>{
    //         frappe.msgprint("u clicked Yes");
    //     },
    //     ()=>{
    //         frappe.msgprint("u clicked No");
    //     }
    // )
    // frappe.warn('Are you surre you want to continue?',
    //     '<h2>Read through before you continue</h2>',
    //     () => {
    //         frappe.msgprint("You clicked Continue");
    //     },
    //     'Continue', //primary_label
    //     is_minimizable = true
    // )
    // frappe.show_alert({
    //     message:"Hello",
    //     indicator:"red",

    // },15)

    // frappe.show_progress('Loading..', 70, 100, 'Please wait');
    //BELOW DOES NOT WORK BCS THE METHOD EXPEXTS ONLY 4 ARGS....
    // frappe.show_progress({
    //     title:"Progress Test",
    //     count:10,
    //     total:100,
    //     description:"Heloo world description!"
    // })

    // },

    // setup(frm) {
    //     let dialog = new frappe.ui.Dialog({
    //         title: "Get First Name",
    //         fields: [
    //             {
    //                 label: "First Name",
    //                 fieldname: "first_name",
    //                 fieldtype: "Data"
    //             }
    //         ],
    //         primary_acton_label: "Submit",
    //         primary_action(values) {
    //             server_action: "library_management.library_management.api.greet",
    //                 // frappe.new_doc('JS API', { "user_name": values.first_name });
    //                 dialog.hide();
    //         }
    //     })
    //     dialog.show();
    // },

    // onload_post_render(frm){
    //     frappe.new_doc('JS API', { "user_name": "Sam" });
    // }

    // email(frm) {
    //     frm.set_value("email", frappe.format('2200-02-01', {
    //         fieldtype: 'Date',

    //     }));
    // }

    // refresh(frm) {
    //     new frappe.ui.form.MultiSelectDialog({
    //         doctype: "Members",
    //         target: frm,
    //         setters: {
    //             membership_type: "Free",
    //         },
    //         add_filters_group: true,
    //         // date_field: "join_date",
    //         columns: ["member_name", "membership_type", "join_date"],
    //         get_query() {
    //             return {
    //                 filters: { docstatus: ['!=', 2] }
    //             }
    //         },
    //         action(selections) {
    //             console.log(selections);
    //         }
    //     });
    // }

    // refresh(frm) {
    //     const d = new frappe.ui.Dialog({
    //         title: __("Create Logs"),
    //         fields: [
    //             {
    //                 fieldname: "logs",
    //                 fieldtype: "Table",
    //                 label: "Logs",
    //                 in_place_edit: true,
    //                 reqd: 1,
    //                 fields: [
    //                     {
    //                         fieldname: "log_type",
    //                         label: "Log Type",
    //                         fieldtype: "Select",
    //                         options: "IN\nOUT\n",
    //                         in_list_view: 1,
    //                         reqd: 1,
    //                     },
    //                     {
    //                         fieldname: "time",
    //                         label: "Time",
    //                         fieldtype: "Time",
    //                         in_list_view: 1,
    //                         reqd: 1,
    //                     }
    //                 ]
    //             }
    //         ],
    //         on_add_row: (idx) => {
    //             // idx = visible idx of the row starting from 1
    //             // eg. set `log_type` as alternating IN/OUT in the table on row addition
    //             let data_id = idx - 1;
    //             let logs = dialog.fields_dict.logs;
    //             let log_type = (data_id % 2) == 0 ? "IN" : "OUT";

    //             logs.df.data[data_id].log_type = log_type;
    //             logs.grid.refresh();
    //         },
    //         primary_action(values) {
    //             server_action:"library_management.library_management.api.new_sign_up"
    //         },
    //         primary_action_label:"Print"
    //     })
    //     d.show();
    // }

    // refresh(frm) {
    //     let dialog = new frappe.ui.Dialog({
    //         title: "Form dialog",
    //         fields: [
    //             {
    //                 label: "User Name",
    //                 fieldname: "user_name",
    //                 fieldtype: "HTML"
    //             },
    //         ]
    //     })
    //     dialog.show();

    //     let wrapper = $(dialog.fields_dict.user_name.wrapper);
    //     wrapper.html(`<div class = "new-class"></div>`);

    //     const chart = new frappe.ui.RealtimeChart(
    //         wrapper.find(".new-class"),
    //         "test_event",
    //         8,
    //         {
    //             labels: ["1", "2", "3", "4"],
    //             datasets: [
    //                 {
    //                     values: [5, 8, 3, 10]
    //                 }
    //             ]
    //         }
    //     );
    //     chart.show();
    // }

    // refresh(frm) {
    //     const scanner = new frappe.ui.Scanner({
    //         dialog: true,
    //         multiple: false,
    //         on_scan(data) {
    //             console.log("data :", data);
    //         }
    //     })
    // }

    refresh() {
        //get_doc
        // let doc = frappe.db.get_doc('JS API', null, filters = { "user_name": ["like", "S%"] }).then(
        //     (doc) => {
        //         console.log(doc);
        //     }
        // );
        //get_list
        // let doc1 = frappe.db.get_list("JS API", {
        //     fields:['user_name','email'],
        //     filters:{
        //         docstatus : ["!=",2]
        //     }
        // }).then((res)=>{
        //     console.log(res);
        // });
        //get_value
        // let doc2 = frappe.db.get_value("JS API","JSAPI-0015","phone").then((res)=>{
        //     console.log("get_value() single value:",res);
        // })
        //set_value
        frappe.db.set_value("JS API", "JSAPI-0015", "user_name","Somu Kumar").then((res)=>{
            console.log("set_value() single value:",res);
        });
    }
})

function toggle_save_button(frm) {
    if (!frm.doc.user_name) {
        frm.disable_save();
    } else {
        frm.enable_save();
    }
}