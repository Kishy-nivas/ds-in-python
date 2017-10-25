# stack

class stack(object):


    def __init__(self):
        self.content_array  =[]
        self.min_array = []
        self.min_element = float('inf')


    def push(self,value):
        self.content_array.append(value)
        if value < self.min_element:
            self.min_element = value
        self.min_array.append(self.min_element)

    def pop(self):
        if self.content_array:
            self.content_array.pop()
            self.min_array.pop()
        if self.min_array:
            self.min_element = self.min_array[-1]

    def peek(self):
        return  self.content_array[-1]

    def find_min (self):
        return self.min_element

if __name__ == '__main__':
    s = stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.find_min())
    print(s.peek()) 
    s.pop())
    s.push(4)
    print(s.peek() )
   


    """while 1:
        choice =0
        print ("1.push ")
        print ("2.pop")
        print ("3.find min ")
        print ("4.peek")
        print ("5 exit ")
        choice = input() 
        if choice ==1:
            print(" Enter the value : ")
            val = int(input())
            s.push(val)
        elif choice ==2 :
            s.pop() 
        elif choice ==3:
            print(s.find_min() )
        elif choice ==4:
         print(s.peek() )
        elif choice ==5:
            break

        """




