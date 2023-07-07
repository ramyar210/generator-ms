from main import CollectData

obj=CollectData()
program=obj.program
df_data=obj.get_file()

def totalenrolment_event_data():
    df_snap = df_data[['state_code','district_code','program', 'total_enrollments']]
    df_snap.columns = ['state_id','district_id','program_name', 'total_enrolments']
    obj.upload_file(df_snap, 'districtwiseenrolments-event.data.csv')

def totalcertification_event_data():
    df_snap = df_data[['state_code', 'district_code', 'program', 'total_certifications']]
    df_snap.columns = ['state_id', 'district_id', 'program_name',  'total_certifications']
    obj.upload_file(df_snap, 'districtwisecertifications-event.data.csv')

def program_dimension_data():
    df_snap = df_data[['program']].drop_duplicates()
    df_snap['program_id'] = range(1, len(df_snap) + 1)
    df_snap = df_snap[['program_id', 'program']]
    df_snap.columns = ['program_id', 'program_name']
    df_snap.update(df_snap[['program_id']].applymap("'{}'".format))
    obj.upload_file(df_snap, 'programnishtha-dimension.data.csv')


if df_data is not None:
    totalenrolment_event_data()
    totalcertification_event_data()
    program_dimension_data()
