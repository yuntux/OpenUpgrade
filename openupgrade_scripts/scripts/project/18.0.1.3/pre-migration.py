from openupgradelib import openupgrade
import logging
_logger = logging.getLogger(__name__)

_field_renames = [
    ("project.project", "project_project", "analytic_account_id", "account_id"),
]

def ir_actions_act_window_view_project_duplicate(env):
    _logger.info("*********************************************************************** IR ACTION")
    env.cr.execute(
        """
        DELETE FROM ir_act_window_view
        WHERE (act_window_id=271 AND view_mode in ('kanban', 'list', 'tree'));
        """
    )


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.rename_fields(env, _field_renames)
    rule = env.ref(
        "project_todo.task_visibility_rule_project_user", raise_if_not_found=False
    )
    if rule:
        openupgrade.rename_xmlids(
            env.cr,
            [
                (
                    "project_todo.task_visibility_rule_project_user",
                    "project.task_visibility_rule_project_user",
                )
            ],
        )
    ir_actions_act_window_view_project_duplicate(env)
