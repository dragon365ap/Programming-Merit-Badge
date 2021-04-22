#Run this program in https://trinket.io/python/f7ad7f9864
#This program takes some text and a key to shift the text by. For example, if you put the letter h, and the key 3. The program would shift the letter h up 3 spaces, i, j, k. The out put should be k.

#declare variables
text = input("Input text: ")
key = input("Input key: ")
ascii = 0
encodedText = ""
##loop going though each character for text
for i in range(len(text)):
#check if letter
    if (text[i].isalpha()) == True: 
#check if lowercase
      if (text[i].islower()) == True:
#shift letter by key
        ascii = (int(ord(text[i]))-97+int(key))%26
        encodedText = (str(encodedText) + chr(ascii+97))
#if not lowercase than must be uppercase
      else:
#shift letter by key
        ascii = (int(ord(text[i]))-65+int(key))%26
        encodedText = (str(encodedText) + chr(ascii+65))
    else:
      encodedText = encodedText + text[i]
#print encrypted result
print(encodedText)
