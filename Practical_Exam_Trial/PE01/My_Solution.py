class Empty(Exception):
  """Error attempting to access an element from an empty container."""
  pass

class Pet:
    def __init__(self, nickname, age, weight):
        self._nickname = nickname
        self._age = age
        self._weight = weight

    def display(self):
        print("Pet nickname: ", self._nickname)
        print("Pet age: ", self._age)
        print("Pet weight: ", self._weight)

    def get_nickname(self):
        return self._nickname

    def set_age(self, new_age):
        self._age = new_age

    def set_weight(self, new_weight):
        self._weight = new_weight


class PetList:
    # -------------------------- nested _Node class --------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'  # streamline memory usage

        def __init__(self, element, next_node):
            self._element = element
            self._next = next_node

        def get_element(self):
            return self._element

        def get_next(self):
            return self._next

    # -------------------------- PetList class --------------------------
    def __init__(self):
        """Create an empty list of pets."""
        self._head = None  # Do NOT modify this line
        self._tail = None  # Do NOT modify this line
        self._size = 0  # number of CURRENT elements in the list

    def __len__(self):
        """Return the number of CURRENT elements in the list."""
        return self._size

    def is_empty(self):
        """Return True if the list is empty, False otherwise."""
        return self._size == 0

    def check_exist(self, nickname):
        """ Test whether the pet which nickname exists in the list
        if it is in the list, then return that NODE, None otherwise
        :param nickname: a string stores the nickname of a pet
        :return: a node that contains the pet or None
        """
        # Hint:
        #   1. declare tmp = self._head
        #   2. use tmp to loop over the list
        #       if the pet's nickname stored in tmp == nickname, then
        #           return that node (tmp)
        #       tmp = tmp.get_next()
        #   3. return None # go through all nodes and not found
        # LOC: 5-8
        # ---------- Write your code here----------
        temp = self._head
        while temp is not None:
            if temp._element._nickname == nickname:
                return temp
            temp = temp._next
        return None
        # ---------- End you code here-------------


    def add_first(self, e):
        """
        Add the element e to the list's head
        :param e: the pet to be added
        :return: void
        """
        # ---------- Write your code here----------
        # create a newNode
        new_node = self._Node(e,self._head)  # write your code here

        # links newNode to head
        self._head = new_node  # write your code here

        # special case: if the list is empty, then
        # update reference to tail node
        if self._tail is None:  # Do NOT modify this line!
            self._tail = new_node  # write your code here

        # increase size by 1
        self._size += 1  # write your code here
        # ---------- End you code here-------------

    def add_last(self, e):
        """
        Add the element e to the list's tail
        :param e: the pet to be added
        :return: void
        """
        # ---------- Write your code here----------
        new_node = self._Node(e, None)  # new_node will be the new tail node

        if self.is_empty():
            # special case: update head if the list is empty
            self._head = new_node  # write your code here
        else:
            self._tail._next = new_node  # write your code here

        # update the reference to tail node
        self._tail = new_node  # write your code here
        self._size += 1 # write your code here
        # ---------- End you code here-------------

    def search(self, name):
        """
        Traverse and return all nodes that has name in their nickname.
        :param name: the substring in nickname of a pet
        :return: all nodes that contains name in nickname, [] otherwise
        """
        # Hint:
        #   1. declare result = []
        #   2. declare tmp = self._head
        #   3. use tmp to loop over the list
        #       3.1. if name is a substring of the nickname in tmp's pet, then
        #               append tmp to the last of 'result'
        #       3.2. tmp = tmp.get_next()
        #   4. return result # go through all nodes of pet_list
        # LOC: 5-9
        # ---------- Write your code here----------
        result  = []
        temp = self._head
        while temp is not None:
            if temp._element._nickname == name:
                result.append(temp)
            temp = temp._next
        return result


        # ---------- End you code here-------------

    def remove_first(self):
        """
        Remove and return the first element of the list.
        :return: element (the pet that has been deleted)
        """
        # ---------- Write your code here----------
        if self.is_empty():
            raise Empty('Pet list is empty')

        answer = self._head  # write your code here
        self._head = answer._next  # write your code here
        self._size -= 1  # write your code here

        # special case: if the list is empty, then update the tail node
        if self.is_empty():
            self._tail = None  # Do NOT modify this line

        return answer  # write your code here
        # ---------- End you code here-------------
        pass

    def print_pet(self):
        """
        Prints the content of all pets in the list,
        starting from head.
        :return: void
        """
        # ---------- Write your code here----------
        temp = self._head
        while temp is not None:
            temp._element.display()
            temp = temp._next
        # ---------- End you code here-------------



# Do NOT modify this variable
menu_options = {
    1: 'Add a new pet',
    2: 'Displays all pets',
    3: 'Search pets by nickname',
    4: 'Update pet nickname',
    5: 'Remove a pet',
    6: 'Exit',
}

