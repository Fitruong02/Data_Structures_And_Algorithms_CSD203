from queue import Empty
class Student:
    def __init__(self, id, studentName, address, score):
        self._id = id
        self._studentName = studentName
        self._address = address
        self._score = score

    def display(self):
        print("Student Id: ",self._id)
        print("Student Name ",self._studentName)
        print("Address: " ,self._address)
        print("Score: ",self._score)
    def set_studentName(self,newName):
        self._studentName = newName
    def set_address(self,newAddress):
        self._address = newAddress
    def set_score(self,newScore):
        self._score = newScore

class StudentList:
    # -------------------------- nested _Node class --------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'  # streamline memory usage

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        """Create an empty list of books."""
        self._head = None
        self._tail = None
        self._size = 0  # number of CURRENT elements in the book list

    def __len__(self):
        """Return the number of CURRENT elements in the list."""
        return self._size

    def is_empty(self):
        """Return True if the list is empty, False otherwise."""
        return self._size == 0

    def get_first(self):
        """Return (but do not remove) the element stored in head.
            Note that:
                1. list's head means stack's top or peak.
                2. list's head means queue's front.
                3. list's tail means queue's read.
            Raise Empty exception if the list is empty.
        """
        if self.is_empty():
            raise Empty('Book list is empty')
        return self._head._element  # head of list means front of queue

    def get_last(self):
        """ Return (but do not remove) the element stored in tail.
            Note that:
                  1. list's head means stack's top or peak.
                  2. list's head means queue's front.
                  3. list's tail means queue's read.
            Raise Empty exception if the list is empty.
        """
        if self.is_empty():
            raise Empty('Book list is empty')

        return self._tail._element  # tail of list means rear of queue
    def get_by_name(self,name):
        temp = self._head
        while temp:
            if name == temp._element._studentName:
                print("Search is Successfuly")
                return temp._element.display()
            temp = temp._next
        print("Search is Fail")
        print(f"Don't have any Student's name: {name}")
    def get_by_id(self,id):
        temp = self._head
        while temp is not None:
            if id == temp._element._id:
                print("Search is Successfuly")
                print(temp._element.display())
                return temp._element
            temp = temp._next
        print("Search is Fail")
        print(f"Don't have any Student's id: {id}")
        return None
    def get_at(self, index):
        """ Traverse and return the element at the position 'index' the list.
            This method return -1 if e does not exist in the list.
            Raise Empty exception if:
                1. index > list's size, or
                2. index < 0
        """
        # write your code here, then remove the keyword 'pass'
        if (index > self._size) or (index < 0):
            raise IndexError("Out of range")
        count = 0
        temp = self._head
        while (temp):
            if count == index:
                return temp._element
            temp = temp._next
            count += 1
        return -1

    def check_duplicate(self, id):
        # write your code here, then remove the keyword 'pass'
        temp = self._head
        count = 0
        while (temp):
            if id == temp._element._id:
                return True
            count += 1
            temp = temp._next
        return False

    def add_first(self, e):
        """ Add the element e into the head of the list.
            This method is identical to stack's push
        """
        newNode = self._Node(e, self._head)  # create a newNode
        self._head = newNode  # links newNode to head

        if self._tail is None:  # special case: the list is empty
            self._tail = newNode  # update reference to tail node

        self._size += 1

    def add_last(self, e):
        """ Add the element e into the head of the list.
            This method is identical to queue's enqueue.
        """
        newNode = self._Node(e, None)  # newNode will be the new tail node
        if self.is_empty():
            self._head = newNode  # special case: previously empty
        else:
            self._tail._next = newNode

        self._tail = newNode  # update reference to tail node
        self._size += 1

    def remove_first(self):
        """ Remove and return the first element of the list.
            This method is identical to:
                1. stack's pop
                2. dequeue from a queue
            Raise Empty exception if the list is empty.
        """
        if self.is_empty():
            raise Empty('Book list is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1

        if self.is_empty():  # special case as the list is empty
            self._tail = None  # removed head had been the tail

        return answer

    def remove_last(self):
        """ Remove and return the last element of the list.
            Raise Empty exception if the list is empty.
        """
        if self.is_empty():
            raise Empty('Student list is empty')

        answer = None
        if self._head._next is None:  # List has only ONE node
            answer = self._head._element
            self._head = None
            self._tail = None
            self._size -= 1
            return answer

        # If the program reaches here,
        # Then there were at least TWO nodes in the list
        second_last = self._head
        while second_last._next._next:
            second_last = second_last._next

        answer = self._tail._element
        second_last._next = None  # None means self._tail._next
        self._tail = second_last
        self._size -= 1
        return answer

    def remove_by_id(self,id):
        temp = self._head
        if self.is_empty():
            raise Empty('Student list is empty')
        if (temp is not None):
            if (temp._element._id == id):
                self._head = temp._next
                temp = None
                print(f"Remove the Student with id: {id} is Successful")
                return
        while (temp is not None):
            if temp._element._id == id:
                break
            prev = temp
            temp = temp._next
            return
        prev.next = temp.next
        temp = None
        if temp is None:
            print(f"Can't find the Id of Student: {id}")
            return
    def print_student(self):
        """This function prints contents of Student list.
        It starts from head.
        """
        count = 0
        temp = self._head
        while temp is not None:
            print("\nStudent ", count, "'s info:")
            temp._element.display()
            temp = temp._next
            count += 1


menu_options = {
        1: 'Add a new Student',
        2: 'Update Student info',
        3: 'Search Student info',
        4: 'Remove a Student',
        5: 'Displays n Student',
        6: 'Exit',
}


def menu():
    menu_options = {1: "Change Name",
                    2: "Change Address",
                    3: "Change Score",
                    4: "Change All",  # Remove nood and add new node with same Code
                    5: "Done"
                    }
    print("===============MENU===============")
    for key in menu_options.keys():
        print("===", key, '. ', menu_options[key])
    print("==================================")


def print_menu():
      """
      displays the menu options on screen
      :return: void
      """
      print("===============MENU===============")
      for key in menu_options.keys():
          print("===", key, '. ', menu_options[key])
      print("==================================")

def add_student(student_list):
      print('Code for handling \'Add a new Student\'')
      # Write your code here
      id = input('Input id: ')
      name = input('Input name: ')
      address = input('Input address: ')
      score = int(input('Input score: '))
      newStudent = Student(id, name, address, score)

      # Check duplicate before insertion
      if not student_list.check_duplicate(id):
          student_list.add_first(newStudent)
          print("Student added successfully")
      else:
          print("Cannot insert! Student'ID is duplicated")

def update_student(student_list):
      print('Code for handling \'Update Student info\'')
      id = input("Enter Student's id you want to: ")
      temp = student_list.get_by_id(id)  #Search Student by id
      if temp is None:
          return
      while True:
        menu()
        user_input = int(input("Enter your choice: "))
        if user_input == 1:
            temp.set_studentName(input("Enter new Name: "))
            print("Change Name Successful")
        elif user_input == 2:
            temp.set_address(input("Enter new Address: "))
            print("Change Address Successful")
        elif user_input == 3:
            temp.set_score(input("Enter new Score: "))
            print("Change Score Successful")
        elif user_input == 4:
            temp = Student(id,input("Name: "),input("Address: "),input("Score: ")) #Save the old id( unchange)
            student_list.remove_by_code(id)
            student_list.add_first(temp)
        elif user_input == 5:
            student_list.get_by_id(id)


def search_student(student_list):
      print('Code for handling \'Search Student info\'')
      id = input("Enter id of Student: ")
      return student_list.get_by_id(id)

def remove_student(student_list):
      print('Code for handling \'Remove a student\'')
      id = input("Enter ID of Student You want to Delete: ")
      return student_list.remove_by_id(id)



def display_student(student_list):
      # Write your code here
      student_list.print_student()

def exit_menu():
      print('Thank you, Good Bye, Babies!')
      exit()


def start_menu(b_management):
    while True:
        print_menu()
        user_choice = input('Enter your choice: ')

        # Check what choice was entered and act appropriately
        if user_choice == '1':
            add_student()
        elif user_choice == '2':
            update_student()
        elif user_choice == '3':
            search_student()
        elif user_choice == '4':
            remove_student()
        elif user_choice == '5':
            display_student()
        elif user_choice == '6':
            exit_menu()
        else:
            print('Invalid option. Please enter a number [1--5].')


if __name__ == '__main__':
    student_list = StudentList()
    while True:
        print_menu()
        user_choice = input('Enter your choice: ')

        # Check what choice was entered and act appropriately
        if user_choice == '1':
            add_student(student_list)
        elif user_choice == '2':
            update_student(student_list)
        elif user_choice == '3':
            search_student(student_list)
        elif user_choice == '4':
            remove_student(student_list)
        elif user_choice == '5':
            display_student(student_list)
        elif user_choice == '6':
            exit_menu()
        else:
            print('Invalid option. Please enter a number [1--5].')
