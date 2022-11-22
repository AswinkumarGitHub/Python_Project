import csv
import os
import random

f = open("log_in.txt",'a+')
f.close()
f = open("management.txt",'a+')
f.close()
f1=open("info.csv",'a',newline='')
f1.close()
c1=open("fees.csv",'a',newline='')
c1.close()
def register():
	print()
	u = input("Enter Username to register: ")
	p = input("Enter password: ")
	f = open("log_in.txt")
	data = f.readlines()
	up= u+' '+p+'\n'
	f.close()
	if up not in data:
		f = open("log_in.txt", 'a',newline='')
		f.write(u + ' ' + p + '\n')
		
		f.close()
		print("Registration successful",'\n')
	else:
		print("Aldredy registered",'\n')
		



def login():
	print()
	u = input("Enter Username: ")
	p = input("Enter password: ")
	f = open("log_in.txt")
	data = f.readlines()
	f.close()
	up = u+' '+p+'\n'
	if up in data:
		print('\nLogin successful!','\n')
		menue()
	else:
		print("Incorrect username or password"'\n')

        
        

def menue():
        while True:
                print("\t\t\tMENU")
                print("press 1:To know more about our School")#About
                print("press 2:To fill the new addmisiom form")#input
                print("press 3:To Search student details")# To search specific student detail 
                print("press 4:To Pay fee and fee Receipt")#Fee
                print("press 5:To Edit/Make change")#Edit- Del and insert 
                print("press 6:To Delete a student data")#Del
                print("press 7:To Display all Students data")#Exit
                print("press 8:To Exit")#Exit
                print('\n')
                f = input("Enter your choice: ")
                print('\n')
                if f=='1':
                        about()
                elif f=='2':
                        information()
                elif f=='3':
                        search()
                elif f=='4':
                        fee()
                elif f=='5':
                        edit()
                elif f=='6':
                        del1()
                elif f=='7':
                        show()       
                elif f=='8':
                        break
                else:
                        print("Wrong input")


def about():
        print("\t\tWELCOME TO AK SCHOOL\n")
        print("ABOUT US:\n")
        print("A community of men and women with a keen sense of Responsibility, Integrity, Initiative, Perseverance, Self- Reliance, Dedication and Loyalty.")
        print("We are a dedicated team working with a mission ,To render full, liberal and   comprehensive education, to develop the character, personality of the child,  an all round development and bring out the best in the child's body, mind and spirit.\n")
        print("AK School caters to students aspiring to study in CBSE stream. We provide quality education and all round development to our students.It is a co-educational school serving 9960 children from LKG to Std XII. The medium of instruction is English. AK School  was started on 6th June 1979 to synchronise with the International Year Of The Child. It is managed by the State Bank of India Officers Association , Chennai Circle.\n")
        print("The school is affiliated to Central Board of Secondary Education, New Delhi. The saga of the mite to the mighty is the 8 classes from Kindergarten to class VI in the introductory year 1979 with 282 students to 9679 students with 333 teaching faculties and 150 non teaching staff on its roll. The school has grown over the years in leaps and bounds.\n")




        
def information():
        
                
                f1=open("info.csv",'a',newline='')
                writer=csv.writer(f1)
                

                Name_of_student=(input("Name of student:"))
                print('\n')
                Name_of_Father=(input("Name of Father/Gardian:"))
                print('\n')
                Name_of_Mother=(input("Name of Mother:"))
                print('\n')
                address=(input("Address:"))
                print('\n')
                while('True'):
                        mobile_num=(input("Mobile number:"))
                        l=len(mobile_num)
                        if(l != 10):
                                print("Please do check your ur mobile number entered")
                                continue 
                        break 
                print('\n')
                while('True'):
                        gender=(input("Gender:"))
                        if gender.lower()!='male':
                                break
                        elif gender.lower()!='female':
                                break
                        else:
                                print("Give the correct gender")
                                continue 
                print('\n')
                dob=input("DOB_(DD/MM/YY):")
                print('\n')
                email_id=(input("Email_id:"))
                print('\n')
                print("Please uplode your Pastport size photo, Aadhar card,birth certificate,10th Marksheet (if applicable),Migration certificate(if applicable)")
                print('\n')
                fees=(input("Paid / Unpaid ?:"))
                if(fees.lower()=='unpaid'):
                        fees=fee()
                
                print('\n')
                
                writer.writerow([Name_of_student,Name_of_Father,Name_of_Mother,address,mobile_num,gender,dob,email_id,fees])
                f1.close()




def search():
        g=open("info.csv",'r',newline='\n')
        g1=open("search.csv",'w',newline='\n')
        search = csv.reader(g)
        writer= csv.writer(g1)
        writer.writerow(["Name of student","Name of Father/Gardian","Name of Mother","Address","Mobile number","Gender","DOB","Email_id"])
        value_to_be_found=(input("Enter the Name:"))
        print('\n')
        for i in search:
                if(i[0]==value_to_be_found):
                        print(i)
                        print('\n')
                        writer.writerow(i)
        g.close()
        g1.close()


def show():
        s=open("info.csv",'r',newline='\n')
        search = csv.reader(s)
        for i in search:
                        print(i)
                        print('\n')
                        
        s.close()
           
        


