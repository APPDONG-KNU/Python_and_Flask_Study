#자료형(숫자형, 문자열, boolean)

#숫자형

print(5), print(-10), print(3.14)
	#정수 뿐 아니라 음수, 실수도 출력 가능

print(5+3), print(2*8), print(3*(3+1))
	#연산도 처리하여 출력

#문자형

print('풍선'), print("나비")
	#따옴표나 큰따옴표로 문자열을 출력 가능

print('ㅋㅋㅋ'), print('ㅋ'*3)
	#초성을 출력하거나 연산도 가능

#boolean

print(5 < 10), print(5 > 10)
	#True 또는 False로 출력 가능
	
print(True), print(False)
	#True 또는 False를 바로 출력 가능
	
print(not True), print(not (5 > 10))
	#부정하여 출력이 가능하며, 연산값도 부정하여 출력 가능


#변수

animal = "강아지"
name = "티나"
age = 7
is_adult = age >= 7

print("우리 " + animal + "의 이름은 " + name )
print("티나의 나이는 " +str(age)+ "살이에요")
print(name+"는 어른인가요?" ,is_adult,)

	#변수는 값을 저장하는 어떤 공간
	#+ 변수 이름 +로 입력이 가능
	#정수형이나 boolean 변수는 입력 시 str()을 필요로 함
	#+ 대신 , 를 통해 입력이 가능하며, ,를 사용하면
	#정수형이나 boolean 변수에 str을 쓸 필요가 없어지며
	#자동으로 공백이 하나 들어가게 됨

#주석

	# 프로그램 코드 내에는 작성이 되어있지만, 실행 시 출력이 되지않게 함
	# 문장에 앞에 #을 사용하거나 여러 문장의 앞뒤에 '를 3개씩 작성하여 주석처리 가능함
	# 여러 문장을 지정 후 ctrl + / 키를 이용해서 한 번에 주석처리 가능함


station = "사당"
print(station+ "행 열차가 들어오고 있습니다.")

station = "신도림"
print(station+ "행 열차가 들어오고 있습니다.")

station = "인천공항"
print(station+ "행 열차가 들어오고 있습니다.")


#**은 승을 나타내며 다음과 같은 코드에서 2의 3승을 나타낸다
print(2**3)

#//은 몫을 나타내며 다음과 같은 코드에서 12를 5로 나눈 몫을 나타낸다
print(12//5)

#비교연산도 나타낼 수 있으며, 값은 True 또는 False로 출력된다
print(10>3)
print(4>7)
print(3==3)
print(3!=3)

#AND연산은 and 혹은 &로 나타낼 수 있고
#OR연산은 or 혹은 |로 나타낼 수 있다
print((5>3) & (9>6))
print((5>3) | (9<6))

#abs()를 통해 절댓값을 나타낼 수 있다
print(abs(-7))

#pow()를 통해서도 제곱 연산을 나타낼 수 있다
print(pow(3,3))

#max()를 통해 입력값 중 최댓값을 출력할 수 있다
#min()를 통해 입력값 중 최솟값을 출력할 수 있다
print(max(5,12))
print(min(5,12))

#round()를 통해 소수점 아래 값을 반올림 할 수 있다
print(round(3.14))

#from 함수 import *을 통해 제공하는 함수를 이용할 수 있다

#math 함수
from math import *
print(sqrt(36))

#random 함수
from random import *

#다음은 0.0 ~ 1.0에 해당하는 수 중 무작위로 하나를 출력한다
print (random())

#random 뒤에 *를 통해 범위를 변경할 수 있고
#() 뒤에 +를 통해 시작하는 수를 변경할 수 있고
#int를 통해 출력을 정수 형태로 변경할 수 있다
print(random()*10)
print(int(random()*10))
print(int(random()*10+1))

#randrange, randint를 통해 지정한 범위에서의 무작위 정수형 자료의 출력이 가능하다
#randrange는 마지막이 열린 구간이며, randint는 마지막이 닫힌 구간이다
print(randrange(1,45))
print(randint(1,46))



from random import *
a = randint(4, 28)
print("오프라인 스터디 날짜는 매월" ,a, "일로 결정되었습니다.")