# Hierachical Inheritance
# 1 Father - Multiple children

class Parent:
    def BHK1(self):
        return "1BHK"
    
class Pramod(Parent):
    def BHK2(self):
        return "2BHK"

class Amid(Parent):
    def BHK3(self):
        return "3BHK"
    
class Lucky(Parent):
    def no_house(self):
        return "No House"