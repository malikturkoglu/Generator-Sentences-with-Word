# -*- coding: utf-8 -*-
"""
@author: Malik Türkoğlu , Ömer Okumuş , Varol Koçoğlu , Mert Egi
"""
import random


class generateWordPartOne:
    def __init__ (self,totalSearching):
        self.totalSearching=totalSearching
    
    def generateWord(self, ValueWord, nounValue, nounList):  # this function help us for find a word , we can take different words for same value.
        notFindSentence = True
        valueWord = ValueWord
        totalSearching = 0   # when we look 400.000 times , we will break , we dont want to enter a loop.
        while(notFindSentence):
            randomValueWord = random.randint(1,9400)           # this place help us to produce different words with same value .
            if valueWord == nounValue[randomValueWord]:
                print(nounList[randomValueWord])
                break
            if totalSearching ==self.totalSearching:   
                print("we could not find any word for this value "+str(valueWord)+" , please try another value.")
                break
            totalSearching +=1
            
            
            
        
class generateSentencePartTwo:
    def __init__ (self,totalSearching):
        self.totalSearching=totalSearching
        
    def generateSentence(self, ValueSentence, nounValue, nounList, verbValue, verbList  ):  # this function return us =  ( noun + verb ) sentences , we can take different sentences for same value.
        notFindSentence = True
        valueSentence = ValueSentence
        totalSearching = 0    # when we look 400.000 times , we will break , we dont want to enter a loop.
        while(notFindSentence):
            randomValueVerb = random.randint(1,880)    # this place help us to produce different words with same value .
            randomValueNoun = random.randint(1,9400)
            if valueSentence == (verbValue[randomValueVerb]+nounValue[randomValueNoun]):
                print(nounList[randomValueNoun] , verbList[randomValueVerb])
                break
            if totalSearching == self.totalSearching:              # when we look self.totalSearching times , we will break , we dont want to enter a loop.
                print("we could not find any sentence for this value "+str(valueSentence)+" , please try another value.")
                break
            totalSearching +=1
            

    

class generateSentencePartThree:
    def __init__ (self,totalSearching):
        self.totalSearching=totalSearching
        
        
        
    def most_frequent(self, List):
        counter = 0
        mostFrequentString = List[0]   #most frequent string
        for i in List:
            curr_frequency = List.count(i) 
            if(curr_frequency> counter):
                counter = curr_frequency
                mostFrequentString = i
                
        while(0<counter):      # we are removing most frequent string , we want to learn the other most frequent words. 
            List.remove(mostFrequentString)
            counter -=1
        return mostFrequentString  
    
        
        
 # this function , firstly , we find most frequent words in lists and delete single word and put most frequent words in top of lists these list are ;verblistMostCommon,
         
    def generateSentence(self ,ValueSentence, nounValue, nounList, verbValue, verbList,adjList,adjValue):
        
         
         verbListBackup=verbList.copy()                                                              # verblistMostCommon, nounListMostCommon and adjListMostCommon , This method help us to increase meaning. 
         verbListMostCommon=[]                 # for example , using most common adj can meaningful almost all nouns.
         
         for i in verbListBackup:
              if i not in verbListMostCommon:
                  verbListMostCommon.append(self.most_frequent(verbListBackup))
                  
                  
         adjListBackup = adjList.copy()
         adjListMostCommon = []
         for i in adjListBackup:
             if i not in adjListMostCommon:
                 adjListMostCommon.append(self.most_frequent(adjListBackup))
         
         nounListBackup=nounList.copy()
         nounListMostCommon=[]
         for i in nounListBackup:
             if i not in nounListMostCommon:
                 nounListMostCommon.append(self.most_frequent(nounListBackup))
                 
         
         notFindSentence = True
         valueSentence = ValueSentence
         incrementer = 1
         counter = 0
         totalSearching = 0   # when we look 400.000 times , we will break , we dont want to enter a loop.
         while(notFindSentence):
             randomValueAdj = random.randint(1,2+incrementer)       # this place help us to produce different words with same value . also when we begin , we want to try most frequent words in list  
             randomValueVerb = random.randint(1,2+incrementer)      # after we dont find and words in top of lists , we increase randint sizes and look less frequent words.
             randomValueNoun = random.randint(10,(70+incrementer*6))    # this place help us to produce different words with same value .
             if valueSentence == (adjValue[adjList.index(adjListMostCommon[randomValueAdj])]  +  verbValue[verbList.index(verbListMostCommon[randomValueVerb])]  +  nounValue[nounList.index(nounListMostCommon[randomValueNoun])]):
                 print(adjList[adjList.index(adjListMostCommon[randomValueAdj])] , nounList[nounList.index(nounListMostCommon[randomValueNoun])] , verbList[verbList.index(verbListMostCommon[randomValueVerb])])
                 break
             if counter == 400:
                 if incrementer<100:                                 #this place help us for dont  exceed the list size.
                     incrementer +=1
                 counter=0
             counter +=1
             if totalSearching == self.totalSearching:       # when we look 400.000 times , we will break , we dont want to enter a loop.
                 print("we could not find any sentence for this value "+str(valueSentence)+" , please try another value.")
                 break
             totalSearching +=1
            
                
                   
                   
    
    
        






