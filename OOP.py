# class BigObject:
#   pass

# obj1 = BigObject() #instantiate
# obj2 = BigObject()
# obj3 = BigObject()

# class PlayerCharacter:
#   def __init__(self,name):
#     self.name = name
#   def run(self):
#     print(f"{self.name} runs!")
    
# player1 = PlayerCharacter("Mark")
# print(player1)

class PlayerCharacter:
    membership = True
    def __init__(self, name,age):
        self.name = name #attributes
        self.age = age
    
    def run(self):
        print(f"{self.name} runs!")
        return ''
    
    def __str__(self):
        return f"Player: {self.name}"
      
    @classmethod
    def adding_things(cls,num1,num2): #cls stands for class
      return num1 + num2
    
    @staticmethod
    def adding_more(num1,num2):
      return num1 + num2

player1 = PlayerCharacter("Mark", 23)
player2 = PlayerCharacter("Tatiana",16)
player3 = PlayerCharacter("Louis",25)
player4 = PlayerCharacter("Denise",37)
print(player1.age)  # Output: Player: Mark
print(player2.run())  # Output: Player: Mark
print(player3)  # Output: Player: Mark
print(player4.age)  # Output: Player: Mark

player4.attack = 50

print(player4.adding_things(2,4))

print(PlayerCharacter.adding_things(4,4))