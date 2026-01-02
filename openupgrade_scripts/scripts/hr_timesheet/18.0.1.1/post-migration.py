# Copyright 2025 Le Filament (https://le-filament.com)
# Copyright 2025 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from openupgradelib import openupgrade


def _convert_task_progress(env):
    """On v17, the value was multiplied by 100:

    https://github.com/odoo/odoo/blob/f9726cfe93e8850a38d9de06acfa5d78473b50b0/addons/hr_timesheet/models/project_task.py#L101

    but on v18, it's not:

    https://github.com/odoo/odoo/blob/1cac54db8634267a780b4011291f1e8a80ac5f5b/addons/hr_timesheet/models/project_task.py#L98

    so we have to divide current stored values by 100.
    """
    openupgrade.logged_query(
        env.cr, "UPDATE project_task SET progress = progress / 100"
    )

def _correct_user_id_stock(env):
	lines = env['account.analytic.line'].search([('employee_id', '!=', False)])
	for line in lines :
		if line.employee_id.user_id :
			if line.user_id != line.employee_id.user_id :
				line.user_id = line.employee_id.user_id.id

@openupgrade.migrate()
def migrate(env, version):
    openupgrade.load_data(env, "hr_timesheet", "18.0.1.1/noupdate_changes.xml")
    _convert_task_progress(env)
    _correct_user_id_stock(env)
