import sys
import os

characters = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9,
                  "J":10, "K":11, "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17,
                  "R":18, "S":19, "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25,
                  "Z":26, " ":27,1:"A", 2:"B", 3:"C", 4:"D", 5:"E", 6:"F", 7:"G",
                  8:"H", 9:"I", 10:"J", 11:"K", 12:"L", 13:"M", 14:"N", 15:"O",
                  16:"P", 17:"Q", 18:"R", 19:"S", 20:"T",21:"U", 22:"V", 23:"W",
                  24:"X", 25:"Y", 26:"Z", 27:" "}


try:
    assert len(sys.argv) == 5
    
except:
    print("Parameter number error")
    exit()


codetype = (sys.argv[1])
try:
    assert codetype == "enc" or codetype == "dec"

except:
    print("Undefined parameter error")
    exit()
    
    
try:
    assert sys.argv[3].endswith(".txt")
        
except:
    print("The input file could not be read error")
    exit()
    
    
try:
    assert sys.argv[2].endswith(".txt")
        
except:
    print("Key file could not be read error")
    exit()
    
    
try:
    z = open(sys.argv[2])
    z.close
    
except:
    print("Key file not found error")
    exit()


try:
    z = open(sys.argv[3])
    z.close
    
except:
    print("Input file not found error")
    exit()
    
        
try:
    z = open(sys.argv[3],"r")
    assert len(z.readline()) != 0
    z.close()
except:
    print("Input file is empty error")
    exit()
    
    
try:
    z = open(sys.argv[2],"r")
    assert len(z.readline()) != 0
    z.close()
except:
    print("Key file is empty error")
    exit()
    
    
try:
    m = "0123456789-1-2-3-4-5-6-7-8-9"
    z = open(sys.argv[2],"r")
    k = [(line.strip()) for line in z]
    k = [("".join(i)).split(",") for i in k]
    for i in range(len(k)):
        for j in range(len(k[0])):
            assert (k[i][j]) in m
except:
    print("Invalid character in key file error")
    exit()


if "plain_input.txt" in sys.argv[3]:
    
    try:
        z = open(sys.argv[3],"r")
        k = z.readline()
        m = ""
        for i in range(len(k)):
            m += (k[i].upper())
            assert m[i] in characters
        m = ""
        
    except:
        print("Invalid character in input file error")
        exit()
        
elif "ciphertext.txt" in sys.argv[3]:
    
    try:
        z = open(sys.argv[3],"r")
        k = z.readline()
        k = k.split(",")
        characters_c = characters.copy()
        for i in range(len(k)):
            assert int(k[i])
    except:
        print("Invalid character in input file error")
        exit()


key = open(sys.argv[2],"r")

list_of_key = [(line.strip()).split() for line in key]
list_of_key = [("".join(i)).split(",") for i in list_of_key]
for i in range(len(list_of_key)):
    for j in range(len(list_of_key[0])):
        list_of_key[i][j] = int(list_of_key[i][j])

def coding(x,y):
    for m in range(len(x)):
        result = [[0] for i in range(len(list_of_key))]
        matrix2 = []
        if (m+1) % len(y) == 0:
            for k in range(len(y)):
                matrix2.insert(k,[x[m-(len(y)-1-k)]])
            for i in range(len(y)):
                for j in range(len(matrix2[0])):
                    for k in range(len(matrix2)):
                        result[i][j] += int(y[i][k]) * matrix2[k][j]
                    list_of_result.append(result[i][j])
            result = [[0] for i in range(len(list_of_key))]

if codetype == "enc":
   
    plain_input = open(sys.argv[3],"r")
    output_enc = open(sys.argv[4],"w")
    
    list_of_plain_input = [line.strip() for line in plain_input]
    number_of_plain = []

    for i in list_of_plain_input :
        i = i.upper()
        i = list(i)
        number_of_plain = [characters[j] for j in i]
        
    list_of_result = []
    while len(number_of_plain) % len(list_of_key) != 0:
        number_of_plain.append(27)
    
    coding(number_of_plain,list_of_key)         

    text_of_result = ""
    for i in list_of_result:
        text_of_result += str(i)
        text_of_result += ","
    text_of_result = text_of_result[:-1]
    output_enc.write(text_of_result)
    output_enc.close()


