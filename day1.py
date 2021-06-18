
# data

print("hi")

print('hi')

# boolean

print(True)

# 변수

animal = "강아지"
name = "연탄이"
age = 4

print("우리집" + animal + "는" + str(age) + "살입니다.")

# station[2] = {"사당","신도림","인천공항"}

# for i in range(station):
#     print(station[i] + "행 열차가 들어오고 있습니다." )

# 숫자 처리 함수

print(abs(-5)) # 5
print(pow(4, 2)) # 4^2 = 4*4 = 16
print(max(5,12)) # 12
print(min(5,12)) # 5
print(round(3.14)) # 3
print(round(4.99)) # 5

from math import *

print(floor(4.99)) # 내림 4
print(ceil(3.14)) # 올림 4
print(sqrt(16)) # 제곱근 4


# 랜덤

from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의의 값.
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값.

print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성

print(randint(1,45)) # 1 ~ 45 이하의 임의의 값.

print(range(2))

for i in range(3):
    print("온라인 스터디 모임 날짜는 매 월 " + str((randint(4,28))) + "일로 선정되었습니다." ) 


print("오프라인 스터디 모임 날짜는 매 월 " + str((randint(4,28))) + "일로 선정되었습니다." )

# 문자열

sentence = """
하이
하이"""
print(sentence)

# 슬라이싱

jaemin = "990120-1234567"

print("성별 : " + jaemin[7])

print("연 : " + jaemin[0:2]) # 0부터 2 직전까지

print("월 : " + jaemin[2:4])

print("생년월일 : " + jaemin[:6]) # 처음부터 6 직전까지
print("뒷자리 : " + jaemin[7:]) # 7부터 끝까지

# 문자열 처리 함수

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("python", "Java"))

index = python.index("n")
print(index)

print(python.find("Java"))

print(python.count("n"))

# 문자열 합치기

# %d = 정수
# %s = 문자열
# %c = 아무거나 하나

print("나는 %d살 입니다.")

print("나는 {0}색과 {1}색을 좋아합니다.".format("파란","빨간"))

age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

# 탈출 문자

# \n

print(f"나는 {age}살이며, \n{color}색을 좋아해요.")