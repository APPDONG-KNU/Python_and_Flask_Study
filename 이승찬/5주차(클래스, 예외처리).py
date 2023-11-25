#마린 : 공격 유닛, 군인, 총을 쏠 수 있음

name =  "마린" #유닛의 이름
hp = 40 #유닛의 체력
damage = 5 #유닛의 공격력

print(f"{name} 유닛이 생성되었습니다.")
print(f"체력 {hp}, 공격력 {damage}\n")

#탱크 : 공격 유닛, 탱크, 포를 쏠 수 있음, 일반/시즈모드

tank_name =  "탱크"
tank_hp = 150
tank_damage = 35

print(f"{tank_name} 유닛이 생성되었습니다.")
print(f"체력 {tank_hp}, 공격력 {tank_damage}\n")

def attack(name, location, damage):
	printf(f"{name} : {location} 방향으로 적군을 공격합니다. [공격력 {damage}]")

#계속해서 이런 식으로 유닛을 추가할 경우
#클래스가 필요하게 됨

#클래스는 붕어빵 틀과 같은 개념
#클래스는 변수와 함수의 집합

class unit:
	def __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp
		self.damage = damage
		print(f"{self.name} 유닛이 생성되었습니다.")
		print(f"체력 {self.hp}, 공격력 {self.damage}")

marine1 = unit("마린", 40, 5)
marine2 = unit("마린", 40, 5)
tank = unit("탱크", 150, 35)

#여기서 어떤 클래스로부터 만들어지는 것 => 객체
#마린과 탱크 => 유닛 클래스의 인스턴스
#객체가 생성될 때는 이닛 함수의 정의된 개수와 동일해야 함

class attack_unit:
	def __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp
		self.damage = damage

	def attack(self, location):
		print(f"{self.name} : {location} 방향으로 공격합니다.
		[공격력 {self.damage}]")

	def damaged(self, damage):
		print(f{self.name} : {damage} 데미지를 입었습니다.")
		self.hp -= damage
		print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")
		if self.hp <= 0:
			print("{self.name} : 파괴되었습니다.")

#class 뒤에 괄호를 통해 위의 클래스를 상속 가능
#여러 개의 클래스를 상속도 가능

#예외 처리
#except 예외 유형을 통해 처리 가능

try:
        print("나누기 전용 계산기입니다.")
        num1 = int(input("첫 번째 숫자를 입력하세요 : "))
        num2 = int(input("두 번째 숫자를 입력하세요 : "))
        print(f"{num1} / {num2} = {num1/num2}")

except ValueError:
        print("에러! 잘못된 값을 입력하였습니다.")
        
except ZeroDivisionError as err:
        print(err)

#사용자가 정의하는 방식으로도 예외 처리 가능

try:
        print("나누기 전용 계산기입니다.")
        num1 = int(input("첫 번째 숫자를 입력하세요 : "))
        num2 = int(input("두 번째 숫자를 입력하세요 : "))
        if num1 >= 10 or num2 >= 10:
                raise BigNumberError
        print(f"{num1} / {num2} = {int(num1/num2)}")

except ValueError:
        print("에러! 잘못된 값을 입력하였습니다.")

except BigNumberError:
        print("에러가 발생하였습니다. 한자리 숫자만 입력하세요.")

#finally는 구문의 오류에 상관없이 항상 실행되는 구문

        try:
        print("나누기 전용 계산기입니다.")
        num1 = int(input("첫 번째 숫자를 입력하세요 : "))
        num2 = int(input("두 번째 숫자를 입력하세요 : "))
        if num1 >= 10 or num2 >= 10:
                raise BigNumberError
        print(f"{num1} / {num2} = {int(num1/num2)}")

except ValueError:
        print("에러! 잘못된 값을 입력하였습니다.")

except BigNumberError:
        print("에러가 발생하였습니다. 한자리 숫자만 입력하세요.")

finally:
        print("계산기를 이용해주셔서 감사합니다.")


        
        


