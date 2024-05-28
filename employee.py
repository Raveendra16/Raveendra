class Empo:
    def __init__(self,id,name,position):
        self.id=id
        self.name=name
        self.position=position
class Emanage:
    def __init__(self):
        self.employee=[]
    def add(self, id, name, position):
        emp=Empo(id, name, position)
        self.employee.append(emp) 
        #delete the employee
    def delete(self,id):
        for emp in self.employee:
            if emp==id:
                self.employee.remove(emp)
        print("deleted")
    def dis(self):
        for emp in self.employee:
            print(f"ID: {emp.id}, Name: {emp.name}, Position: {emp.position},")

if __name__ == "__main__":
    emp=Emanage()
    emp.add(1, "hii", "IT")
    emp.add(2, "ooo", "IT")
    emp.add(3, "kkk", "IT")
    emp.add(4, "hhh", "IT")
    emp.dis()
    emp.delete(3)
    emp.dis()