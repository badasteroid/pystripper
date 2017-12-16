toAnalyze= input("enter the string that needs to be cleaned")

regex = input("enter the regex that will be deleted from the previous string")

print ("this string will get stripped: "+toAnalyze+"\nfrom the "+regex+" regex")

if (toAnalyze):
    
    if (regex in toAnalyze):
        
        clean = toAnalyze.split("(")
        
        i = clean.__len__()
        print(i)
        reform_clean=clean[0]
        for element in range(1, i):
            reform_clean+=clean[element][regex.__len__():]

        print("\n\n\nThe final result is: \n"+reform_clean)



