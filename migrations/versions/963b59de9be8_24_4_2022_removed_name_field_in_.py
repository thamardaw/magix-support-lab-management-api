"""24_4_2022_removed_name_field_in_parameter_range

Revision ID: 963b59de9be8
Revises: 316f5e830c00
Create Date: 2022-04-24 23:40:23.166975

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '963b59de9be8'
down_revision = '316f5e830c00'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_lab_report_patient_id'), 'lab_report', ['patient_id'], unique=False)
    op.drop_column('parameter_range', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('parameter_range', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_index(op.f('ix_lab_report_patient_id'), table_name='lab_report')
    # ### end Alembic commands ###
