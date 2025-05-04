try:
   file1=open("sample.txt","r")
   read_=file1.readline()
   read_2=file1.readline()
   print("Line1:",read_)
   print("Line2:",read_2)
   file1.close()
except FileNotFoundError:
   print("error:The file sample.txt not found ")