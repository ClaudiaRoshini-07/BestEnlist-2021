//Create a real time scenario for inheritance example Banking concept

class Bank:
    def f(self):
        input("Enter Your Name :")
class Branch(Bank):
    def f1(self):
        input("Enter the Branch Name:")
class ACCOUNT(Bank):
    def f2(self):
        input("Enter Your Account Number :")
class IFSC(ACC):
    def f3(self):
        input("Enter IFSC CODE :")
class amount(Bank):
    def f4(self):
        input("Enter Amount You Want to Deposit :")
        print("Payment Successful!!")
        print("Credited Amount will be Updated Soon")
        

a=Bank()
b=Branch()
c=ACCOUNT()
d=IFSC()
e=amount()
a.f()
b.f1()
c.f2()
d.f3()
e.f4()

OUTPUT:
  
Enter Your Name :tina
Enter the Branch Name:CR32456789
Enter Your Account Number :43257849282
Enter IFSC CODE :73CD892
Enter Amount You Want to Deposit :1000
Payment Successful!!
Credited Amount will be Updated Soon
