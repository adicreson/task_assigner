from random import randint

class taskAssigner:
    assignments = {}

    def __init__(self, persons, tasks):
        self.persons = persons
        self.tasks  = tasks #Tasks are tuples containing a task and a corresponding category.

    #Returns a random person
    def __random_person(self):
        rand_idx = randint(0, len(self.persons) - 1)
        rand_person = self.persons.pop(rand_idx)

        return rand_person

    #Returns a random task
    def __random_task(self):
        rand_idx = randint(0, len(self.tasks) - 1)
        rand_task = self.tasks.pop(rand_idx)

        return rand_task

    #Assigns tasks to persons
    def __assign_tasks(self):
        while self.persons:
            rand_person = self.__random_person()
            rand_task = self.__random_task()

            self.assignments[rand_person] = rand_task

    #Generates nice print for assigments
    def generate(self):
        self.__assign_tasks()

        print("Person \t\t\t\t Task \t\t Category")
        print("==========================================================")
        for person, task_tuple in self.assignments.items():
            print("{} \t\t\t {} \t\t {}".format(person, task_tuple[0], task_tuple[1]))
        
        print("\n\n***Remaining tasks to be done when finished with initial task***")
        print("Task \t\t Category")
        print("================================================================")

        while tasks:
            task, category = self.__random_task()
            print("{} \t\t {}".format( task, category))



persons = ["Person1", "Person2", "Person3", "Person4", "Person5"]
tasks = [("Task1", "Category1"), ("Task2", "Category2"), ("Task3", "Category3"), ("Task4", "Category4"), ("Task5", "Category5"), ("Task6", "Category6"), ("Task7", "Category7") , ("Task8", "Category8")]

taskAssigner = taskAssigner(persons, tasks)

taskAssigner.generate()