if codetype == "dec":
    
    ciphertext = open(sys.argv[3],"r")
    output_dec = open(sys.argv[4],"w")
    list_of_ciphertext = [line.strip() for line in ciphertext]
    list_of_ciphertext = [("".join(i)).split(",") for i in list_of_ciphertext]

    for i in range(len(list_of_ciphertext)):
        for j in range(len(list_of_ciphertext[0])):
            list_of_ciphertext.append(int(list_of_ciphertext[i][j]))
        list_of_ciphertext.pop(0)
        

    if len(list_of_key) == 2:
        list_of_key_inv = [b.copy() for b in list_of_key]
        determinant = 1/((list_of_key[0][0]*list_of_key[1][1])-(list_of_key[0][1]*list_of_key[1][0]))
        list_of_key_inv[0][0] = int(list_of_key[1][1]/determinant)
        list_of_key_inv[0][1] = int(-1*list_of_key[0][1]/determinant)
        list_of_key_inv[1][0] = int(-1*list_of_key[1][0]/determinant)
        list_of_key_inv[1][1] = int(list_of_key[0][0]/determinant)
        
        
    if len(list_of_key) == 3:
        matrix_of_minors = [[0,0,0], [0,0,0], [0,0,0]]

        matrix_of_minors[0][0] = (list_of_key[1][1]*list_of_key[2][2])-(list_of_key[1][2]*list_of_key[2][1])
        matrix_of_minors[0][1] = (list_of_key[1][0]*list_of_key[2][2])-(list_of_key[1][2]*list_of_key[2][0])
        matrix_of_minors[0][2] = (list_of_key[1][0]*list_of_key[2][1])-(list_of_key[1][1]*list_of_key[2][0])
        matrix_of_minors[1][0] = (list_of_key[0][1]*list_of_key[2][2])-(list_of_key[0][2]*list_of_key[2][1])
        matrix_of_minors[1][1] = (list_of_key[0][0]*list_of_key[2][2])-(list_of_key[0][2]*list_of_key[2][0])
        matrix_of_minors[1][2] = (list_of_key[0][0]*list_of_key[2][1])-(list_of_key[0][1]*list_of_key[2][0])
        matrix_of_minors[2][0] = (list_of_key[0][1]*list_of_key[1][2])-(list_of_key[1][1]*list_of_key[0][2])
        matrix_of_minors[2][1] = (list_of_key[0][0]*list_of_key[1][2])-(list_of_key[1][0]*list_of_key[0][2])
        matrix_of_minors[2][2] = (list_of_key[0][0]*list_of_key[1][1])-(list_of_key[0][1]*list_of_key[1][0])
        matrix_of_minors[0][1] = -matrix_of_minors[0][1]
        matrix_of_minors[1][0] = -matrix_of_minors[1][0]
        matrix_of_minors[1][2] = -matrix_of_minors[1][2]
        matrix_of_minors[2][1] = -matrix_of_minors[2][1]

        matrix_of_adjugate = [[0,0,0], [0,0,0], [0,0,0]]

        for i in range(len(matrix_of_adjugate)):
            for j in range(len(matrix_of_adjugate[0])):
                matrix_of_adjugate[i][j] = matrix_of_minors[j][i]

        determinant = (list_of_key[0][0]*matrix_of_minors[0][0])+(list_of_key[0][1]*matrix_of_minors[0][1])+(list_of_key[0][2]*matrix_of_minors[0][2])

        list_of_key_inv = [[0,0,0], [0,0,0], [0,0,0]]
        for i in range(len(matrix_of_adjugate)):
            for j in range(len(matrix_of_adjugate[0])):
                list_of_key_inv[i][j] = int(matrix_of_adjugate[i][j]/determinant)

    list_of_result = []
    coding(list_of_ciphertext,list_of_key_inv)
        
    list_of_text = [characters[i] for i in list_of_result]
    text = "".join(list_of_text)
    output_dec.write(text)
    output_dec.close()

