from random import *

dice = int(input("주사위 값을 입력해주세요 : "))
roll = randint(1,dice)
print("주사위에서 " + str(roll) + "가 나왔습니다.")
