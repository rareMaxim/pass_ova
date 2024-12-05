import datetime
import frappe
from frappe.utils import now_datetime, now
import frappe.utils
from pass_ova.pass_ova.doctype.pass_getdb_log.pass_getdb_log import PassGetDBLog

# Зберегти tokenAPI Secret: ac35f9826196880
# Key API: d5e6a11e755fee5


@frappe.whitelist(allow_guest=False)
def last_db_update() -> datetime:
    try:
        last_updated_doc = frappe.get_all(
            "Pass Customers",
            fields=["modified"],
            order_by="modified desc",
            limit=1,
        )
        if last_updated_doc:

            last_upd: frappe.utils.datetime.datetime = last_updated_doc[0].modified
            return last_upd.isoformat()
        else:
            return {"error": "No documents found"}
    except Exception as e:
        return {"error": str(e)}


@frappe.whitelist(allow_guest=True)
def load_db():
    # create a new document
    doc = frappe.get_doc(
        {
            "doctype": "Pass GetDB Log",
            "ip": frappe.request.headers.get("X-Real-Ip", ""),
            "datetime": frappe.utils.now_datetime(),
            "os_version": frappe.request.headers.get("os-version", ""),
            #  device
            "device_model": frappe.request.headers.get("device-model", ""),
            "device_name": frappe.request.headers.get("device-name", ""),
            "device_username": frappe.request.headers.get("device-username", ""),
            "device_uid": frappe.request.headers.get("device-uid", ""),
            "device_manufacturer": frappe.request.headers.get("device-manufacturer", ""),
            # Package
            "package_build": frappe.request.headers.get("PackageBuild", ""),
            "package_display_version": frappe.request.headers.get("PackageDisplayVersion", ""),
            "package_filename": frappe.request.headers.get("PackageFileName", ""),
            "package_id": frappe.request.headers.get("PackageID", ""),
            "package_name": frappe.request.headers.get("PackageName", ""),
            "package_version": frappe.request.headers.get("PackageVersion", ""),
        }
    )
    doc.insert(ignore_permissions=True)
    frappe.db.commit()

    customers = frappe.get_all(
        "Pass Customers",
        fields=[
            "name",
            "full_name",
            "birthday",
            "passport",
            "description",
            "enterprise",
        ],
        limit_page_length=10000,
        order_by="full_name asc",
    )
    for customer in customers:
        if customer.enterprise:
            enterprise_title = frappe.get_value(
                "Pass Enterprise", customer.enterprise, "enterprise_name"
            )
            customer.enterprise = enterprise_title
    result = {}
    result.update({"last_update": last_db_update()})
    result.update({"data": customers})

    return result
