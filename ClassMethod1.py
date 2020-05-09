class Employee:
	leaves = 8
	
	def __init__(self,aname,asalary):
		self.name  = aname
		self.salary = asalary
	
	def printdetails(self):
		print("Name:-",self.name,"Salary:-",self.salary,"Leaves:-",self.leaves)
		
	@classmethod
	def changeleaves(cls,newleaves):
		cls.leaves = newleaves
		
	@classmethod
	def dash(cls,string):
		param = string.split("-")
		print(param)
		return cls(param[0],param[1])
	
	@classmethod
	def slash(cls,string):
		param = string.split("/")
		print(param)
		return cls(param[0],param[1])
	@classmethod
	def slice(cls,string):
		return cls(*string.split(":"))
		
	
E1 = Employee("Parth",5000)
print(type(E1.leaves))
E1.changeleaves(35)
print(E1.leaves)
		
E2 = Employee.dash("Lopy-60000")
print(type(E2.salary))

E3 = Employee.slash("jbpatel/65000")
E3  = Employee.slice("Pbpatel:80000")
print(E3.salary)