import mysql.connector as pysql
import calendar as cal
conn=pysql.connect(host="localhost",user="root",passwd=" ",database="project")
curr=conn.cursor()

print("Welcome!")
print("Who are you?")
print("1. Admin")
print("2. New User")
a=int(input("Please enter 1 or 2: "))
if a==1:
    b=input("Enter password: ")
    if b=="123456":
        while True:
            print("Welcome Admin! \n What do you want to do today?")
            print("1. View Database\n2. Change Database Entries\n3. Add Entries\n4. Exit")
            c=int(input("Enter your choice: "))
            if c==1:
                q1="select * from dest"
                curr.execute(q1)
                print(curr.fetchall())
            elif c==2:
                print("What Do You Want To Modify?")
                print(" 1.Destination Description\n2. Recommended Tourist Sites\n3. Package\n4. Exit")
                d=int(input("Enter your choice: "))
                
                        
                if d==1:
                    moddata3=input("Enter The destination  Whose des You Want To Modify:")
                    q7="select destid from dest where destname=%s"
                    v2=(moddata3,)
                    curr.execute(q7,v2)
                    if curr.fetchone():
                        print("ID exists")
                        desc=input("Enter New description:")
                        q4="update dest set destdesc=%s where destname=%s"
                        val4=(desc,moddata3)
                        curr.execute(q4,val4)
                        conn.commit()
                    else:
                        print("Value Does Not Exist In Table")
                        break
                elif d==2:
                    moddata4=int(input("Enter The Destination ID For Which You Want To Change the Tourist Attractions: "))
                    q7="select sites from dest where destid=%s"
                    v3=(moddata4,)
                    curr.execute(q7,v3)
                    if curr.fetchone():
                        print("ID exists")
                        toatt=input("Enter The New Tourist Attractions: ")
                        q4="update dest set sites=%s where destid=%s"
                        val3=(toatt,moddata4)
                        curr.execute(q4,val3)
                        conn.commit()
                    else: 
                        print("Value Does Not Exist In Table")
                        break
                elif d==3:
                     moddata5=input("Enter The Destination Whose Package You Want To Modify:")
                     q7="select package from dest where destname=%s"
                     v4=(moddata5,)
                     curr.execute(q7,v4)
                     if curr.fetchone():
                         print("ID exists")
                         desc=int(input("Enter New Package:"))
                         q4="update dest set package=%s where destname=%s"
                         val4=(desc,moddata5)
                         curr.execute(q4,val4)
                         conn.commit()
                     else:
                         print("Value Does Not Exist In Table")
                         break
                elif d==4:
                    continue
            elif c==3:
                did=int(input("Enter The Destination id: "))
                q8="select package from dest where destid=%s"
                v5=(did,)
                curr.execute(q8,v5)
                if curr.fetchone():
                    print("ID Exists")
                    print("You Cannot Add A Record With This id\nTry Using Another id")
                    continue
                dn=input("Enter Destination Name:")
                dd=input("Enter Short Description For Destination: ")
                dt=input("Enter Tourist Spots:")
                dp=input("Enter Tourist Package: ")
                q5="insert into dest (destid,destname,destdesc,sites,package) values(%s,%s,%s,%s,%s)"
                val5=(did,dn,dd,dt,dp)
                curr.execute(q5,val5)
                conn.commit()
            elif c==4:
                break
            
