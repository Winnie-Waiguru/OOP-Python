class Student:
    school="Akirachix"
    def __init__(self,first_name, last_name,age,country):
        self.first_name= first_name
        self.last_name=last_name
        self.age= age
        self.country=country
        
    def full_name(self):
        
        return f"Your full name is {self.first_name} {self.last_name}."   
    
    def year_of_birth(self):
        
        current_year=int(input("Enter current year: \n"))
        YoB= current_year-self.age
        return f"You were born in {YoB}" 
    
    def initials(self):
        
        acronym= f"{self.first_name[0]}{self.last_name[0]}"
        return acronym