from openupgradelib import openupgrade, openupgrade_180
import logging
_logger = logging.getLogger(__name__)


def convert_company_dependent(env):
    _logger.info('=================================== convert property_payment_bank_account')
    openupgrade_180.convert_company_dependent(
        env, "res.partner", "property_payment_bank_account"
    )

def set_discuss_chanel_to_read(env):
    _logger.info("*********************************** set_discuss_chanel_to_read")
    env.cr.execute(
        """
        UPDATE discuss_channel_member SET fold_state = 'closed';
        """
    )


@openupgrade.migrate()
def migrate(env, version):
    convert_company_dependent(env)
    set_discuss_chanel_to_read(env)