elif a==2:
    print("Welcome New User! What Do You Want To Do Today?")
    print("1. Make a Booking\n2. Browse our Database\n3. Make Payment\n4.Exit")
    e=int(input("Please Enter Your Choice:"))
    if e==1:
        print("Services Provided By Us")
        q6="select destname,destdesc,sites,package from dest"
        curr.execute(q6)
        print(curr.fetchall())
        print("Please Enter The Following Personal Details Required For Your Booking: ")
        usern=input("CHOOSE USERNAME:  ")
        pasw=input("CHOOSE PASSWORD")
        cfname=input("FIRST NAME: ")
        clname=input("LAST NAME: ")
        cmob=int(input("MOBILE NUMBER: "))
        cema=input("EMAIL: ")
        print("Please Enter  Travel Related Details: ")
        cdest=input("DESTINATION: ")
        cno=int(input("NUMBER OF PEOPLE TRAVELLING: "))
        cdays=int(input("NUMBER OF DAYS: "))
        citd=input("Enter City of Departure")
        mot=input("Enter Mode of Transport: ")
        print("Choose The Days You Will Be Travelling: ")
        print ("The calendar of year 2023 is : ")
        print (cal.calendar(2023))
        mon=int(input("Enter The Month Number: "))
        print(cal.month(2023, mon))
        fday=int(input("Enter the start/first date: "))
        lday=fday+cdays
        print("Your last day will be",lday)

        print("Great Dates are Available")
        q6="insert into client(Usern,Password,FirName,LasName,Mob,Email,Destination,Nump,Numd,CiDep,Transport,Month,Fdate,Ldate) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val6=(usern,pasw,cfname,clname,cmob,cema,cdest,cno,cdays,citd,mot,mon,fday,lday)
        curr.execute(q6,val6)
        conn.commit()
        print("INFORMATION REGISTERED SUCCESSFULLY!")
        q=int(input("Enter 0 To Continue To Payment or 9 to exit"))
        if q==0:
            print("Welcome",usern,"!")
            p=input("Enter The Password: ")
            if p==pasw:
                q7="select Firname,LasName, Destination,Nump,Numd,CiDep,Transport,Fdate,Ldate from client where password=%s"
                p1=p,
                curr.execute(q7,p1)
                print(curr.fetchone())
                q8="select package from dest where destname=%s"
                val7=(cdest,)
                curr.execute(q8,val7)
                var=curr.fetchone()
                print("The Amount You Need To Pay Is:",var)
                while True:
                    print("Proceeding to Payment Section: ")
                    print("PAYMENT METHODS OFFERED BY US:")
                    print("1. Net Banking\n2. Credit Card\n3. Debit Card\n4. UPI\n5. Exit")
                    paym=input("Enter Your Payment Method Number Given Above: ")
                    if paym==1:
                        m=input("enter Bank number: ")
                        amt1=int(input("Enter The Amount You Want To Pay Now: "))
                        n=var[0]
                        if amt1==n:
                            print("Payment Successful!\nYour Booking Is confirmed")
                            time1=input("Enter The Time You Want To Be Picked Up At : ")
                            print("We have contacted Uber and the Assigned Driver  Will Pick You Up at",time1,"\n")
                        else:
                            print("You Need To Pay The Entire Amount At one Go ")
                            g=int(input("Enter 0 to go back to payment Section "))
                            if g==0:
                                continue 
                            else:
                                break
                    elif paym==2:
                        m=input("enter card number: ")
                        amt1=int(input("Enter The Amount You Want To Pay Now: "))
                        n=var[0]
                        if amt1==n:
                            print("Payment Successful!\nYour Booking Is confirmed")
                            time1=input("Enter The Time You Want To Be Picked Up At : ")
                            print("We have contacted Uber and the Assigned Driver  Will Pick You Up at",time1,"\n")
                        else:
                            print("You Need To Pay The Entire Amount At one Go ")
                            g=int(input("Enter 0 to go back to payment Section "))
                            if g==0:
                                continue 
                            else:
                                break
                    elif paym==3:
                        m=input("enter card number: ")
                        amt1=int(input("Enter The Amount You Want To Pay Now: "))
                        n=var[0]
                        if amt1==n:
                            print("Payment Successful!\nYour Booking Is confirmed")
                            time1=input("Enter The Time You Want To Be Picked Up At : ")
                            print("We have contacted Uber and the Assigned Driver  Will Pick You Up at",time1,"\n")
                        else:
                            print("You Need To Pay The Entire Amount At one Go ")
                            g=int(input("Enter 0 to go back to payment Section "))
                            if g==0:
                                continue 
                            else:
                                break
                    elif paym==4:
                        m=input("enter UPI id : ")
                        amt1=int(input("Enter The Amount You Want To Pay Now: "))
                        n=var[0]
                        if amt1==n:
                            print("Payment Successful!\nYour Booking Is confirmed")
                            time1=input("Enter The Time You Want To Be Picked Up At : ")
                            print("We have contacted Uber and the Assigned Driver  Will Pick You Up at",time1,"\n")
                        else:
                            print("You Need To Pay The Entire Amount At one Go ")
                            g=int(input("Enter 0 to go back to payment Section "))
                            if g==0:
                                continue 
                            else:
                                break
                    else: 
                        break
    elif e==2:
        print("Here are all the options for you")
        q13="select * from dest"
        curr.execute(q13)
        a=curr.fetchall()
        for i in a:
            print(a)
    elif e==3:                
        print("Welcome!")
        w1=input("Enter your username:")
        q9="select user_id from client where Usern=%s"
        v6=(w1,)
        curr.execute(q9,v6)
        if curr.fetchone():
            print("Username Exists")
            p=input("Enter the password: ")
            q10="select Password from client where Usern=%s"
            v7=(w1,)
            curr.execute(q10,v7)
            p1=curr.fetchone()
            p2=str(p1[0])
            print(p2)
            if p==p2:
                print("Password matches\nWelcome",w1)
                q7="select Firname,LasName, Destination,Nump,Numd,CiDep,Transport,Fdate,Ldate from client where password=%s"
                curr.execute(q7,p1)
                b1=curr.fetchone()
                print(b1)
                b2=b1[2]
                b3=b2,
                print(b3)
                q8="select package from dest where destname=%s"
                curr.execute(q8,b3)
                var=curr.fetchone()
                print("The Amount You Need To Pay Is:",var)
                while True:
                    print("Proceeding to Payment Section: ")
                    print("PAYMENT METHODS OFFERED BY US")
                    print("1. Net Banking\n2. Credit Card\n3. Debit Card\n4. UPI\n5. Exit")
                    paym=int(input("Enter Your Payment Method Number Given Above: "))
                    if paym==1:
                        m=input("enter Bank number: ")
                        amt1=int(input("Enter The Amount You Want To Pay Now: "))
                        n=var[0]
                        if amt1==n:
                            print("Payment Successful!\nYour Booking Is Confirmed")
                            time1=input("Enter The Time You Want To Be Picked Up At : ")
                            print("We have contacted Uber and the Assigned Driver  Will Pick You Up at",time1,"\n")
                        else:
                            print("You Need To Pay The Entire Amount At one Go ")
                            g=int(input("Enter 0 to go back to payment Section "))
                            if g==0:
                                continue 
                            else:
                                break
                                
                    elif paym==2:
                        m=input("enter card number: ")
                        amt1=int(input("Enter The Amount You Want To Pay Now: "))
                        n=var[0]
                        if amt1==n:
                            print("Payment Successful!\nYour Booking Is confirmed")
                            time1=input("Enter The Time You Want To Be Picked Up At : ")
                            print("We have contacted Uber and the Assigned Driver  Will Pick You Up at",time1,"\n")
                        else:
                            print("You Need To Pay The Entire Amount At one Go ")
                            g=int(input("Enter 0 to go back to payment Section "))
                            if g==0:
                                continue 
                            else:
                                break
                    elif paym==3:
                        m=input("enter card number: ")
                        amt1=int(input("Enter The Amount You Want To Pay Now: "))
                        n=var[0]
                        if amt1==n:
                            print("Payment Successful!\nYour Booking Is confirmed")
                            time1=input("Enter The Time You Want To Be Picked Up At : ")
                            print("We have contacted Uber and the Assigned Driver  Will Pick You Up at",time1,"\n")
                        else:
                            print("You Need To Pay The Entire Amount At one Go ")
                            g=int(input("Enter 0 to go back to payment Section "))
                            if g==0:
                                continue 
                            else:
                                break
                    elif paym==4:
                        m=input("enter UPI id : ")
                        amt1=int(input("Enter The Amount You Want To Pay Now: "))
                        n=var[0]
                        if amt1==n:
                            print("Payment Successful!\nYour Booking Is Confirmed")
                            time1=input("Enter The Time You Want To Be Picked Up At : ")
                            print("We have contacted Uber and the Assigned Driver  Will Pick You Up at",time1,"\n")
                        else:
                            print("You Need To Pay The Entire Amount At One Go ")
                            g=int(input("Enter 0 to go back to payment Section "))
                            if g==0:
                                continue 
                            else:
                                break
                        
                    else: 
                        break
