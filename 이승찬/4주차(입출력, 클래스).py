# sep, end
# sep을 통해 출력되는 값 사이에 원하는 정보 입력 가능
# end를 통해 출력값의 마지막 부분을 설정 가능하며
# 아무 값도 지정하지 않으면 파이썬에서는 \n으로 설정
print("apple", "banana", "camera")
print("apple", "banana", "camera", sep = "/")
print("apple")
print("banana")
print("apple", end = "&")
print("banana")

# import sys
# file=sys.stdout이나 file=sys.stderr을 통해
# 표준출력이나 표준에러로 출력 가능
# vscode에서는 보기에 큰 차이가 없음
import sys
print("apple", "banana", "camera", file=sys.stdout)
print("apple", "banana", "camera", file=sys.stderr)

# .items()를 이용하면 key와 value를 쌍으로 출력 가능

a = {"수학": 100, "물리학": 100, "한국사": 50}
for subject, grade in a.items():
    print(subject, grade)

# 문자형 변수 뒤에 .ljust(자릿수), .rjust(자릿수)를 통해 출력 자릿수와 함께
# 오른쪽 또는 왼쪽 정렬이 가능


a = {"수학": 100, "물리학": 100, "한국사": 50}
for subject, grade in a.items():
    print(subject.ljust(8), str(grade).rjust(4), sep=":")

# 빈자리에 0을 채워넣기 위해서 .zfill()을 사용 가능

for a in range(1, 21):
    print(f"대기번호 : {str(a).zfill(3)}")

# input은 늘 문자형 자료 형태로 변수에 저장

# a = input("아무 값이나 입력하세요.")
# print(type(a))

# 빈 자리는 빈칸으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
a = 700
print(f"{a: >10}")

# 다른 활용 예시
print(f"{a:_<+8}")

# ,를 활용하면 세자리마다 콤마를 입력 가능
a=100000000000
print(f"{a:,}")

# f를 통해 실수형으로 출력이 가능하며, .자릿수f 를 통해 자릿수 지정도 가능
a=22/7
print(f"{a:.2f}")

# 변수명 = open("파일 형태", "파일 목적", encoding="사용할 유니코드")의 형태로 파일 열기가 가능하며
# 파일을 열어줬다면 변수명.close() 반드시 닫아줘야함

a = open("b.txt", "w", encoding="utf8")
print("수학 : 100", file = a)
print("물리학 : 100", file = a)
a.close()

# 쓰기용으로 연 파일은 덮어쓰며
# 열 때 w(write) 대신 a(append)를 사용하고
# 변수명.write를 통해 이어쓰기도 가능
# 이때는 줄바꿈을 직접 작성


a = open("b.txt", "a", encoding="utf8")
a.write("한국사 : 50")
a.write("\n화학 : 50")
a.close()

# w(write) 대신 r(read)를 사용하고
# print(변수명.read())를 통해
# 파일을 읽어오는 것도 가능

a = open("b.txt", "r", encoding="utf8")
print(a.read())
a.close()

# read 대신 readline을 사용하면 한 줄씩 읽어옴


a = open("b.txt", "r", encoding="utf8")
print(a.readline())

a.close()

# list 형태로 저장 후 출력도 가능

k = a.readlines()

# pickle 이란 프로그램을 파일 형태로 저장

