from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
user = Table('user', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('role', SMALLINT),
    Column('group_id', INTEGER),
    Column('login', VARCHAR(length=64)),
    Column('password_hash', VARCHAR(length=128)),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('role', SmallInteger, default=ColumnDefault(0)),
    Column('username', String(length=64)),
    Column('password_hash', String(length=128)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['user'].columns['group_id'].drop()
    pre_meta.tables['user'].columns['login'].drop()
    post_meta.tables['user'].columns['username'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['user'].columns['group_id'].create()
    pre_meta.tables['user'].columns['login'].create()
    post_meta.tables['user'].columns['username'].drop()
