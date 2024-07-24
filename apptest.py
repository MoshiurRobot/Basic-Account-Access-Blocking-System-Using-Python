our_pass = "hello 123"
your_ans = ""
num_of_try = 0
num_of_max_try = 3
max_try = "Not Reached"

while your_ans != our_pass and max_try != "Reached":
    if num_of_try < num_of_max_try :
        your_ans = input("What is the Password? : ")
        num_of_try = num_of_try+1
    else:
        max_try = "Reached"

if max_try == "Reached":
    print("Access Blocked")
else:
    print("Access Granted")