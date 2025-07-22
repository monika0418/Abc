file=open("C:\\VIP\\game.text","w")
file.write("I am Monika")
file.close()

#file read
file = open("C:\\VIP\\game.text","r")
content =file.read()
print(content)
file.close

#file append
file=open("C:\\VIP\\game.text","a")
file.write("\ngojan school of business and technology ")
file.close()

file=open("C:\\VIP\\game.text","r")
content =file.read()
print("after append")
print(content)
file.close()
