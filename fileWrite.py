#"a" -Append -will append to the end of the file

#"w" - Write - will overwrite any existing content in the file 


#syntax to open a file 

#readText=open("text.text","r")
#print(readText.read())


#open er modde je syntax er file dibo  seta create hoye jabe

wr=open("hablu.html","w")

wr.write("<p>subscribe hablu programmer</p>")

#"w" use korle ager ta muche new ta create hobe 

wr=open("hablu.text","w")

wr.write("subscribe me\n")

#"a" use korar karone ager line gulao exist korbe 

wr=open("hablu.text","a")

wr.write("you are amazing")


#using "r" print what we write in the html or text file 
wr=open("hablu.text","r")

print(wr.read())