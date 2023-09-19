import os
from types import SimpleNamespace
from typing import Optional, Union

from alembic.config import Config
from configargparse import Namespace

DEFAULT_DB_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/projectdatabase"

def make_alembic_config(cmd_opts: Union[Namespace, SimpleNamespace]) -> Config:
    # Replace path to alembic.ini file to absolute
    if not os.path.isabs(cmd_opts.config):
        cmd_opts.config = os.path.join(cmd_opts.config)

    config = Config(file_=cmd_opts.config, ini_section=cmd_opts.name,
                    cmd_opts=cmd_opts)

    # Replace path to alembic folder to absolute
    alembic_location = config.get_main_option('script_location')
    if not os.path.isabs(alembic_location):
        config.set_main_option('script_location',
                               os.path.join(alembic_location))
    if cmd_opts.url:
        config.set_main_option('sqlalchemy.url', cmd_opts.url)

    return config


def alembic_config_from_url(url: Optional[str] = None) -> Config:
    """
    Provides Python object, representing alembic.ini file.
    """
    cmd_options = SimpleNamespace(
        config='alembic.ini', name='alembic', url=url,
        raiseerr=False, x=None,
    )

    return make_alembic_config(cmd_options)