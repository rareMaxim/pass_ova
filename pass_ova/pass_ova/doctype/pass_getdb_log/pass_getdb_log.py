# Copyright (c) 2024, Maxim S and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class PassGetDBLog(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		datetime: DF.Datetime | None
		device_model: DF.Data | None
		device_name: DF.Data | None
		device_uid: DF.Data | None
		device_username: DF.Data | None
		ip: DF.Data | None
		os_version: DF.Data | None
		package_build: DF.Data | None
		package_display_version: DF.Data | None
		package_filename: DF.Data | None
		package_id: DF.Data | None
		package_name: DF.Data | None
		package_version: DF.Data | None
	# end: auto-generated types

	pass
