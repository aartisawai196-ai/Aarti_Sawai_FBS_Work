class Product:
    def __init__(self,pid,pname,price,qty):
        self.pid=pid
        self.pname=pname
        self.price=price
        self.qty=qty

    def ShowProduct(self):
        print(f'Product Id :{self.pid}')
        print(f'Product Name :{self.pname}')
        print(f'Product Price :{self.price}')
        print(f'Product Quantity :{self.qty}')

    def  __del__(self):
        self.pid=None
        self.pname=None
        self.price=None
        self.qty=None

        print(f'Product Id :{self.pid}')
        print(f'Product Name :{self.pname}')
        print(f'Product Price :{self.price}')
        print(f'Product Quantity :{self.qty}')
        

p1=Product(101,'Shampoo',2,10)
p2=Product(102,'Pen',5,20)

p1.ShowProduct()
p2.ShowProduct()