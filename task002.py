# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
f = open('first.txt', 'r')
my_string = ''
for line in f:
    my_string = my_string + line
f.close

f = open('second.txt', 'r')
my_string_2 = ''
for line in f:
    my_string_2 = my_string_2 + line
f.close

def perpetuate_polynomya (received_string):
    received_string = received_string.replace(' ','').replace('=0','')\
    .replace('+',' ').replace('-', ' -')
    received_string = received_string.split()
    my_dictionary = {}
    for item in received_string :
        if item == item.replace('x',''):
            my_dictionary[0] = item
        else:
            item = item.replace('*','').replace('x',' ').split()
            if len(item) == 1:
                my_dictionary[1] = item[0]
            else:
                my_dictionary[item[1]] = item[0]
    return my_dictionary

def split_dictionary (dictonary2, dictonary1):
    dictonary_end = dictonary1
    for item in dictonary2.keys():
        if dictonary1.setdefault(item) == None:
            dictonary_end[item] = int(dictonary2[item])
        else:
            dictonary_end[item] = int(dictonary2[item]) + int(dictonary1[item])
    return dictonary_end
    
def summa_polynomya(dictonary_end):
    end_string = ''
    for item in dictonary_end.keys():
        if int(item)>1:
            if dictonary_end[item]>0:
                end_string +=  '+' + str(dictonary_end[item]) + '*x**'+ item
            else:
                end_string +=   str(dictonary_end[item]) + '*x**'+ item
        elif int(item)==1:
            if dictonary_end[item]>0:
                end_string +=  '+' + str(dictonary_end[item]) + '*x'
            else:
                end_string +=  str(dictonary_end[item]) + '*x'
        else:
            if dictonary_end[item]>0:
                end_string +=  '+' + str(dictonary_end[item])
            else:
                end_string +=str(dictonary_end[item])
    end_string += '=0'
    return end_string


dictonary_1 = perpetuate_polynomya (my_string)
dictonary_2 =perpetuate_polynomya (my_string_2)
dictonary_end = split_dictionary (dictonary_2, dictonary_1)
end_string =  summa_polynomya(dictonary_end)

print(end_string)

f = open('end.txt', 'w')
f.write(end_string)
f.close
  