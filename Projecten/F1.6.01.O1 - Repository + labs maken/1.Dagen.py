from typing import Reversible


print ("1.lijst dagen")
print ("----------------------")

dagen = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]

# hier worden alle dagen getoont
print ("hier worden alle dagen getoond:")
print ("---------")
for alledagen in dagen [:7]:
    print (alledagen)
print ("---------")

# hier worden alle werkdagen getoond
print ("hier worden alle werkdagen getoond:")
print ("---------")
for werkdagen in dagen [:-2]:
    print (werkdagen)
print ("---------")

# hier worden alle weekenddagen getoond
print ("hier worden alle weekenddagen getoond:")
print ("---------")
print(dagen[-2])
print(dagen[-1])
print ("---------")

# hier worden alle weekdagen getoond omgedraaid
print ("alle weekdagen getoond omgedraaid")
print ("---------")
for alledagen in reversed(dagen):
    print(alledagen)
print ("---------") 

# hier worden alle werkdagen omgedraaid 
print ("omgedraaide werkdagen")
print ("---------") 
for werkdagen in reversed(dagen[:5]):
    print (werkdagen)
print ("---------") 

# hier worden de weekenddagen omgekeerd getoond
print ("omgekeerde weekenddagen")
print ("---------")
print(dagen[-1])
print(dagen[-2])
print ("---------") 

print ("bedankt voor het gebruiken van Milware!")
