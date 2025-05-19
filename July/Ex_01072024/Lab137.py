# Multi level Inheritance
# # 1 Grandparent - 1 Parent - 1 Child
# # 1 Grandparent - 1 Parent - 2 Child
# # 1 Grandparent - 2 Parent - 1 Child
# # 1 Grandparent - 2 Parent - 2 Child

class Grandparent:
    def grandparent_method(self):
        return "Grandparent's method"

class Parent(Grandparent):
    def parent_method(self):
        return "Parent's method"
    
class Child(Parent):
    def child_method(self):
        return "Child's method"

child1 = Child()
child1.grandparent_method()
child1.parent_method()
child1.child_method()
