from openupgradelib import openupgrade, openupgrade_180
import logging
_logger = logging.getLogger(__name__)


@openupgrade.migrate()
def migrate(env, version):
    # Odoo plante lorsqu'il essaye de transformer le type de la colonne is_probono_partner de Boolean à JSON car Postgres était buggé et n'arrivait pas à caster un Booléen null en JSONB
    # https://www.postgresql.org/message-id/flat/376008.1737733733%40sss.pgh.pa.us#8ae16f9be6a9c5f2b1763f1a4ca65290

    # Dans la base TAZ1 cette colonne existe déjà car elle était alimentée avant que l'attribut is_probono_partner deviennt company_dependant=True : https://github.com/taz-paris/taz-odoo/commit/cd80ae60f7267334fdeefeb559a26e33e6bbb08c

    #La requête suivante prépare la BDD pour que l'ORM ne plante pas lors de la conversion
    #openupgrade.logged_query( env.cr, f"ALTER TABLE res_partner ALTER COLUMN is_probono_partner DROP DEFAULT, ALTER COLUMN is_probono_partner TYPE jsonb USING is_probono_partner::jsonb", )
    openupgrade.logged_query( env.cr, f"ALTER TABLE res_partner DROP COLUMN is_probono_partner", )
