# 마린 : 공격 유닛, 군인. 총을 쏠 수 있음
marin_name = "마린"
hp = 40
damage = 5

print("{} 유닛이 생성되었습니다.".format(marin_name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반 모드 / 시즈 모드.
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

tank2_name = "탱크 (시즈 모드)"
tank2_hp = 350
tank2_damage = 55

print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

print("{0} 유닛이 생성되었습니다.".format(tank2_name))
print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))

def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(name,location,damage))

attack(marin_name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank2_name, "1시", tank2_damage)