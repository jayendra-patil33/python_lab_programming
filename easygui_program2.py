from easygui import *
import sys

while 1:
   msgbox("Hello, welcome to supermarket !!")
   
   msg1="Enter choice of items"
   title="billing"
   choices=["CHOCOLATES","BISCUITS","SOAPS","CLOTHS"]
   choice=choicebox(msg1,title,choices)
   if str(choice)=="CHOCOLATES":
    msg2="Enter the choice of chocolate"
    title3="chocolate"
    choice1=["Dairymilk","Harsheys","Nutella","Kitkat","Gems"]
    choice2=choicebox(msg2,title3,choice1)
   elif str(choice)=="BISCUITS":
    msg3="Enter the choice of biscuits"
    title4="biscuits"
    choice3=["Parle","Marie","Orea","Bourbon","Hide & seek"]
    choice4=choicebox(msg3,title4,choice3)
   else :
    sys.exit(0)
   elif str(choice)=="SOAPS":
    msg2="Enter the choice of soap"
    title3="Soap"
    choice1=["Lux","Pears","asd","Kitkat","Gems"]
    choice2=choicebox(msg2,title3,choice1)

