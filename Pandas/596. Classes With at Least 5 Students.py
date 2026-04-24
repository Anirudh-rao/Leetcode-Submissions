import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    count = courses.groupby('class')['student'].count().reset_index()
    result = count[count['student'] >= 5][['class']]
    return result