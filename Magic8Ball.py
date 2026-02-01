#Magic8Ball.py
#Name:Tori Gregory
#Date:2/1/26
#Assignment: Lab 2

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
 
  #Prompt the user for their question.
 input("Please ask a question:" )
  #Answer question randomly with one of the options from your earlier list.
answers = ["Yes", "No", "Maybe", "Ask again later", "Most certainly", "Definitely Not",
           "Probably", "Most Likely", "Most likely Not", "Try again ", "Don't count on it", "It is certain",
           "Cannot predict now", "Better not tell you now"]
response = random.choice(answers)
print(response)
if __name__ == '__main__':
  main()
