#!/usr/bin/env python
# coding: utf-8
#Importing datetime module for calculating time taken for finding words
import datetime
import time


def check(lis_word):
    index = 0
    while(True):
        character = input() #Taking character from user

        if(character == '#'):
            print('Exiting') #if input is '#' then exit
            break

        start_time = datetime.datetime.now() #keeping track of start time

        character = character.lower()
        #Segregating only those words where the character at current index of the word matches the input
        lis_word = [x for x in lis_word if x[2]>index and x[0][index].lower() == character]  

        end_time = datetime.datetime.now() #Time at which the calculation ends

        tot_time = end_time - start_time #Total time taken

        #if no words matches the criteria then exit
        if(lis_word == []):
            print('No match Found!!','\t',str(tot_time.microseconds)+' \u03bcs')
            print('Exiting')
            break
        
        #Printing the words     
        for i in range(min(5, len(lis_word))):
            print(lis_word[i][0], end = ',')
        print('\t',str(tot_time.microseconds)+' \u03bcs')
        index += 1
    time.sleep(2)

        

def main():
    

    #opening file
    file = open('../source/EnglishDictionary.txt','r')

    #creating empty dictionary for storing words and their respective frequencies
    dict_words = {}
    for line in file:
        word, frequency = line.split(',') #splitting lines in words and frequency
        frequency = int(frequency)
        dict_words[word] = frequency 

    lis_word = [[x, -1*dict_words[x], len(x)] for x in dict_words.keys()] #creating a list of words, their frequencies in negative and length of words
    
    lis_word.sort(key = lambda x: x[1]) #Sorting list according to negative frequencies
    
    check(lis_word) #Calling function to check for each input
    
        

if __name__ == "__main__":
    main()



