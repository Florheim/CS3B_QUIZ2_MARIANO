""""
Florheim Wizard V. Mariano
CS3B
Quiz No: 2
Date: October 11,2024
"""

studentName = "Lewis Fonsi"
studentAddress = "City of Candon, Ilocos Sur"
studentFavNum1 = 25                 #Declare the value as 25 as an integer
studentAge = 25                     #Declare the value as 25 as an integer
studentAllowance = float(500)       #Declare the value as 500 as an float with tycasting

classmateName = "Andrea Andres"
classmateAddress = "City of Vigan, Ilocos Sur"
classmateFavNum1 = "18"               #Declare the value as 18 as an string
classmateAge = "21"                   #Declare the value as 21 as an string
classmateAllowance = "700"            #Declare the value as 700 as an string

sName_Lenght = len(studentName)
cName_Lneght = len(classmateName)

if "Ilocos Sur" in studentAddress and "Ilocos Sur" in classmateAddress: #use as a condition if "Ilocos Sur" is in studentAddress and classsmateAddress.
    print("Lewis Fonsi is from ", studentAddress)   #Ouput: LEWIS FONSI is from City of Candon, Ilocos Sur - call and format your variables with concatenation techniques except fstring formatter
    print("Andrea Andres is from ", classmateAddress)   #Ouput: andrea andres is from City of Vigan, Ilocos Sur - call and format your variables with concatenation techniques except fstring formatter
    
    if sName_Lenght > cName_Lneght:
        print("aAndrea Andres has a longer name than Lewis Fonsi with 13 letters over 11 letters")  #andrea andres has a longer name than LEWIS FONSI with 13 letters and 11 letters
    else:
        print("Lewis Fonsi has a longer name than Andrea Andres with 13 letters over 11 letters")  #The oppposite result of IF Condition

elif "Ilocos Sur" in studentAddress and "Ilocos Sur" in classmateAddress: #use as a condition for elif "Ilocos Sur" is in studentAddress and classsmateAddress.
    sName_Split = studentName.split(" ")  #split the studentName with " " a space as identifier of the spliiter
    cName_Split = classmateName.split(" ")    #split the className with " " a space as identifier of the spliiter
    print("One among {sName_Split[0]} or {cName_Split[0]} lives in Ilocos Sur")   #One among Lewis or Andrea lives in Ilocos Sur" use the sName_split and cName_split and use of indexing
else:
    print("None of the students lives in Ilocos Sur")   #None of the students lives in Ilocos Sur
      
print(f"The addded age of Lewis Fonsi and Andrea Andres is",studentAge + int(classmateAge))  #print using fstring format: The addded age of studentAge and classmateAge, in addition to perform a mathematical
print(f"The subtracted age of Lewis Fonsi and Andrea Andres is",studentFavNum1 - int(classmateFavNum1))  #print using fstring format: The subtracted favNum of studentFavNum and classmateFavNum, in subtraction to perform a mathematical

combinedWeeklyAllowance = studentAllowance + float(classmateAllowance)
print(f"The added allowance of Lewis Fonsi and Andrea Andres is {float(combinedWeeklyAllowance):.2f} pesos")  #print using fstring format: the added allowances of the student and classmate allowance in printing the allowance make sure it is in 2 decimal form

classList = ['Lewis Fonsi', 'Andrea Andres']  #Create a list containing the value of student name and classmate name
classList_Ext = ['City of Candon, Ilocos Sur', 'City of Vigan, Ilocos Sur']      #Create a list containing the address of the student and classmate
classList.extend(classList_Ext)    #Extend the value of classList with classList_ext

for i in classList:
    print(i)              #print out the value of the classList using the for loop
    
classNumbers = [25, 25, 500, 18, 21, 700]  #Create a list cointaining all the numerical vars of the student, assure that all var are int 
classNumbers.append(int(classmateAge))     #append the classmateAge, Note that the list must contain int var only
classNumbers.append(int(classmateFavNum1))   #append the classmateFavNum, Note that the list must contain int var only
classNumbers.append(int(classmateAllowance))   #append the classmateAllowance, Note that the list must contain int var only
classNumbers.sort()

for i in classNumbers:
    print(i)            #print out the value of the classNumberes using the for loop
    
def quizTwo(studentNameCS):              #Create a simple function for QuizTwo() whichs receive a parameters studentNameCS
    print(f"Congratulations on Quiz 2 {studentNameCS}")     #Print wuth fstring format Ouput: Congratulations on Quiz 2 {passed variable}
quizTwo('Mariano')              #Call the function QuizTwo() passingg a variable value of the Name of the student of CS3B