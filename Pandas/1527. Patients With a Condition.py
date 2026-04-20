import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    patients_with_diabets = patients[patients['conditions'].str.contains(r'^DIAB1|\sDIAB1')]
    result_df = patients_with_diabets[['patient_id','patient_name','conditions']]
    return result_df