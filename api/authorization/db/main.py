"""
Alembic wrapper. Utility to manage database.
Unlike alembic command is available anywhere and can work in any folder.

Accepts --db-url argument (or STAFF_DB_URL env variable), that is used instead
of sqlalchemy.url option in alembic.ini
"""
import argparse
import logging
from db.utils import make_alembic_config, DEFAULT_DB_URL
import os

from alembic.config import CommandLine

def main():
    logging.basicConfig(level=logging.DEBUG)

    alembic = CommandLine()
    alembic.parser.formatter_class = argparse.ArgumentDefaultsHelpFormatter
    alembic.parser.add_argument(
        '--url', help='Database url', default=os.getenv('DEFAULT_DB_URL', DEFAULT_DB_URL),
    )

    options = alembic.parser.parse_args()
    if 'cmd' not in options:
        alembic.parser.error('too few arguments')
        exit(128)
    else:
        config = make_alembic_config(options)
        exit(alembic.run_cmd(config, options))


if __name__ == '__main__':
    main()