# Do NOT modify this function
def print_menu(): # Do NOT modify this function
      """
      displays the menu options on screen
      :return: void
      """
      print("===============MENU===============")
      for key in menu_options.keys():
          print("===", key, '. ', menu_options[key])
      print("==================================")


# Task 1: Add a new pet to the list
# (duplicate nickname is not allowed)
def add_pet(pet_list):
    # Hint:
    #   1. Get information (nickname, age, weight) from user input
    #   2. implement the method 'check_exist(nickname)' in the class PetList
    #   3. implement ONLY one of the two methods in the class PetList
    #           add_first(e) or add_last(e)
    #   4. if the pet's nickname does not exist (check_exist(nickname) returns None):
    #          4.1. create a new pet with the input information
    #          4.2. add the new pet to pet_list via the method you have implemented
    #      else: # the pet's nickname exists,
    #           display a message
    # LOC: 7-12
    # ---------- Write your code here----------
    petInfo = Pet(str(input("Enter Pet's name: ")),int(input("Enter Pet's age: ")),float(input("Enter Pet's Weight: ")))
    if pet_list.check_exist(petInfo.get_nickname()) is None:
        pet_list.add_first(petInfo)
        print(f"Add new pet with name: {petInfo.get_nickname()} sucessfully")
    else:
        print("Do not allow duplicate name of pet, please try again")

    # ---------- End you code here-------------
# Task 2: Display all pets in the list
def display_pet(pet_list):
    # Hint:
    #   1. implement 'print_pet()' in the class PetList
    #   2. call the method 'print_pet()' here
    # LOC: 1-3
    # ---------- Write your code here----------
    return pet_list.print_pet()
    # ---------- End you code here-------------



# Task 3: Search a pet by name (returns a Python list of all pets
# that have the search string in their nickname)
def search_pet(pet_list):
    # Hint:
    #   1. ask users to input search_name
    #   2. implement the method 'search(self, name)' in the PetList class
    #   3. call the method search here to get a Python list of pets having search_name, called search_result
    #   4. for item in search_result:
    #           call 'get_element()' method, then
    #           call 'display()' method
    # LOC: 5-9
    # ---------- Write your code here----------
    search_name = input("Enter your pet's name: ")
    result =  pet_list.search(search_name)
    for item in result:
        item.get_element().display()
    # ---------- End you code here-------------



# Task 4: Update age and weight of a pet.
# Nickname can NOT be updated
def update_pet(pet_list):
    # Hint:
    #   1. ask user to input pet nickname
    #   2. declare 'pet_node' by calling the method 'check_exist(nickname)'
    #   3. check if pet_node is not None, then
    #           ask user to input new_age
    #           ask user to input new_weight
    #           update the new_age (e.g., pet_node.get_element().set_age(new_age))
    #           update the new_weight (e.g., pet_node.get_element().set_age(new_age))
    #      else: # the input nickname does NOT exist in the list
    #           display a message, e.g., print("Pet nickname does not exist")
    # LOC: 8-12
    # ---------- Write your code here----------
    search_name = str(input("Enter your pet's name: "))
    pet_node = pet_list.check_exist(search_name)
    if pet_node:
        pet_node._element.set_age(int(input("Enter new pet's age: ")))
        pet_node._element.set_weight(float(input("Enter new pet's weight: ")))
    else:
        print("Pet nickname does not exist")
    # ---------- End you code here-------------



# Task 5: Remove the first pet which is held by _head from the list
def remove_pet(pet_list):
    # Hint:
    #   1. implement the method 'remove_first()' in the class PetList
    #   2. call the method 'remove_first()' here
    # LOC: 1-3
    # ---------- Write your code here----------
    print("Remove sucessful")
    return pet_list.remove_first()
    # ---------- End you code here-------------



if __name__ == '__main__':
    pet_list = PetList()
    while True:
        print_menu()
        user_choice = input('Enter your choice: ')

        # Check what choice was entered and act appropriately
        if user_choice == '1':
            # Write your code here to handle Task 1
            add_pet(pet_list)
            # End your code here
        elif user_choice == '2':
            # Write your code here to handle Task 2
            display_pet(pet_list)
            # End your code here

        elif user_choice == '3':
            # Write your code here to handle Task 3
            search_pet(pet_list)
            # End your code here
        elif user_choice == '4':
            # Write your code here to handle Task 4
            update_pet(pet_list)
            # End your code here
        elif user_choice == '5':
            # Write your code here to handle Task 5
            remove_pet(pet_list)
            # End your code here
        elif user_choice == '6':
            print('Thank you, Good Bye!')
            exit()
        else:
            print('Invalid option. Please enter a number [1--5].')
