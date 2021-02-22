class Publisher:
    def __init__(self,Pname):
        self.Pname=Pname
    def display(self):
        print("name",self.Pname)

class Book(Publisher):
    def __init__(self,Pname,Bname,title):
        self.Pname=Pname
        self.Bname=Bname
        self.title=title
    def display(self):
        print("Pname",self.Pname)
        print("Bname",self.Bname)
        print("title",self.title)


class Python(Book):
    def __init__(self,Pname,Bname,title,page,price):
        self.Pname=Pname;
        self.Bname=Bname;
        self.title=title;
        self.page=page
        self.price=price

    def display(self):
        print("Pname",self.Pname)
        print("Book",self.Bname)
        print("title",self.title)
        print("pages",self.page)
        print("Price",self.price)
      
n=input("Enter publisher")
B=input("Enter book")
t=input("Enter title")
p=int(input("Enter pages"))
pr=int(input("Enter price"))

obj=Python(n,B,t,p,pr)
obj.display()
      
                
