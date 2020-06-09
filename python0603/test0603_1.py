import numpy as np
import pandas as pd

data = pd.read_csv("C:\Python37_Project\data\student.csv")
h = (data['height']/100)
w = data['weight']
data['bmi']  = w/(h*h)

filter1 =data['sex'] == 'male'
df_male = data[filter1]
filter2 = data['sex'] == 'female'
df_female = data[filter2]

while(True):
    print("############남녀 평균 BMI 지수############")
    number = int(input("알고 싶은 평균 BMI지수의 성별을 입력해주세요. 남자(1) 여자(2) :"))

    if number == 1:
        mbmi = df_male['bmi'].mean()
        print(mbmi)
    elif number == 2:
        fbmi = df_female['bmi'].mean()
        print(fbmi)
    else:
        break
    