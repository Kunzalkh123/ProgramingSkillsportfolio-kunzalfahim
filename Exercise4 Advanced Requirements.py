#Advanced Requirements Exercise 4 
a = input("What is the capital of France? ")    
if a.lower()=='paris': 
    print('Correct Answer!')
    
else:                                           
    print("Incorrect Answer!")
    #Quiz

score=0 
ans1=input("What is the capital of Russia?")    
if ans1.lower()=='moscow':                      
    print("Correct!") 
    score+=1 
else:
    print("Incorrect answer!")
    print("your score is", score)
