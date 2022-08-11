import pandas as pd

student_dict = {
    'student': ['Angela', 'James', 'Lily'], 
    'score': [56, 76, 98]
}


stu_data_frame = pd.DataFrame(student_dict)
stu_data_inher = {row.student: row.score for index, row in stu_data_frame.iterrows()}

print(stu_data_inher)