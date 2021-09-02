n= 5232 # Say the limit is thousand
#write the above as a string 
dictionary_one = {
    #1000000000: 'one billion',
    #100000000: 'hundred million',
    #10000000: 'ten million',
    #1000000 : 'one million',
    #100000 : 'hundred thousand',
    10000: 'ten thousand',
    1000: 'thousand',
    100: 'hundred',
    10: 'ten',
    1: 'ones'
}
dictionary_two = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four',
    5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
    9: 'nine', 10: 'ten'
    }

dictionary_three = {1: 'teen', 2: 'twenty', 3: 'thirty', 4 :'fourty', 5: 'fifty',
6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'} 

# To Do 
# 1) Teens 2) > than thousand

value = []
reminder = []
removeReminder =[] 

for key in dictionary_one:
    value.append(key)

for i in range(len(value)):
    reminder.append(n%value[i])

r = len(reminder) - 1
while r <= len(reminder) and r > 0 :
    removeReminder.append(reminder[r-1] - reminder[r])
    r-=1
print(removeReminder)
    

j= len(removeReminder) - 1
k=1
u=1
power = 0
unitsPlace = ''
unitsPlaceString =''
numLength = len(str(n))


while j in range(len(removeReminder)):
    while k in dictionary_one:
        if (len(str(removeReminder[j])) == len(str(k))):
            unitsPlace = int(removeReminder[j] / k)
            if unitsPlace != '' :
                for u in dictionary_two:
                    if (unitsPlace == u):
                        unitsPlaceString = dictionary_two[u]
                        if (dictionary_one[k] == 'ones'):
                            dictionary_one[k] = ''
                        if (dictionary_one[k] == 'ten' and unitsPlace != ''):
                            for t in dictionary_three:
                                if (unitsPlace == t):
                                    dictionary_one[k] = ''
                                    unitsPlaceString = dictionary_three[t]
                        print(unitsPlaceString + '' + dictionary_one[k])
                        break
        k = pow(10,power)
        power+=1
    j-=1
    k=1
    power = 0
