text_1=str(input("Enter text to write to the file:"))
file_1=open("output.txt","w")
write_=file_1.write(text_1)
file_1.close()

text_2=str(input("Enter text to append to the file:"))
file_2=open("output.txt","a")
append_=file_2.write("\n"+text_2)
file_2.close()

file_3=open("output.txt","r")
read_=file_3.read()
print(read_)
file_3.close()
