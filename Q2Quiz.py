# Create a second program that will read the file questions.txt, formatted as described above, and pose the questions to the user. 
# The program will keep score of the number of questions answered correctly.
file = open("questions.txt","r"); table = file.readlines()
for i in range(5):
    print(table[i+1])
if input()+'\n' == table[i+1]:
    print("You win")
else:
    print("You lose")
    print(table[i+1])