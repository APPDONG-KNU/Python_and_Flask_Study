#문자열

#문자열은 '' 나 "" 를 통해 출력가능하고
#'''를 통해 여러 문장을 한 번에 출력할 수도 있다

a = "나는 소년입니다."
print(a)

#슬라이싱

#정보를 필요한 만큼 잘라서 사용
#변수 뒤에 []를 통해 몇 번째 수를 가져올 것인지 선택 가능
#0에서부터 세며, 여러 숫자를 가져올 땐 :를 통해 지정 가능
#범위는 앞에는 닫힌 구간, 뒤에는 열린 구간
#범위에 -를 통해 뒤에서부터 지정도 가능

a = "030511-1234567"
print("나는 " +a[0:2]+ "년생 입니다.")

#문자열처리함수
a = "I am Iron man"

#문자열변수 뒤에 .lower()나 upper().를 통해 소문자 혹은 대문자로 전환 가능
print(a.lower())

#[].islower(), [].isupper()를 통해 지정한 문자에 대해 참/거짓 판별 가능
print(a[0].isupper())

#len(변수)를 통해 문자열의 길이 출력 가능
print(len(a))

#.replace("바꾸려는 문자", "새로넣을 문자")를 통해 문자열교체 가능
print(a.replace("Iron", "Super"))

#변수.index ("찾으려는 글자")를 통해 원하는 글자의 위치를 알 수 있음
#글자 뒤에 , +k 를 통해 그 다음 글자의 위치를 찾는 것도 가능
b = a.index("m")
print(b)
b = a.index("m", b+1)
print(b)

#index 대신 find를 사용하면 기능은 같으나, 없는 글자를 입력했을 때
#오류가 나고 코드가 종료되는 것이 아니라 -1이 출력됨
print(a.find("girl"))

#.count를 사용하게 되면 그 문자의 사용횟수가 출력됨
print(a.count("m"))

#%d, %s, %c 를 사용하고 뒤에 대응시킬 값을 % 뒤에 작성하여 원하는 곳에 출력
#%d는 정수형 자료, %c는 문자형 자료를 나타내며, %s는 범용성이 큼
#( , )를 통해 여러 값을 대응 가능
print("나는 %d살 입니다." % 20)
print("나는 %s년생 입니다." % 2003)
print("나는 %s와 %s를 좋아합니다." % ("야구", "배드민턴"))

#% 대신 {}와 .format을 이용하여 출력 가능
print("나는 {}살 입니다." .format(20))
print("나는 {}와 {}를 좋아합니다." .format("야구", "배드민턴"))

#중괄호 속에 숫자를 통해 순서 지정 가능
print("나는 {1}와 {0}를 좋아합니다." .format("야구", "배드민턴"))

#변수를 대입하여 출력도 가능하고
# .format 대신, 가장 앞의 f를 통해 출력도 가능
a= "야구"
b= "배드민턴"
print("나는 {}와 {}를 좋아합니다." .format(a, b))
print(f"나는 {a}와 {b}를 좋아합니다.")

#Quiz3

a = "http://naver.com"
b = a[7:-4]
c = b[0:3]
d = b.count("e")
e = len(b)
print(f"{c}{e}{d}!")

#리스트 : 순서를 가지는 객체의 집합
#.append를 통해 리스트에 추가도 가능
a= [1, 2, 3]
a.append(4)
print(a)

#.insert(위치, 추가하려는 값)을 통해 위치도 지정 가능
a.insert(1, 5)
print(a)

#.pop을 통해 뒤에서부터 삭제도 가능
a.pop()
print(a)

#문자열과 마찬가지로 .count를 통해 중복되는 자료의 횟수도 출력 가능
a.append(1)
b= a.count(1)
print(b)

#.sort를 통해 오름차순으로 정렬하거나, .reverse를 통해 내림차순으로도 정렬 가능
a.sort()
print(a)
a.reverse()
print(a)

#.clear를 통해 리스트 안의 모든 값을 초기화 가능
a.clear()
print(a)

# ++ *리스트, sep , 을 통해 필요없는 부분을 지우고 출력 가능
# ++ "구분자".join을 통해 문자열을 합치기 가능

#리스트는 자료형에 구애받지 않고 복합적으로 사용이 가능
b= ["사람", "human", 12, True]
print(b)

#확장하려는 함수.extend(확장하려는 함수)를 통해 리스트 병합도 가능
a= [1, 2, 3, 4, 5]
a.extend(b)
print(a)

#{키 : 저장하려는 데이터}를 통해 변수 지정 가능하며
#키의 자료형은 무관함
a= {1:"apple", 3:"banana"}
print(a[1])

#출력 시 .get()을 통해 출력도 가능하며
#이 방식을 이용하면 오류 대신 None이 출력되며, 프로그램이 종료되지 않음
#없는 값 뒤에 ,를 통해 대신 출력될 값을 지정도 가능
print(a.get(2))
print("coffee")
print(a.get(2, "OK"))

#(키 in 리스트)를 통해 키의 존재 유무를 출력 가능
print(1 in a)
print(2 in a)

#리스트[키] = 자료 를 통해 자료 추가/변경도 가능
#del 리스트[키]를 통해 삭제도 가능
a[4] = "camara"
print(a[4])
del a [1]
print(a.get(1))

#리스트.keys나 리스트.values, 리스트.items 를 통해 리스트의 키나 자료 출력 가능
print(a.keys())
print(a.values())
print(a.items())

#튜플은 변경/추가가 안되지만, 속도가 리스트에 비해 빠름
a=("apple", "banana")
print(a[0])
print(a[1])

#집합은 중복되는 값을 무시하고 출력
a={1, 2, 3, 2, 3}
print(a)

#&와 |, -를 이용해 교집합과 합집합, 차집합을 표현 가능 
a={"x", "l"}
b={"x", "y", "z"}
print(a&b)
print(a|b)
print(a-b)

#자료구조의 변경도 가능함
a= {1, 2, 3, 4, 5}
a=list(a)
print(a)
a=set(a)
print(a)
a=tuple(a)
print(a)

#Quiz4

from random import *
a= range(1, 21)
a= list(a)

#Shuffle 이용
shuffle(a)
b= a[0]
c= a[1:4]
print("--당첨자 발표--")
print("치킨 당첨자", b)
print("커피 당첨자", c)
print("--축하합니다--\n\n")

#Sample 이용
b= sample(a, 4)
print("--당첨자 발표--")
print("치킨 당첨자", b[0])
print("커피 당첨자", b[1:4])
print("--축하합니다--")
