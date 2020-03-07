
import random

ans = True

while ans:
  question = input("Ask the 8 ball a question: Press 'NO' to quit")
  
  answers = random.randint(1,15)
  
  if question == "NO":
    break
    
  elif answers == 1:
      print ("It is certain")
    
  elif answers == 2:
      print ("Yes")
      
  elif answers == 3:
      print ("No way!")
      
  elif answers == 4:
      print ("Ask again later")
        
  elif answers == 5:
      print ("uh oh stinky!")
  
  elif answers == 6:
     print  ("dont ask me, its not like im magic ;)")

  elif answers == 7:
     print  ("Hell Na!!!!")

  elif answers == 8:
     print  ("gimmy a £10 and ill tell you")

  elif answers == 9:
     print  ("mabey mabey not, ask mr moore.")
      
  elif answers == 10:
     print  ("most definatly")

  elif answers == 11:
      print ("now that is a YES")

  elif answers == 12:
      print("100%")

  elif answers == 13:
      print("yes yes yes yes.....")
    
  elif answers == 14:
      print("Ohhh baby yes")

  elif answers == "no":
      print ("I'm sorry? I didn't understand, do you want to keep playing? If no, please type NO")
      

print ("Thanks for playing! See you next time! and remember dylan is better than jacob at minecraft!")
  
      
      
      