#MUTABLE DEFAULT ARGUMENTS
# never use a mutable object in the function parameter.
#it  is created when the function is created not when called. Therefore iti is created once. 

from typing import List, Optional



class Student_problematic():
    def __init__(self, name:str, grades=[]):
        self.name=name
        self.grades=grades
        
    def take_exam(self, result:int):
        self.grades.append(result)
        
    
    
bob_problematic=Student_problematic("Bob")
rolf_problematic=Student_problematic("Rolf")
bob_problematic.take_exam(78)
print("MUTABLE DEFAULT ARGUMENT PROBLEM")
print(bob_problematic.grades)
print(rolf_problematic.grades)

#now correction

class Student():
    def __init__(self, name:str, grades: Optional[List[int]]=None): #Optional is to allow None as a parameter instead of List type.
        self.name=name
        self.grades=grades or []
        
    def take_exam(self, result:int):
        self.grades.append(result)
        
    
    
bob=Student("Bob")
rolf=Student("Rolf")
bob.take_exam(78)

print("CORRECTED RESULTS")
print(bob.grades)
print(rolf.grades)