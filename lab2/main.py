from pprint import pprint

from dacite import from_dict
import requests
from entity import Student
import pandas as pd


# https://www.hse.ru/n/student-ratings/api/filter?unit=122392301
# https://www.hse.ru/n/student-ratings/api?unit=122392301&course=1&from=576252978
#
#
# https://nnov.hse.ru/ba/se/ratings?course=1&from=555130949

def setup():
    pd.set_option('display.max_columns', None)
    all_data.head()

def save(data: pd.DataFrame):
    data.to_csv("txt.csv")

def serchMidValue(data: pd.DataFrame):
    print("Среднее число для поиска: ")
    value_search = float(input())
    student_id = data['gradeMid'].sub(value_search).abs().idxmin()
    print(data.iloc[[student_id]])


request_for_pi = 'https://www.hse.ru/n/student-ratings/api?unit=122392301&course={}&from=576252978'

df = []
# pd.DataFrame(columns=["id", "title", "place", "gradeMid", "gradeMin", "percentil", "gpa"])

for i in range(1, 5):
    students_json = requests.get(request_for_pi.format(i)).json()
    data = students_json["data"]
    student_list = [Student(**s) for s in data]
    print(student_list)
    df.append(pd.DataFrame(data=student_list))

all_data = pd.concat(df, ignore_index=True)

save(all_data)
serchMidValue(all_data)

