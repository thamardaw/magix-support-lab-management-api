"""init

Revision ID: d4b634d994d7
Revises: 
Create Date: 2022-05-08 15:54:49.575505

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4b634d994d7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lab_report',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_time', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_time', sa.DateTime(timezone=True), nullable=True),
    sa.Column('patient_id', sa.Integer(), nullable=False),
    sa.Column('doctor_name', sa.String(), nullable=True),
    sa.Column('smaple_id', sa.Integer(), nullable=True),
    sa.Column('sample_type', sa.String(), nullable=True),
    sa.Column('patient_type', sa.String(), nullable=True),
    sa.Column('test_date', sa.Date(), nullable=True),
    sa.Column('created_user_id', sa.Integer(), nullable=True),
    sa.Column('updated_user_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_lab_report_created_user_id'), 'lab_report', ['created_user_id'], unique=False)
    op.create_index(op.f('ix_lab_report_id'), 'lab_report', ['id'], unique=False)
    op.create_index(op.f('ix_lab_report_patient_id'), 'lab_report', ['patient_id'], unique=False)
    op.create_index(op.f('ix_lab_report_updated_user_id'), 'lab_report', ['updated_user_id'], unique=False)
    op.create_table('patient',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_time', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_time', sa.DateTime(timezone=True), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('gender', sa.Enum('male', 'female', name='gender_enum'), nullable=False),
    sa.Column('date_of_birth', sa.Date(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('contact_details', sa.String(), nullable=False),
    sa.Column('created_user_id', sa.Integer(), nullable=True),
    sa.Column('updated_user_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_patient_created_user_id'), 'patient', ['created_user_id'], unique=False)
    op.create_index(op.f('ix_patient_id'), 'patient', ['id'], unique=False)
    op.create_index(op.f('ix_patient_updated_user_id'), 'patient', ['updated_user_id'], unique=False)
    op.create_table('test_category',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_time', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_time', sa.DateTime(timezone=True), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('created_user_id', sa.Integer(), nullable=True),
    sa.Column('updated_user_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_test_category_created_user_id'), 'test_category', ['created_user_id'], unique=False)
    op.create_index(op.f('ix_test_category_id'), 'test_category', ['id'], unique=False)
    op.create_index(op.f('ix_test_category_updated_user_id'), 'test_category', ['updated_user_id'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('role', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.create_table('lab_result',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_time', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_time', sa.DateTime(timezone=True), nullable=True),
    sa.Column('lab_report_id', sa.Integer(), nullable=False),
    sa.Column('parameter_name', sa.String(), nullable=True),
    sa.Column('test_name', sa.String(), nullable=True),
    sa.Column('parameter_id', sa.Integer(), nullable=True),
    sa.Column('unit', sa.String(), nullable=True),
    sa.Column('result', sa.String(), nullable=True),
    sa.Column('upper_limit', sa.Integer(), nullable=True),
    sa.Column('lower_limit', sa.Integer(), nullable=True),
    sa.Column('remark', sa.String(), nullable=True),
    sa.Column('created_user_id', sa.Integer(), nullable=True),
    sa.Column('updated_user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['lab_report_id'], ['lab_report.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_lab_result_created_user_id'), 'lab_result', ['created_user_id'], unique=False)
    op.create_index(op.f('ix_lab_result_id'), 'lab_result', ['id'], unique=False)
    op.create_index(op.f('ix_lab_result_parameter_id'), 'lab_result', ['parameter_id'], unique=False)
    op.create_index(op.f('ix_lab_result_updated_user_id'), 'lab_result', ['updated_user_id'], unique=False)
    op.create_table('lab_test',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_time', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_time', sa.DateTime(timezone=True), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('test_category_id', sa.Integer(), nullable=True),
    sa.Column('created_user_id', sa.Integer(), nullable=True),
    sa.Column('updated_user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['test_category_id'], ['test_category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_lab_test_created_user_id'), 'lab_test', ['created_user_id'], unique=False)
    op.create_index(op.f('ix_lab_test_id'), 'lab_test', ['id'], unique=False)
    op.create_index(op.f('ix_lab_test_updated_user_id'), 'lab_test', ['updated_user_id'], unique=False)
    op.create_table('parameter',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_time', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_time', sa.DateTime(timezone=True), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('unit', sa.String(), nullable=False),
    sa.Column('lab_test_id', sa.Integer(), nullable=True),
    sa.Column('result_type', sa.Enum('text', 'number', name='result_type_enum'), nullable=True),
    sa.Column('result_default_text', sa.JSON(), nullable=True),
    sa.Column('created_user_id', sa.Integer(), nullable=True),
    sa.Column('updated_user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['lab_test_id'], ['lab_test.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_parameter_created_user_id'), 'parameter', ['created_user_id'], unique=False)
    op.create_index(op.f('ix_parameter_id'), 'parameter', ['id'], unique=False)
    op.create_index(op.f('ix_parameter_updated_user_id'), 'parameter', ['updated_user_id'], unique=False)
    op.create_table('parameter_range',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_time', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_time', sa.DateTime(timezone=True), nullable=True),
    sa.Column('parameter_id', sa.Integer(), nullable=True),
    sa.Column('upper_limit', sa.Integer(), nullable=True),
    sa.Column('lower_limit', sa.Integer(), nullable=True),
    sa.Column('low_remark', sa.String(), nullable=True),
    sa.Column('high_remark', sa.String(), nullable=True),
    sa.Column('normal_remark', sa.String(), nullable=True),
    sa.Column('created_user_id', sa.Integer(), nullable=True),
    sa.Column('updated_user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['parameter_id'], ['parameter.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_parameter_range_created_user_id'), 'parameter_range', ['created_user_id'], unique=False)
    op.create_index(op.f('ix_parameter_range_id'), 'parameter_range', ['id'], unique=False)
    op.create_index(op.f('ix_parameter_range_updated_user_id'), 'parameter_range', ['updated_user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_parameter_range_updated_user_id'), table_name='parameter_range')
    op.drop_index(op.f('ix_parameter_range_id'), table_name='parameter_range')
    op.drop_index(op.f('ix_parameter_range_created_user_id'), table_name='parameter_range')
    op.drop_table('parameter_range')
    op.drop_index(op.f('ix_parameter_updated_user_id'), table_name='parameter')
    op.drop_index(op.f('ix_parameter_id'), table_name='parameter')
    op.drop_index(op.f('ix_parameter_created_user_id'), table_name='parameter')
    op.drop_table('parameter')
    op.drop_index(op.f('ix_lab_test_updated_user_id'), table_name='lab_test')
    op.drop_index(op.f('ix_lab_test_id'), table_name='lab_test')
    op.drop_index(op.f('ix_lab_test_created_user_id'), table_name='lab_test')
    op.drop_table('lab_test')
    op.drop_index(op.f('ix_lab_result_updated_user_id'), table_name='lab_result')
    op.drop_index(op.f('ix_lab_result_parameter_id'), table_name='lab_result')
    op.drop_index(op.f('ix_lab_result_id'), table_name='lab_result')
    op.drop_index(op.f('ix_lab_result_created_user_id'), table_name='lab_result')
    op.drop_table('lab_result')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_test_category_updated_user_id'), table_name='test_category')
    op.drop_index(op.f('ix_test_category_id'), table_name='test_category')
    op.drop_index(op.f('ix_test_category_created_user_id'), table_name='test_category')
    op.drop_table('test_category')
    op.drop_index(op.f('ix_patient_updated_user_id'), table_name='patient')
    op.drop_index(op.f('ix_patient_id'), table_name='patient')
    op.drop_index(op.f('ix_patient_created_user_id'), table_name='patient')
    op.drop_table('patient')
    op.drop_index(op.f('ix_lab_report_updated_user_id'), table_name='lab_report')
    op.drop_index(op.f('ix_lab_report_patient_id'), table_name='lab_report')
    op.drop_index(op.f('ix_lab_report_id'), table_name='lab_report')
    op.drop_index(op.f('ix_lab_report_created_user_id'), table_name='lab_report')
    op.drop_table('lab_report')
    # ### end Alembic commands ###