def fee():
        print('\n')
        print("\t\tWELCOME TO AK SCHOOL FEE PAYMENT\n")
        ch=(input("Press 1 to Pay or Press 2 to Pay later:"))
        if ch=='1':
                n=(input("Enter the Student Name:"))
                Date=(input("Enter the Date(DD/MM/YY):"))
                grade=(int(input("Enter your Child grade/Standard in number:")))
                if(grade<=5):
                        print('\n')
                        print("FEE STRUCTURE:\n")
                        print("Term fee           - 16,839.00")
                        print("Tuition fee        - 12,085.00")
                        print("Book fee           -  6,076.00")
                        print("Transport          -  5,000.00")
                        print("Sports Ext.class   -  3,000.00")
                        print("Lab equipments fee -  2,000.00")
                        print("------------------------------")
                        print("       Total       - 45,000.00")
                        print('\n')
                        pay=(input("Payment method:- Credit card , Debit card ,G-pay or other:"))
                        print('Transanction pending..')
                        print('\n')
                        status='Paid'
                        bill_No=random.randint(0,1000)
                        c1=open("fees.csv",'a',newline='\n')
                        writer= csv.writer(c1)
                        writer.writerow([Date,bill_No,n,grade,pay,status])
                        c1.close()
                        paid(bill_No,n,grade)
                else:
                        print('\n')
                        print("FEE STRUCTURE:\n")
                        print("Term fee           - 20,839.00")
                        print("Tuition fee        - 13,085.00")
                        print("Book fee           -  6,076.00")
                        print("Transport          -  5,000.00")
                        print("Sports Ext.class   -  3,000.00")
                        print("Lab equipments fee -  2,000.00")
                        print("------------------------------")
                        print("       Total       - 50,000.00")
                        print('\n')
                        pay=(input("Payment method:- Credit card , Debit card ,G-pay or other:"))
                        print('Transanction pending..')
                        print('\n')
                        status='Paid'
                        bill_No=random.randint(0,1000)
                        c1=open("fees.csv",'a',newline='\n')
                        writer= csv.writer(c1)
                        writer.writerow([Date,bill_No,n,grade,pay,status])
                        c1.close()
                        paid(bill_No,n,grade)
                return("Paid")
        elif ch=='2':
                return ("Unpaid")

        
                
                
def paid(num,name,g):
                print('Transanction Done for Bill.No:',num)
                print('Name:',name,'of grade:',g)
                print('\t\tRECEIPT')
                print("Term fee           - 16,839.00")
                print("Tuition fee        - 12,085.00")
                print("Book fee           -  6,076.00")
                print("Transport          -  5,000.00")
                print("Sports Ext.class   -  3,000.00")
                print("Lab equipments fee -  2,000.00")
                print("------------------------------")
                print("       Total       - 45,000.00")
                print('\n')
                print("\t\tALL PAID AND CLEAR ")
                print('THANKYOU FOR USING OUR AK SCHOOL FEE PAYMENT\n')
        

        

def edit():
        e=open("info.csv",'r',newline='\n')
        e1=open("edited.csv",'w',newline='\n')
        search = csv.reader(e)
        writer= csv.writer(e1)
        value_to_be_found=(input("Enter the Student's name where need to edit/Update:"))
        print('\n')
        for i in search:
                if(i[0]==value_to_be_found):
                        Name_of_student=(input("Name of student:"))
                        print('\n')
                        Name_of_Father=(input("Name of Father/Gardian:"))
                        print('\n')
                        Name_of_Mother=(input("Name of Mother:"))
                        print('\n')
                        address=(input("Address:"))
                        print('\n')
                        while('True'):
                                mobile_num=(input("Mobile number:"))
                                l=len(mobile_num)
                                if(l != 10):
                                        print("Please do check your ur mobile number entered")
                                        continue 
                                break 
                        print('\n')
                        while('True'):
                                gender=(input("Gender:"))
                                if gender.lower()!='male':
                                        break
                                elif gender.lower()!='female':
                                        break
                                else:
                                        print("Give the correct gender")
                                        continue 
                        print('\n')
                        dob=input("DOB_(DD/MM/YY):")
                        print('\n')
                        email_id=(input("Email_id:"))
                        print('\n')
                        fees=(input("Paid / Unpaid ?:"))
                        print('\n')

                        writer.writerow([Name_of_student,Name_of_Father,Name_of_Mother,address,mobile_num,gender,dob,email_id,fees])
                        
                        
                else:
                        writer.writerow(i)
                        
        e.close()
        e1.close()
        os.remove("info.csv")
        os.rename("edited.csv","info.csv")
        


def del1():

        
        d=open("info.csv",'r',newline='\n')
        d1=open("delete.csv",'w',newline='\n')
        search = csv.reader(d)
        writer= csv.writer(d1)
        dele= input("Please enter a Student's name to be deleted:")
        for j in search:
                if(j[0]==dele):
                        print("Deletion is done !")
                        print('\n')
                else:
                        writer.writerow(j)
                        
        d.close()
        d1.close()
        os.remove("info.csv")
        os.rename("delete.csv","info.csv")
        show()
        

        
             
	


while True:
    
    print("\t\tWELCOME TO AK SCHOOL MANAGEMENT SYSTEM")
    print("press 1: Register")
    print("press 2: Login")
    print("press 3: Exit")
    c = input("Enter choice: ")
    if c=='1':
        register()
    elif c=='2':
        login()
    elif c=='3':
        print("THANKYOU FOR USING OUR AK SCHOOL MANAGEMENT SYSTEM")
        break
    else:
        print("Wrong input")

