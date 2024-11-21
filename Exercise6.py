#Exercise 6: Brute Force Attack
password='12345' 
while True:     
    ans= input("Enter the password: ") 
    if ans==password: 
        print("Your answer is correct!")
        break 
    else:
        print("incorrect! Try again!")

#Advanced Requirement:
12345
maxi_attempts = 5 
correct_pass = '12345' 
attempts = 0    
while attempts < maxi_attempts:
    password = input("Enter the password: ")  
    if password == correct_pass:
        print('Correct Password!')
        break 
    else:
        attempts +=1
        remaining_attempts= maxi_attempts - attempts
        if remaining_attempts > 0:
            print(f"Incorrect! You have {remaining_attempts} attempts left.")  
        else:
            print("You have reached the maximum number of attempts. The authorities have been informed")