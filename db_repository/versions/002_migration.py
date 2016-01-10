from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
faculty = Table('faculty', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('faculty_name', String(length=64)),
)

group = Table('group', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('faculty_id', Integer),
    Column('group_name', String(length=16)),
    Column('grouo_sum', Integer),
)

lesson = Table('lesson', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('start', Time),
    Column('end', Time),
)

schedule = Table('schedule', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('group_id', Integer),
    Column('day_of_week', Integer),
    Column('subject_id', Integer),
    Column('lesson_id', Integer),
)

subject = Table('subject', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('subject_name', String(length=64)),
)

week = Table('week', post_meta,
    Column('day_id', Integer, primary_key=True, nullable=False),
    Column('day_name', String(length=16)),
)

user = Table('user', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('nickname', VARCHAR(length=64)),
    Column('email', VARCHAR(length=120)),
    Column('role', SMALLINT),
    Column('group', VARCHAR(length=10)),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('role', SmallInteger, default=ColumnDefault(0)),
    Column('group_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['faculty'].create()
    post_meta.tables['group'].create()
    post_meta.tables['lesson'].create()
    post_meta.tables['schedule'].create()
    post_meta.tables['subject'].create()
    post_meta.tables['week'].create()
    pre_meta.tables['user'].columns['email'].drop()
    pre_meta.tables['user'].columns['group'].drop()
    pre_meta.tables['user'].columns['nickname'].drop()
    post_meta.tables['user'].columns['group_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['faculty'].drop()
    post_meta.tables['group'].drop()
    post_meta.tables['lesson'].drop()
    post_meta.tables['schedule'].drop()
    post_meta.tables['subject'].drop()
    post_meta.tables['week'].drop()
    pre_meta.tables['user'].columns['email'].create()
    pre_meta.tables['user'].columns['group'].create()
    pre_meta.tables['user'].columns['nickname'].create()
    post_meta.tables['user'].columns['group_id'].drop()
