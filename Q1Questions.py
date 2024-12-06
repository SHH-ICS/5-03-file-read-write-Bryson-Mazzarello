filehandle = open("questions.txt","w"); print("Question?"); filehandle.write(input()+'\n')
for i in range(4):
    print("Question :", i+1); filehandle.write(input()+'\n')
print("Correct Response : (State Number)"); filehandle.write(input()+'\n'); filehandle.close()