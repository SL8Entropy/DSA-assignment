
class Manager:
    
    #implemented as a doubly linked list, with both head and tail pointers
    class Task:
        #each task is a node in the doubly linked list
        def __init__(self, task_id, name, task_type):
            self.taskId = task_id
            self.taskName = name
            self.taskType = task_type
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None
        self.tail = None

    def add_task(self, task_id, name, task_type):
        #adds a new task to the end of the list. time complexity: O(1)
        newTask = self.Task(task_id, name, task_type)

        if self.head == None:
            # First task in the list
            self.head = self.tail = newTask
        else:
            # Append to the end and update tail
            self.tail.next = newTask
            newTask.prev = self.tail
            self.tail = newTask
        print(f"Added Task: TaskID: {newTask.taskId}, TaskName: {newTask.taskName}, TaskType: {newTask.taskType} ")

    def remove_task(self, task_id):
        
        #removes the task with the specified ID from the list. time complexity: O(n)
        currentTask = self.head

        currentTask = self.head
        while currentTask is not None:
            if currentTask.taskId == task_id:
                # Case 1: Deleting the head
                if currentTask == self.head:
                    self.head = currentTask.next
                    if self.head:
                        self.head.prev = None

                # Case 2: Deleting the tail
                elif currentTask == self.tail:
                    self.tail = currentTask.prev
                    if self.tail:
                        self.tail.next = None

                # Case 3: Deleting a middle node
                else:
                    currentTask.prev.next = currentTask.next
                    currentTask.next.prev = currentTask.prev

                print(f"Deleted: TaskID: {currentTask.taskId}, TaskName: {currentTask.taskName}, TaskType: {currentTask.taskType}")
                del currentTask
                break  #deleting only first instance
            currentTask = currentTask.next
        print(f"Could not delete id:{task_id}   ID not found")



    def print_tasks(self):
        #prints all tasks in forward order. time complexity: O(n)
        print("------Printing in forward direction-------")
        currentTask = self.head
        while currentTask!=None:
            print(f"TaskID: {currentTask.taskId}, TaskName: {currentTask.taskName}, TaskType: {currentTask.taskType}")
            currentTask = currentTask.next

    def print_tasks_reverse(self):
        #prints all tasks in reverse order. time complexity: O(n)
        print("------Printing in reverse direction-------")

        currentTask = self.tail
        while currentTask!=None:
            print(f"TaskID: {currentTask.taskId}, TaskName: {currentTask.taskName}, TaskType: {currentTask.taskType}")
            currentTask = currentTask.prev



def main():
    manager = Manager()
    filePath = "testCase3.txt"
    try:
        file = open(filePath,"r", encoding="utf-8")
    except:
        print(f"File not found: {filePath}")
        return
    with file:
        for line in file:
            parts = line.strip().split()
            
            if not parts:
                continue  # skip empty lines

            command = parts[0]

            if command == "A" and len(parts) == 4:
                # Eg: A 1 steins;gate anime (create task with id 1, name steins;gate, and type anime)
                task_id = parts[1]
                name = parts[2]
                task_type = parts[3]
                manager.add_task(task_id, name, task_type)

            elif command == "R" and len(parts) == 2:
                # Eg: R 1 (removes task with id 1)
                task_id = parts[1]
                manager.remove_task(task_id)

            elif command == "P":
                manager.print_tasks()

            elif command == "PR":
                manager.print_tasks_reverse()

            else:
                print(f"Invalid command: {line.strip()}")
main()