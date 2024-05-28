a=open("ok.txt","w")
#write a new file using "W" mode for write the data
a.write(""" hii good morning....
        this is Raveendra,
        i am for kadapa distict,
        i am studying SV Arts college TTD thirupatic""")
#close the file ofter complete the file write close it
a.close()
b=open("ok.txt","r")
#read the file what u write in the prious using "R" mode
print(b.read())
b=open("ok.txt","a")
#adding the some off data using "a" mode to add the adta
b.write("""\n\t my hobbies are watching reels and eating Biryani and watching documentaries etc...""")
print(b)
#ofter append the data close it
b.close()
#again read the data for checking if it is appended or not
b=open("ok.txt","r")
print(b.read())
b.close()
g=open("ok.txt","r+")
c=g.read()
print(c)
g.write("\n \tMy strengths are self motivating and hardworkinng")
print(g.read())
g.close()
d=open("ok.txt","r")
print(d.read())
d.close()