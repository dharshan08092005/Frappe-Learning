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

})

function toggle_save_button(frm) {
    if (!frm.doc.user_name) {
        frm.disable_save();
    } else {
        frm.enable_save();
    }
}