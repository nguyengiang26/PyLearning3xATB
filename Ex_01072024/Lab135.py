
class Parent:
    gold = "2kg"

    def BHK2(self):
        return "2BHK"
    
class Child(Parent):
    def BHK3(self):
        return "3BHK"
    
    def BHK4(self):
        return "4BHK"

child_obj = Child()
child_obj.BHK2()
child_obj.BHK3()

print(child_obj.gold)

father_obj = Parent()
print(father_obj.gold)

