#제어문

# 조건문

# if 문
# if 조건문:
#     실행문  을 통해 실행 가능
# elif 를 통해 다른 조건문도 입력이 가능하며
# else 를 통해 조건이 아무것도 충족되지 않을 때에 관한 출력도 가능

a = int(input("사잇각의 크기가 얼마인가요? "))

if 0<a<90:
    print("예각")

elif a==90:
    print("직각")

else:
    print("둔각")


# 반복문

# for 문
# for 변수 in range() 또는
# for 변수 in []:
#    실행문  을 통해 반복 실행 가능

a = 0
for a in range(5):
    a = a+1

print(a)

# while 문

# while (조건):
#     실행문

# 조건을 만족할 때까지 반복 실행

a = 0
while a==5:
    a = a+1

print(a)

# countinue를 사용하게 되면
# 조건을 충족할 때, 반복문의 처음으로 올라가 다시 실행
# break를 사용하게 되면
# 조건을 충족할 때, 반복문을 탈출

for a in range(5):
    if a == 3:
        continue
    print(a)


# for 를 통해 리스트 안의 자료 변환 가능
a = [1, 2, 3, 4, 5]
a = [i+100 for i in a]
print(a)

# QUiz5

from random import *
c = 0
for a in range(49):
    b = randint(5,51)
    c = c+1

    if 5<= b <=15:
        print(f"{c}번째 손님(소요시간 : {b})")

# 함수

# def 를 통해 함수 생성이 가능
def a(b):
    print(b+10)

a(40)

# return을 통해 함수의 결과값을 반환 가능

c=0
def f(c, d):
    print(f"잔액은 {c+d}원 입니다.")
    return c+d

c = f(c, 1000)
c = f(c, 5000)
c = f(c, 12000)

# 기본값
# 반복되는 값이라 불필요하게 여러 번 사용할 필요가 없을 떄 사용
# 아무 값이 입력되지 않았을 때만 기본값을 출력

def f(name, major, grade):
    print(f"이름 : {name}\n전공 : {major}\n학년 : {grade}\n")

f("철수", "컴퓨터학부", 4)
f("영희", "기계공학부", 2)

def f(name, major="전자공학부", grade=1):
    print(f"이름 : {name}\n전공 : {major}\n학년 : {grade}\n")

f("철수")
f("철수", "컴퓨터학부", 4)
f("영희")

# 함수 출력 시 함수 내에서 지정을 해주면 순서가 정렬되어 출력

f(major ="전자공학부", grade = 1, name="철수")

# print 문 마지막에 end = " "를 입력해주면 실행 후 줄바꿈을 실행하지 않음

print("star", end="")
print("bucks")

# 입력될 자료가 몇 개일 지 모를 때
# 변수 앞에 *를 입력해 가변인자를 유용하게 사용 가능

def g(name, grade, *major):
    print(f"이름 : {name}\n학년 : {grade}\n전공 :")
    for k in major:
        print(k)

g("철수", 4, "컴퓨터학부", "전자공학부", "기계공학부")

# 지역변수 : 함수 호출 시에만 적용되는 변수
# 전역변수 : 프로그램 내 전체에 적용되는 변수

# car = 10

# def garage(driver):
#     car = car - driver
#     print(f"남은 차는 {car}대 입니다.")

#garage(5)

# 는 초기화하지 않은 변수 car를 다시 함수 내에서 사용해서
# 오류가 발생, 이를 정정하기 위하여 car를 global을 통해
# 전역변수로 지정해 줋 수 있음
# 하지만 전역변수를 많이 사용하게 되면 코드관리가 어려워져
# 사용에 주의가 필요
# return을 통해 지역변수를 사용하고
# 그 값을 함수 밖으로 전달 가능

car = 20

def garage(driver):
    global car
    car = car - driver     
    print(f"남은 차는 {car}대 입니다.")

garage(5)

# Quiz6

Height = int(input("키를 입력하세요." ))
Gender = input("성별을 입력하세요." )


def std_weight():

    if Gender == "남성":
        print(f"키 {Height}cm인 {Gender}의 표준체중은 {(Height/100)**2 * 22 }kg입니다.")
    elif Gender == "여성":
        print(f"키 {Height}cm인 {Gender}의 표준체중은 {(Height/100)**2 * 21 }kg입니다.")


std_weight()

