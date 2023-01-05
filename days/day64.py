class animal:
  species = None
  name = None
  sound = None

  def __init__(self, name, species, sound,
               color):  # Include the 'self' in the 'init'
    self.name = name
    self.species = species
    self.sound = sound
    self.color = color


class bird(animal):

  def __init__(self):
    self.name = "Bird"
    self.species = "Avian"
    self.sound = "Tweet"
    self.color = "green"


cow = animal("Ermintrude", "Bo Taurus", "Moo", "black")

# print(cow.sound)

# create the generic class for job
# contains name, salary, hours worked
# init >> self, name, salary, hours_worked
# inherit to other kinds of job: doctor (years of experience, specialty), teacher (subjects and position)
# instanciate a lawyer
# inherit doctor (7 years exp, paediatric consultant)
# inherit teacher (subject comp science and position teacher)
# print out the info for all jobs


# original class
class Job:
  name = None
  salary = None
  hours_worked = None

  def __init__(self, name, salary, hours_worked):
    self.name = name
    self.salary = int(salary)
    self.hours_worked = int(hours_worked)

  def job(self):
    print(
      f'Job name: {self.name}\nWage: {self.salary} €\nHours worked: {self.hours_worked}'
    )


# inherited 1
class Doctor(Job):
  experience = None
  speciality = None

  def __init__(self, salary, hours_worked, exp, speciality):
    self.name = "doctor"
    self.salary = salary
    self.hours_worked = hours_worked
    self.experience = float(exp)
    self.speciality = speciality

  def doctor(self):
    print(
      f'Job name: {self.name}\nWage: {self.salary} €\nHours worked: {self.hours_worked}\nExp.: {self.experience} years\nSpeciality: {self.speciality}'
    )


# inherited 2
class Teacher(Job):
  subject = None
  position = None

  def __init__(self, salary, hours_worked, subject, position):
    self.name = "teacher"
    self.salary = salary
    self.hours_worked = hours_worked
    self.subject = subject
    self.position = position

  def teacher(self):
    print(
      f'Job name: {self.name}\nWage: {self.salary} €\nHours worked: {self.hours_worked}\nExp.: {self.subject} years\nSpeciality: {self.position}'
    )


# print job instances
# 1. original class
lawyer = Job("lawyer", 100000, 60)
lawyer.job()
print()
#2. inherited classes
doctor = Doctor(150000, 65, 7.5, "Paediatric consultant")
doctor.doctor()
print()
teacher = Teacher(65000, 40, "Mathematics", "Head Teacher")
teacher.teacher()
