frappe.listview_settings["Pass Customers"] = {
    hide_name_column: true, // hide the last column which shows the `name`
    hide_name_filter: true, // hide the default filter field for the name column
    add_fields: ['term_work_execution'],
    get_indicator(doc) {
        // customize indicator color
        let now = frappe.datetime.get_today();
        if (doc.term_work_execution >= now) {
            return [__("Дозволено"), "green", "term_work_execution,>=," + now];
        } else {
            return [__("Заборонено"), "darkgrey", "term_work_execution,<," + now];
        }
    },
};

