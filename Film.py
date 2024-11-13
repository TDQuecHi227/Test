
class Film:
    def __init__(self, iD, name, year, award, nomination):
        self.id = iD
        self.name = name
        self.year = year
        self.award = award
        self.nomination = nomination
    
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Year: {self.year}, Award: {self.award}, Nomination: {self.nomination}"

