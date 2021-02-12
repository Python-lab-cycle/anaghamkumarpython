class Arith:


  # init method or constructor
  def __init__(self, no1,no2):
      self.num1 = no1
      self.num2 = no2

      #sample method
    def  sum(self):
        #print('Hello, my name is', self,name)
        return(self.num1+self.num2)
a=int(input("Enter num1"))
b=int(input("Enter num2: "))
p = Arich(a,b)
print('sum=',p.sum() )
            
