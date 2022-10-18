class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class groceryGoods:
    def __init__(self, No, Code, Name, Price):
        self.No = No
        self.Code = Code
        self.Name = Name
        self.Price = Price
    def __str__(self):
        return f"""No: {self.No};
Code: {self.Code};
Name: {self.Name};
Price: {self.Price}"""
    def set_Price(self,newPrice):
        self.Price = newPrice

class SLL:
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def empty(self):
        return self.head is None
    def searchByCode(self,code):
        temp = self.head
        while temp:
            if code == temp.data.Code:
                print("Search is Successfuly")
                return print(temp.data)
            temp = temp.next
        print("Search is Fail")
    def add_first(self, el):
        p = Node(el)
        if self.empty():
            self.head = self.tail = p
        else:
            p.next = self.head
            self.head = p

    def sized(self):
        count = 0
        tmp = self.head
        while tmp is not None:
            count = count + 1
            tmp = tmp.next
        return count

    def printAll(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.data, end='\n')       #print all info of Goods
            tmp = tmp.next
        if self.empty():
            print('List is empty')
    def Unique_Code_Dict(self):
        dicOfCode = {}
        tmp = self.head
        while tmp is not None:
              dicOfCode[tmp.data.Code] = []
              tmp = tmp.next
        return dicOfCode            #dictionary of Goods with key is Code and Value is empty list
    def groupByCode(self,code):
        tmp = self.head
        dicOfCode = self.Unique_Code_Dict()
        for key,val in dicOfCode.items():
          while tmp is not None:
            if tmp.data.Code == key:
              val.append(tmp.data.Price)
            tmp = tmp.next
        return code ,dicOfCode[code]
    def maxPrice(self):
        tmp = self.head
        max = int(tmp.data.Price)
        while tmp is not None:
            if int(tmp.data.Price) > max:
                max = int(tmp.data.Price)
            tmp = tmp.next
        result = []
        tmp = self.head
        while tmp is not None:
            if int(tmp.data.Price) == max:
                result.append(tmp.data.Code)
            tmp = tmp.next
        return result
    def equalPrice(self,price):            #Print all of code which equal the Price is user input
        tmp = self.head
        result = []
        while tmp is not None:
            if int(tmp.data.Price) == price:
                result.append(tmp.data.Code)
            tmp = tmp.next
        return result
    def updatePrice(self,code=None,newPrice:int=None,path=None):
        if path is not None:
            handle = open(path,"r")
            lines = handle.readlines()
            tmp = self.head
            for line in lines:
                pairOfCode = line.split(" ")
                while tmp is not None:
                    if tmp.data.Code == pairOfCode[0]:
                        tmp.data.set_Price(pairOfCode[1])
                    tmp = tmp.next
        else:
            tmp = self.head
            while tmp is not None:
                if tmp.data.Code == code:
                    tmp.data.set_Price(newPrice)
                    break
                tmp = tmp.next
            if tmp is None:
                print("Can't find your Product's Code")
                return -1
        result = open("e.txt","w")
        for code in sll.maxPrice():
            result.write(code + "\n")
        print("Update new Price Succesfully")

def load_data(sll):
    handle = open("groceryGoods.csv", "r")
    lines = handle.readlines()
    for line in lines[1:]:
      Goods = groceryGoods(*line.split(','))
      sll.add_first(Goods)
    return sll.printAll()

if __name__ == "__main__":
  sll = SLL()
  load_data(sll)
  result = open("d.txt","w")
  lstMax = sll.maxPrice()
  for code in lstMax:
    result.write(code + "\n")
  sll.updatePrice(path="update.txt")
  sll.updatePrice(code="FO18530",newPrice=3400)


#Not finish task (f)