def most_frequent(List):          # we are finding here most frequent word
    counter = 0
    mostFrequentString = List[0]   #most frequent string
      
    for i in List: 
        curr_frequency = List.count(i) 
        if(curr_frequency> counter): 
            counter = curr_frequency 
            mostFrequentString = i
            
    while(0<counter):      # we are removing most frequent string , we want to learn the other most frequent words. 
        List.remove(mostFrequentString) 
        counter -=1
    return mostFrequentString     



letterValue = {'a':1 , 'b':2 , 'c':3 , 'ç':4 , 'd':5 , 'e':6 , 'f':7 ,'g':8 ,     # dictionary of letters.
              'ğ':9 , 'h':10 , 'ı':11 , 'i':12 , 'j':13 , 'k':14 , 'l':15 , 
              'm':16 , 'n':17 , 'o':18 , 'ö':19 , 'p':20 , 'r':21 , 's':22 , 
              'ş':23 , 't':24 , 'u':25 , 'ü':26 , 'v':27 , 'y':28 , 'z':28 }

nounTxt = open("Nouns.txt","r" , encoding="utf-8")         # we are reading txt files
verbTxt = open("verbs.txt","r" , encoding="utf-8")
adjTxt = open("adj.txt","r" , encoding="utf-8")


nounString=str(nounTxt.readlines())                        # we are taking words in txr files and weconverted to lower , after we split.
nounStringLower = nounString.lower()
nounList=nounStringLower.split()

verbString = str(verbTxt.readlines())
verbStringLower = verbString.lower()
verbList = verbStringLower.split()

adjString = str(adjTxt.readlines())
adjStringLower = adjString.lower()
adjList = adjStringLower.split()


 
nounValue=[]
nounCounter = -1
for word in nounList:                   # we are finding noun word value and holding in nounValueList 
    nounCounter +=1
    total=0
    values=[]
    cont = True
    for letter in word:
        if letter not in letterValue:
            cont = False
            continue
        values.append(letterValue[letter])
        total = total + letterValue [letter]
    if total == 0 :
        nounValue.append(10000)                     # if any letter not in letterValue , we add +10000 value in nounValueList ,
        continue                                    # therefore the users can not choose these type values , we have limit when we receive wordvalue , this is 735 value.
    if cont == False:
        nounValue.append(total)
        continue
        
    nounValue.append(total)


verbValue=[]        
verbCounter = -1        
for word in verbList:                  # we are finding verb word value and holding in verbValueList
    verbCounter +=1
    total=0
    values=[]
    cont = True
    for letter in word:
        if letter not in letterValue:
            cont = False
            continue
        values.append(letterValue[letter])
        total = total + letterValue [letter]
    if total == 0:
        verbValue.append(10000)
        continue
    if cont == False:
        verbValue.append(total)
        continue
    verbValue.append(total)
    



adjValue=[]
adjCounter = -1
for word in adjList:             # we are finding adj word value and holding in adjValueList
    adjCounter +=1
    total =0
    values=[]
    cont = True
    for letter in word:
        if letter not in letterValue:
            cont = False
            continue
        values.append(letterValue[letter])
        total = total + letterValue [letter]
    if total == 0:
        adjValue.append(10000)
    if cont == False:
        adjValue.append(total)
        continue
    adjValue.append(total)
    

modulOne = generateWordPartOne(900000)
modulTwo = generateSentencePartTwo(900000)
modulThree = generateSentencePartThree(400000)

while(True):                                                                             # this is user console , take an input.
    value = int(input("Please enter integer word value or sentence value : "))
    
    if value>735:                    #check value 
        print("please enter less than 734")
        continue
    if value<5:                      # check value
        print("please enter more than 5")
        continue
    
    choice=int(input("Please enter your choice, (1 is module_1), (2 is module_2), (3 is module_3), (0 is exit) : "))
    
    if choice == 0:    
        break
    elif choice == 1:        # choice area 
        modulOne.generateWord(value,nounValue,nounList)
    elif choice == 2:
        modulTwo.generateSentence(value ,nounValue, nounList, verbValue, verbList)
    elif choice == 3:
        print("this part take a little time , please wait...")
        modulThree.generateSentence(value ,nounValue, nounList, verbValue, verbList,adjList,adjValue )
    else:
        print("invalid choice , please enter again")
        



