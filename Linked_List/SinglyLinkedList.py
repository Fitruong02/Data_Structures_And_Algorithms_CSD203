from queue import Empty

class SLL:
  """FIFO queue implementation using a singly linked list for storage."""

  #-------------------------- nested _Node class --------------------------
  class _Node:
    """Lightweight, nonpublic class for storing a singly linked node."""
    __slots__ = '_element', '_next'         # streamline memory usage

    def __init__(self, element, next):
      self._element = element
      self._next = next

  #------------------------------- SLL methods -------------------------------
  def __init__(self):
    """Create an empty queue."""
    self._head = None
    self._tail = None
    self._size = 0      # number of CURRENT elements in the list

  def __len__(self):
    """Return the number of CURRENT elements in the list."""
    return self._size

  def is_empty(self):
    """Return True if the list is empty, False otherwise."""
    return self._size == 0

  def getFirst(self):
    """Return (but do not remove) the element stored in head.
       Note that:
                1. list's head means stack's top or peak.
                2. list's head means queue's front.
                3. list's tail means queue's read.

       Raise Empty exception if the list is empty.
    """
    if self.is_empty():
      raise Empty('SLL is empty')

    return self._head._element  # head of list means front of queue

  def getLast(self):
      """ Return (but do not remove) the element stored in tail.
          Note that:
                1. list's head means stack's top or peak.
                2. list's head means queue's front.
                3. list's tail means queue's read.

          Raise Empty exception if the list is empty.
      """
      if self.is_empty():
        raise Empty('SLL is empty')

      return self._tail._element # tail of list means rear of queue

  def getAt(self, index):
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
    while (temp) :
      if count == index:
        return temp._element
      temp = temp._next
      count += 1
    return -1
  def checkExist(self, e):
    """ Check and return the index of the first node in the list whose element = e.
        This method return -1 if e does not exist in the list.
    """
    # write your code here, then remove the keyword 'pass'
    temp = self._head
    count = 0
    while (temp):
      if e == temp._element:
        return f"{e} in index: {count}"
      count += 1
      temp = temp._next
    return -1
  def addFirst(self, e):
    """ Add the element e into the head of the list.
        This method is identical to stack's push
    """
    newNode = self._Node(e,self._head)      # create a newNode that links to head
    self._head = newNode  # links head to newNode

    if self._tail is None: #special case: the list is empty
      self._tail = newNode  # update reference to tail node

    self._size += 1

  def addLast(self, e):
    """ Add the element e into the head of the list.
        This method is identical to queue's enqueue
    """
    newNode = self._Node(e,None)   # newNode will be the new tail node

    if self.is_empty():
      self._head = newNode          # special case: previously empty
    else:
      self._tail._next = newNode

    self._tail = newNode            # update reference to tail node
    self._size += 1

  def removeFirst(self):
    """ Remove and return the first element of the list.
        This method is identical to:
          1. stack's pop
          2. dequeue from a queue

        Raise Empty exception if the list is empty.
    """
    if self.is_empty():
      raise Empty('SLL is empty')

    answer = self._head
    self._head = self._head._next
    self._size -= 1
    if self.is_empty():   # special case as the list is empty
      self._tail = None   # removed head had been the tail

    return answer._element

  def removeLast(self):
    """ Remove and return the last element of the list.
        Raise Empty exception if the list is empty.
    """
    if self.is_empty():
      raise Empty('SLL is empty')

    answer = self._tail
    if self._head._next is None: #List has only ONE node
      answer = self._head
      self._head = None
      self._tail = None
      self._size -= 1
      return answer._element

    #If the program reaches here,
    #Then there were at least TWO nodes in the list
    second_last = self._head
    while second_last._next._next:
      second_last = second_last._next

    answer = second_last
    second_last._next = None #None means self._tail._next
    self._tail = second_last
    self._size -= 1
    return answer._element

  def printSLL(self):
      """This function prints contents of SLL.

      It starts from head.
      """
      temp = self._head
      while (temp):
        print(temp._element)
        temp = temp._next

if __name__=="__main__":
  #Create an empty list
  mySLL = SLL()

  #Build the list
  mySLL.addFirst("Friday")
  mySLL.addFirst("Thursday")
  mySLL.addFirst("Wednesday")
  mySLL.addLast("Saturday")
  mySLL.addLast("Sunday")
  mySLL.addFirst("Tuesday")
  mySLL.addFirst("Monday")
  #
  # #print all elements of the list mySLL
  mySLL.printSLL()
  print("List's head = ", mySLL.getFirst())
  print("List's tail = ", mySLL.getLast())
  #
  # #Remove Sunday from the list
  mySLL.removeLast()
  print("The last item removed from the list")
  print("List's head = ", mySLL.getFirst())
  print("List's tail = ", mySLL.getLast())

  #Feel free to write your code to test other methods
  print(mySLL.checkExist("Wednesday"))
  print(mySLL.getAt(2))
