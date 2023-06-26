from random import randint

class TaskAssigner:
    def __init__(self, persons, tasks):
        self.persons = persons
        self.tasks = tasks  # Tasks are tuples containing a task and a corresponding category.
        self.assignments = {}

    def random_person(self):
        rand_idx = randint(0, len(self.persons) - 1)
        rand_person = self.persons.pop(rand_idx)
        return rand_person

    def random_task(self):
        rand_idx = randint(0, len(self.tasks) - 1)
        rand_task = self.tasks.pop(rand_idx)
        return rand_task

    def assign_tasks(self):
        while self.persons:
            rand_person = self.random_person()
            rand_task = self.random_task()
            self.assignments[rand_person] = rand_task

    def generate(self):
        self.assign_tasks()

        print("Person \t\t\t\t Task \t\t Category")
        print("==========================================================")
        for person, task_tuple in self.assignments.items():
            print("{} \t\t\t {} \t\t {}".format(person, task_tuple[0], task_tuple[1]))

        print("\n\n***Remaining tasks to be done when finished with initial task***")
        print("Task \t\t Category")
        print("================================================================")

        for task in self.tasks:
            print("{} \t\t {}".format(task[0], task[1]))


persons = ["Person1", "Person2", "Person3", "Person4", "Person5"]
tasks = [
    ("Task1", "Category1"), ("Task2", "Category2"), ("Task3", "Category3"),
    ("Task4", "Category4"), ("Task5", "Category5"), ("Task6", "Category6"),
    ("Task7", "Category7"), ("Task8", "Category8")
]

task_assigner = TaskAssigner(persons, tasks)
task_assigner.generate()
