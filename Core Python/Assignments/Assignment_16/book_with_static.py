class Book:

    count=0
    def __init__(self,bid,bname,price,author):
        self.bid=bid
        self.bname=bname
        self.price=price
        self.author=author
        Book.count+=1


    def ShowBook(self):
        print(f'Book id :{self.bid}')
        print(f'Book Name :{self.bname}')
        print(f'Book Price :{self.price}')
        print(f'Book Author :{self.author}')


    def __del__(self):
        self.bid=None
        self.bname=None
        self.price=None
        self.author=None
        
        print(f'Book id :{self.bid}')
        print(f'Book Name :{self.bname}')
        print(f'Book Price :{self.price}')
        print(f'Book Author :{self.author}')
        


b1=Book(101,'Ramayana',500,'Rishi Walmiki')
b2=Book(102,'Dnyaneshwari',500,'Sant Dnyaneshwar')


b1.ShowBook()
b2.ShowBook()

print(f'No of objects created : {Book.count} \n')






