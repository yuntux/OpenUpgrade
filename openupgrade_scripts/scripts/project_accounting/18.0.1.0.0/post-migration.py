from openupgradelib import openupgrade, openupgrade_180
import logging
_logger = logging.getLogger(__name__)

def convert_company_dependent(env):
    _logger.info('=================================== convert is_probono_partner')
    openupgrade_180.convert_company_dependent(
        env, "res.partner", "is_probono_partner"
    )


@openupgrade.migrate()
def migrate(env, version):
    convert_company_dependent(env)
