
# # # # # data

# # # # print("hi")

# # # # print('hi')

# # # # # boolean

# # # # print(True)

# # # # # 변수

# # # # animal = "강아지"
# # # # name = "연탄이"
# # # # age = 4

# # # # print("우리집" + animal + "는" + str(age) + "살입니다.")

# # # # # station[2] = {"사당","신도림","인천공항"}

# # # # # for i in range(station):
# # # # #     print(station[i] + "행 열차가 들어오고 있습니다." )

# # # # # 숫자 처리 함수

# # # # print(abs(-5)) # 5
# # # # print(pow(4, 2)) # 4^2 = 4*4 = 16
# # # # print(max(5,12)) # 12
# # # # print(min(5,12)) # 5
# # # # print(round(3.14)) # 3
# # # # print(round(4.99)) # 5

# # # # from math import *

# # # # print(floor(4.99)) # 내림 4
# # # # print(ceil(3.14)) # 올림 4
# # # # print(sqrt(16)) # 제곱근 4


# # # # # 랜덤

# # # # from random import *

# # # # print(random()) # 0.0 ~ 1.0 미만의 임의의 값.
# # # # print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값.

# # # # print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성

# # # # print(randint(1,45)) # 1 ~ 45 이하의 임의의 값.

# # # # print(range(2))

# # # # for i in range(3):
# # # #     print("온라인 스터디 모임 날짜는 매 월 " + str((randint(4,28))) + "일로 선정되었습니다." ) 


# # # # print("오프라인 스터디 모임 날짜는 매 월 " + str((randint(4,28))) + "일로 선정되었습니다." )

# # # # # 문자열

# # # # sentence = """
# # # # 하이
# # # # 하이"""
# # # # print(sentence)

# # # # # 슬라이싱

# # # # jaemin = "990120-1234567"

# # # # print("성별 : " + jaemin[7])

# # # # print("연 : " + jaemin[0:2]) # 0부터 2 직전까지

# # # # print("월 : " + jaemin[2:4])

# # # # print("생년월일 : " + jaemin[:6]) # 처음부터 6 직전까지
# # # # print("뒷자리 : " + jaemin[7:]) # 7부터 끝까지

# # # # # 문자열 처리 함수

# # # # python = "Python is Amazing"
# # # # print(python.lower())
# # # # print(python.upper())
# # # # print(python[0].isupper())
# # # # print(len(python))
# # # # print(python.replace("python", "Java"))

# # # # index = python.index("n")
# # # # print(index)

# # # # print(python.find("Java"))

# # # # print(python.count("n"))

# # # # # 문자열 합치기

# # # # # %d = 정수
# # # # # %s = 문자열
# # # # # %c = 아무거나 하나

# # # # print("나는 %d살 입니다.")

# # # # print("나는 {0}색과 {1}색을 좋아합니다.".format("파란","빨간"))

# # # # age = 20
# # # # color = "빨간"
# # # # print(f"나는 {age}살이며, {color}색을 좋아해요.")

# # # # # 탈출 문자

# # # # # \n

# # # # print(f"나는 {age}살이며, \n{color}색을 좋아해요.")

# # # "http://naver.com"

# # # n = input()

# # # front = n[n.find('//')+2:n.find('.')]

# # # password = front[:3] + str(len(front)) + str(front.count("e")) + "!"

# # # print("생성된 비밀번호 : " + password)

# # ## dictionary

# # cabinet = {'a':"김승환"}

# # print(cabinet)

# # print(cabinet.keys()) # 키출력

# # print(cabinet.values()) # value 만 출력

# # print(cabinet.items()) # 둘 다 출력

# # cabinet.clear()

# # 튜플

# menu = ("돈까스", "치즈까스" )

# print(menu[0])
# print(menu[1])

# name, age, hobby = "승환", 25, "영화"

# print(name,age,hobby)


## set
## 중복 안됨, 순서 없음

# my_set = {1,2,2,3,4,4,5}

# print(my_set)

# from random import *

# my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# # users = list(range(1, 21))

# print("-- 당첨자 발표 --")
# print("치킨 당첨자 : " + str(sample(my_list, 1)))
# shuffle(my_list)
# print("커피 당첨자 : " + str(sample(my_list, 3)))

# from random import *
# count = 0

# for i in range(50):
#     time = randint(5,50)
#     if (time >= 5 and time <= 15):
#         matching = 0
#         count = count + 1
#     else:
#         matching = ""
#     print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(matching,i+1,time))

# print("총 탑승 승객 : {0} 분".format(count))

## pickle

## with

# for i in range(1, 51):
#     with open(str(i) + "주차.txt", "w", encoding="trf8") as report_file:
#         report_file.write("{0} 주차 주간보고  -".format(i))

## class

# 마린

name = "마린"
hp = 40
damage = 5

print("{} 유닛이 생성되었습니다. ".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp,damage))


tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{0} 유닛이 생성되었습니다. ".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp,tank_damage))

def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군은 공격 합니다. [공격력{2}]".format(name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)