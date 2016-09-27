#This program will check for profanity in text file

print "Hello, I will be checking sample.txt"
print "\n\n"

swear = ["shit", "Shit", "Fuck", "fuck", "Bastard", "bastard", "Cunt", "cunt"]
samp = open("sample.txt")

check = samp.read()

count = 0
for i in swear:
    #count = 0
    if i in check:
        count += 1

if count > 0:
    print "This file contains profanity!"
else:
    print "This file contains no profanity."
