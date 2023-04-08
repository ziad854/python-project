
import os
while True:
    x=input("write 0 to exit program\n choose admin/user: ")
    if x=="admin":
        while True: #loop for the whole admin

            while True: #loop for taking admin data input
                
                ad_id=input("Enter admin ID: ")
                ad_name=input("Enter admin name: ")
                ad_email=input("Enter admin email : ")
                ad_password=input("Enter admin password: ")
                name=os.listdir("/Users/ziadgahenm/Desktop/hacking/projectis/admin")
                if ad_name+'.txt' in name:
                    break
                else:
                    print("that is not a valide admin name\n enter anothr one")
                    continue
            
            with open(f"/Users/ziadgahenm/Desktop/hacking/projectis/admin/{ad_name}.txt",'r') as file:
                cont=file.readlines()
                id=cont[0].strip("\n")
                name=cont[1].strip("\n")
                email=cont[2].strip("\n")
                password=cont[3].strip("\n")

                if ad_id==id and ad_name == name  and  ad_email == email and ad_password == password:
                    while True:
                        
                        ad_menu=input("""choose from the menu:
                            1-Add vaccination center.
                            2-Remove vaccination center.
                            3-Search for center.
                            4- list of users.
                            5-request.
                            6-enter 6 to return to admin/user menu.\n""")

                        if ad_menu=='1':
                            files=os.listdir("/Users/ziadgahenm/Desktop/hacking/projectis/vaccination_centers")
                            vac_id=str(len(files)+1)
                            while True:
                                vac_name=input("enter vaccination name:")
                                if vac_name in files:
                                    x=input("there is already a center with that name please enter diffrent one\n")
                                    continue
                                else:
                                    break
                            vac_address=input("enter vaccination address:")
                            vac_no=int(input("enter vaccination number:"))
                            vaccines = []
                            for i in range(0, vac_no):
                                vaccines.append(input("enter vaccine name: "))
                            with open (f"/Users/ziadgahenm/Desktop/hacking/projectis/vaccination_centers/{vac_name}.txt","a+") as file1:

                                file1.write("ID: "+vac_id+"\n")
                                file1.write("vaccination center name: "+vac_name+"\n")
                                file1.write("vaccination center address: "+vac_address+"\n")
                                file1.write("availble vaccine: "+str(vaccines)+"\n")
                            x=input("vaccination center is added succesfully.\n choose 0 to exit or any number to choose another opreation :")
                            if x!='0':
                                continue
                            else:
                                raise SystemExit
                            
                            
                        elif ad_menu=='2':
                            del_cen=os.listdir("/Users/ziadgahenm/Desktop/hacking/projectis/vaccination_centers")
                            for item in del_cen:
                                print(item.strip(".txt"))
                            vac_del=input("Enter name of center to delete it: ")
                            del_center=f"/Users/ziadgahenm/Desktop/hacking/projectis/vaccination_centers/{vac_del}.txt"
                            if os.path.isfile(del_center):
                                os.remove(del_center)
                                print("center has been deleted.")
                            else:
                                print("Not existed.")
                            x=input("choose 0 to exit or any number to choose another opreation :")
                            if x!='0':
                                continue
                            elif x=='0':
                                raise SystemExit
                        elif ad_menu=='3':
                            vac_search=input("Enter your desired center: ")
                            search_center = f"/Users/ziadgahenm/Desktop/hacking/projectis/vaccination_centers/{vac_search}.txt"
                            if os.path.isfile(search_center):
                                with open(search_center,"r") as file:
                                    cont=file.read()
                                    print(cont)        
                            else:
                                ("center is not found")
                            x=input("choose 0 to exit or any number to choose another opreation :")
                            if x!='0':
                                continue
                            elif x=='0':
                                raise SystemExit          
                        elif ad_menu=='4':
                            user_names=os.listdir("/Users/ziadgahenm/Desktop/hacking/projectis/user")
                            for item in user_names:
                                print(item.strip(".txt"))
                            while True:
                                u_name=input("please enter a user name to check statues :")
                                if os.path.isfile(f"/Users/ziadgahenm/Desktop/hacking/projectis/requests/{u_name}.txt"):
                                        print("\n"+u_name+"    pending \n")
                                        break
                                elif os.path.isfile(f"/Users/ziadgahenm/Desktop/hacking/projectis/accepted/{u_name}.txt"):
                                        print(f"\n{u_name}    accepted\n") 
                                        break
                                elif os.path.isfile(f"/Users/ziadgahenm/Desktop/hacking/projectis/user/{u_name}.txt"):
                                    print(f"\n{u_name}\tis registere user and has no previous requests\n")
                                    break    
                                else:
                                    print("wrong name")
                                    continue 

                            x=input("choose 0 to exit or any number to choose another opreation :")
                            if x!='0':
                                continue
                            elif x=='0':
                                raise SystemExit          
                        elif ad_menu=='5':
                            req=os.listdir("/Users/ziadgahenm/Desktop/hacking/projectis/requests")
                            for item in req:
                                print(item.strip(".txt"))
                            while True:
                                if len(os.listdir("/Users/ziadgahenm/Desktop/hacking/projectis/requests"))==0:
                                    print("there is no request")
                                    break
                                user_req=input("Enter ID to accept request :")
                                req_user=f"/Users/ziadgahenm/Desktop/hacking/projectis/requests/{user_req}.txt"
                                
                                                                  
                                if os.path.isfile(req_user):
                                    os.remove(req_user)
                                
                                    with open(f"/Users/ziadgahenm/Desktop/hacking/projectis/accepted/{user_req}.txt",
                                        "a+") as file:
                                        date=input("enter the date: ")
                                        # file.write(user_req+'\n')
                                        file.write(date)

                                        x=input("Request accepted\n choose 0 to return to main menu or any number to cheak another request:")
                                        if x!='0' and len(os.listdir("/Users/ziadgahenm/Desktop/hacking/projectis/requests"))==0 :
                                            continue
                                        else:
                                            break
                                else:
                                     print("wrong ID\n")   
                        elif ad_menu=='6':
                            break    
                        else:
                            x=input("this is not an option\n choose 0 to exit or 1 to return to admin/user or any other number to try again")
                            if x=='0':
                                raise SystemExit
                            elif x=='1':
                                break
                            else:
                                continue  
                    break    
                
                else:
                    x=input("either admin is  not found or please cheak your data\n choose any number to try again or enter 0 to exit :")
                    if x!='0':
                        continue
                    else:
                        raise SystemExit            

            
            













    elif x=="user":

        while True:
            user_type = input("write 1 to return to admin/user menu\nchoose login/register : ")

            if user_type=="register":
                user_name=input("please enter your name :")
                user_email=input("please enter your email:")
                user_pass=input("please enter your password :")
                user_phone=input("please enter your phone number :")
                user_nat_ID=input("please enter your national ID :")
                user_fold="/Users/ziadgahenm/Desktop/hacking/projectis/user"
                if os.path.isfile(f"/Users/ziadgahenm/Desktop/hacking/projectis/user/{user_name}.txt"):
                    print("there is already a file with this name please either log in or user other username. ")
                    continue

                with open (f"/Users/ziadgahenm/Desktop/hacking/projectis/user/{user_name}.txt","w+") as file:
                    print(len(os.listdir(user_fold)))
                    user_id = len(os.listdir(user_fold))+1
                    file.write(f"user ID: {user_id}\n")
                    file.write(f"user name: {user_name}\n")
                    file.write(f"user email: {user_email}\n")
                    file.write(f"user pass: {user_pass}\n")
                    file.write(f"user phone: {user_phone}\n")
                    file.write("user national ID: "+user_nat_ID+"\n\n")
                    print(f"your ID is :({user_id}) please remember it\n your register is completed now login :)")




            elif user_type=="login":
                name_user=input("please enter your name :")
                pass_user=input("please enter your password :")
                if os.path.isfile(f"/Users/ziadgahenm/Desktop/hacking/projectis/user/{name_user}.txt"):

                    with open(f"/Users/ziadgahenm/Desktop/hacking/projectis/user/{name_user}.txt", "r") as file:

                        user_cont = file.readlines()

                        us_name=user_cont[1].strip("\n")
                        us_pass=user_cont[3].strip("\n")


                    if us_name == f"user name: {name_user}" and  us_pass == f"user pass: {pass_user}":
                        while True:
                            user_menu=input(f"""hello {name_user}
                            please choose your option:
                            1.reserve a vaccination
                            2.track your request
                            3.to return to the login/register menu.
                            """)
                            if user_menu=='1':
                                req=os.listdir("/Users/ziadgahenm/Desktop/hacking/projectis/vaccination_centers")
                                for item in req:
                                    print(item.strip(".txt"))
                                center_search=input("please enter vaccination center name to display it's data :")

                                with open (f"/Users/ziadgahenm/Desktop/hacking/projectis/vaccination_centers/{center_search}.txt","r") as file:
                                    vac_cont=file.read()
                                    print(vac_cont)

                                    user_req1=input("please enter your vaccination center ID :")
                                    user_req2=input("please enter your vaccine name :")
                                    name_user=input("please enter your name :")

                                    # if user_req1 in vac_cont and name_user in user_cont and user_req2 in vac_cont:
                                    with open(f"/Users/ziadgahenm/Desktop/hacking/projectis/requests/{name_user}.txt","w+") as file:
                                                    
                                            file.write(user_req1 + "\n")
                                            file.write(user_req2 + "\n")
                                            file.write(name_user + "\n")
                                    print ("your request is submeted successfuly  ")
                                    x = input("choose 0 to exit or any number to choose another opreation :\n")

                                if x != '0':
                                    continue
                                elif x == '0':
                                    raise SystemExit
                            elif user_menu=='2':
                                name1 = input("please enter your name to check your request :")
                                if os.path.isfile(f"/Users/ziadgahenm/Desktop/hacking/projectis/accepted/{name1}.txt") or os.path.isfile(f"/Users/ziadgahenm/Desktop/hacking/projectis/requests/{name1}.txt"):
                                    ch_acc = os.listdir("/Users/ziadgahenm/Desktop/hacking/projectis/accepted")
                                    ch_req= os.listdir("/Users/ziadgahenm/Desktop/hacking/projectis/requests")
                                    for item in ch_acc:
                                        if name1 == item.strip(".txt"):
                                            
                                            print("accepted")
                                    for item in ch_req:
                                        if name1==item.strip(".txt"):
                                            print("your request still in checking progress")
                                else:
                                    print("there is no request")            
                                x = (input("choose 0 to exit or any number to choose another opreation :\n"))
                            
                                if x != '0':
                                    continue
                                elif x == '0':
                                        raise SystemExit
                            elif user_menu=='3':
                                break
                            
                        

                else:
                    print("there is no such name or password")                        

            elif user_type=='1':
                break
            else:
                print("this is not an option :)")

                x =input("choose 0to exit program or 1 to return to login/register menu or any other number to try again :")
                if x != '0' and x !='1':
                    continue
                elif x=='1':
                    break
                elif x == '0':
                    raise SystemExit
    elif x=='0':
        raise SystemExit                

    
    else:
        x=input("this not a choice\n choose 0 to exit program or 1 to return to user/admin menu or any other number to try again :\n")

        if x!='0' and x!='1':
            continue
        elif x=='1':
            break
        elif x=='0':
            raise SystemExit
