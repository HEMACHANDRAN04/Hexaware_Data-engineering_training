import pandas as pd
import numpy as np


df = pd.read_csv("progress.csv")

print("Original Data")
print(df)


df['completion'] = df['completion'].fillna(0)


df['completion'] = np.clip(df['completion'], 0, 100)

print("\nCleaned Data")
print(df)


overall_avg = np.mean(df['completion'])

print("\nOverall Average Completion:")
print(overall_avg)


report = df.groupby(
    ['course_id', 'course_name']
)['completion'].mean().reset_index()


report.rename(
    columns={'completion': 'average_completion'},
    inplace=True
)

print("\nCourse Level Report")
print(report)


report.to_csv("course_report.csv", index=False)

print("\nReport saved as course_report.csv")