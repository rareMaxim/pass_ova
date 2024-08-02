# Copyright (c) 2024, Maxim S and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class PassCustomers(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		birthday: DF.Date | None
		description: DF.SmallText | None
		enterprice_manager: DF.Link | None
		enterprise: DF.Link | None
		full_name: DF.Data | None
		passport: DF.SmallText | None
		term_work_execution: DF.Date | None
	# end: auto-generated types

	pass
