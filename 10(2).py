# class Human:
#     name = 'Иван'
#     color_hair = 'black'
#     h = 175
#     w = 65
# human_object = Human()
# print(human_object.name)
# print(dir(Human))#в конце свойства класса
#-------------------------------------------------------
class Human:
    def __init__(self,name,color_hair,h,w):
        self.name = name
        self.color_hair = color_hair
        self.h = h
        self.w = w

human_1 = Human(name='Иван',color_hair='black',h=190,w=75)
human_2 = Human(name='Дмитрий',color_hair='black', h=174,w=70)

print(f'{human_2.name} весит {human_2.w} кг при росте {human_2.h}')
#---------------------------------------------------------------
# import random
# import tank
# class Tank:
#     """Template of tanks"""
#
#     def __init__(self, model, armor, min_damage, max_damage, health):
#         self.model = model
#         self.armor = armor
#         self.damage = random.randint(min_damage, max_damage)
#         self.health = health
#
#     def print_info(self):
#             print(f"{self.model} имеет лобовую броню {self.armor}мм при {self.health}ед. здоровья и урон в {self.damage} единиц")
#
#     def health_down(self, enemy_damage):
#             self.health -= enemy_damage
#             print(f"\n{self.model}:")
#             print(f"Командир, по экипажу {self.model} попали, у нас осталось {self.health} очков здоровья")
#
#
#     def shot(self, enemy):
#             if enemy.health <= 0 or self.damage >= self.health:
#                 self.health = 0
#                 print(f"Экипаж танка {enemy.model} уничтожен")
#             else:
#                 enemy.health_down(enemy.damage)
#                 print(f"\n{self.model}:")
#                 print(f"Точно в цель, у противника {enemy.model} осталось {enemy.health} единиц здоровья")
#
# class SuperTank(Tank):
#     """Template of superTanks"""
#     def __init__(self, model, armor, min_damage, max_damage, health):
#         super().__init__(model, armor, min_damage, max_damage, health)
#         self.forceArmor = True
#
#
#     def health_down(self, enemy_damage):
#         super().health_down(enemy_damage / 2)
#
#
# tank1 = tank.Tank('Tiger', 100, 30, 50, 100)
# super_tank2 = tank.SuperTank('Leopard', 100, 30, 50, 100)
#
# tank1.shot(super_tank2)
# tank1.shot(super_tank2)
# tank1.shot(super_tank2)
#
# super_tank2.shot(tank1)
# super_tank2.shot(tank1)
# super_tank2.shot(tank1)
# super_tank2.shot(tank1)





