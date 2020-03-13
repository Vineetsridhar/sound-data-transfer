#Decoder

'''Creates the dictionary'''
inF = open("dict.txt", 'r')
d = {}
d.setdefault(' ' , '00000')
for line in inF:
    line = line.split()
    d[line[0]] = line[1]
inF.close()

'''alphabet to binary'''
def binary(dict, input):
    builder = '';
    for char in input.lower():
        #print(char)
        for key in dict:
            if(char == key):
                builder += dict.get(key)
    return builder
       
'''binary to alphabet'''       
def alpha(dict, input):
    builder = ''
    
    #Parses incoming code by 5bits
    parse = [(input[i:i+5]) for i in range(0, len(input), 5)]
    for par in parse:
        #print(par)
        for key in dict:
            if (par == dict.get(key)):
                builder += key
    return builder    

#Test for both functions
'''
def check(input):
    try:
        y = int(input)
        val = alpha(d, input)
        return val
    except ValueError:
        val = binary(d, input)
        return val
'''