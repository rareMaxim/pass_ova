# Copyright (c) 2024, Maxim S and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class PassEnterprise(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		tax_id: DF.Data | None
		term_work_execution: DF.Date | None
	# end: auto-generated types

	pass
