# Type Quiz
Try guessing what is the type of the expression in the last row of each code snippet. Write the letter of your answer after the colon.

There is no common state, so one variable declared in a snippet, does not affect other snippets

## 1

    a = 42
    a

- A: Boolean
- B: Error
- C: Float
- D: Integer
- E: String

Answer: 

## 2

    a = 3.1415926535
    a

- A: Boolean
- B: Error
- C: Float
- D: Integer
- E: String

Answer: 

## 3

    a = "TANSTAAFL"
    a

- A: Boolean
- B: Error
- C: Float
- D: Integer
- E: String

Answer: 

## 4

    a = False
    a

- A: Boolean
- B: Error
- C: Float
- D: Integer
- E: String

Answer: 

## 5

    a = 420 == 420.0
    a

- A: Boolean
- B: Error
- C: Float
- D: Integer
- E: String

Answer: 

## 6

    a = 12 - 7.0
    a

- A: Boolean
- B: Error
- C: Float
- D: Integer
- E: String

Answer: 

## 7

    a = "FUBAR" * 50
    a

- A: Boolean
- B: Error
- C: Float
- D: Integer
- E: String

Answer: 

## 8

    a = "Hari Seldon" / 1.0
    a

- A: Boolean
- B: Error
- C: Float
- D: Integer
- E: String

Answer: 

## 9

    a = False - True 
    a

- A: Boolean
- B: Error
- C: Float
- D: Integer
- E: String

Answer: 

## 10

    a = True > "0"
    a

- A: Boolean
- B: Error
- C: Float
- D: Integer
- E: String

Answer: 

## 11

    a = 23
    b = 2
    c = a / b
    c

- A: Boolean
- B: Error
- C: Float
- D: Integer
- E: String

Answer: 

## 12

    a = "5"
    b = 2
    c = a * b
    c

- A: Boolean
- B: Error
- C: Float
- D: Integer
- E: String

Answer: 

## 13

    a = True
    b = False
    c = a + b
    c

- A: Boolean
- B: Error
- C: Float
- D: Integer
- E: String

Answer: 

## 14

    a = True
    b = 4
    c = a + b
    c

- A: Boolean
- B: Error
- C: Float
- D: Integer
- E: String

Answer: 

## 15

    a = "asd"
    b = 4
    c = a * b == "string"
    c

- A: Boolean
- B: Error
- C: Float
- D: Integer
- E: String

Answer: 

## 16

    a = 5
    b = c + 3
    c = a * b
    c

- A: Boolean
- B: Error
- C: Float
- D: Integer
- E: String

Answer: 

## 17

    a = 'négy' < 'öt'
    a

- A: Boolean
- B: Error
- C: Float
- D: Integer
- E: String

Answer: 

## 18

    a = (False and True) or True
    a

- A: Boolean
- B: Error
- C: Float
- D: Integer
- E: String

Answer: 

## 19

    a = False and True
    b = 3 / a
    a

- A: Boolean
- B: Error
- C: Float
- D: Integer
- E: String

Answer: 

## 20

    a = False or True
    b = 3 / a
    b

- A: Boolean
- B: Error
- C: Float
- D: Integer
- E: String

Answer: 

## 21

    a = 'három' < 'kettő'
    b = 'kettő' < 'három'
    c = a + b
    c

- A: Boolean
- B: Error
- C: Float
- D: Integer
- E: String

Answer: 

## 22

    a = 'gizi'
    b == 1
    c = a * b
    c

- A: Boolean
- B: Error
- C: Float
- D: Integer
- E: String

Answer: 

## 23

    a = 3.4
    b = a > 1
    c = a * b
    c

- A: Boolean
- B: Error
- C: Float
- D: Integer
- E: String

Answer: 

## 24

    s = ''
    for b in 'turing gép':
        
        s = s + b
    s

- A: Boolean
- B: Error
- C: Float
- D: Integer
- E: String

Answer: 

## 25

    l = ['kecske', 3, 567.021, False]
    x = None
    for elem in l:
        
        x = elem     
    x

- A: Boolean
- B: Error
- C: Float
- D: Integer
- E: String

Answer: 

## 26

    def fun(x):
        if x < 10:
            return str(x) #A beépített str függvény stringé alakítja a bemeneti paraméterét.
        else:
            return x / 2     
    fun(3)

- A: List
- B: Error
- C: Float
- D: Integer
- E: String

Answer: 

## 27

    def func(y, z):   
        if y < z:
            return z - y
        else:
            return y   
    func('négy', 'öt')

- A: List
- B: Error
- C: Float
- D: Integer
- E: String

Answer: 

## 28

    k = 0
    while k:    
        k = k + 0.3   
        if k > 100:
            break #A break megszakítja az iteráció futását.        
    k

- A: List
- B: Error
- C: Float
- D: Integer
- E: String

Answer: 

## 29

    l = ["r","a","j","k",5,0]
    o = ""
    #A beépített len függvény egy iterálható objektum elemeinek számát adja visszatérési értékként.
    #Pl. lista elemeinek száma
    for i in range(len(l)):     
        o += str(l[i])
    o

- A: List
- B: Error
- C: Float
- D: Integer
- E: String

Answer: 

## 30

    v = ([1,2,3,4],     [2,3,4,5],     [3,4,5,6],     [4,5,6,7])
    v[3]

- A: List
- B: Error
- C: Float
- D: Integer
- E: String

Answer: 

## 31

    i = [True,False]
    i = i*4
    i = [i]*4
    i[i[i]]

- A: List
- B: Error
- C: Float
- D: Integer
- E: String

Answer: 

## 32

    def cosmere(mist):
        if mist:
            return 10
        else:
            return mist
    mist = (10 < 15) and (3 > 1)
    cosmere(mist or b)

- A: NoneType
- B: Error
- C: Float
- D: Integer
- E: String

Answer: 

## 33

    gemmell = 1948
    legend, saga= ["druss", "drenai"] #Több változó deklarálását és értékadását így lehet egy sorba összevonni.
    trusag = ""
    for year in range(2020 - 1948):
        for betu in saga:
            for megegy_betu in legend:
                if betu == megegy_betu and len(trusag) <= year * 30:
                    trusag += betu * year 
    if len(trusag) > 4000:
        megoldas = "rák"
    elif len(trusag) > 3000:
        megoldas = 1
    elif len(trusag) > 2000:
        megoldas = 30/30
    elif len(trusag) > 1000:
        megoldas = ["chronicles", "rigante", "waylander"]  
    megoldas

- A: NoneType
- B: Error
- C: Float
- D: Integer
- E: String

Answer: 

## 34

    def ir():
        match = 0
        for k in "skywards":
            for b in "starsight": 
                if k == b:
                    match += 1
    ir()

- A: NoneType
- B: Error
- C: Float
- D: Integer
- E: String

Answer: 

## 35

    volume = 0
    wheel = "abcdefghijklmno"
    of = 0
    for of in range(len(wheel)):
        time = of ** 3
        if time >= 1: 
            volume = volume + 1     
        else:
            volume += 0.5    
    volume

- A: NoneType
- B: Error
- C: Float
- D: Integer
- E: String

Answer: 

## 36

    epics = True
    calamity, firefight, steelheart = [1, 2, 3]
    if epics and firefight ** 2 * steelhear ** 2 == 14 - calamity:
        epics = "chicago"
    if epics != 1:
        epics = steelheart + 0.14
    if epics > firefight ** 0.5 :
        epics = steelheart    
    megoldas

- A: NoneType
- B: Error
- C: Float
- D: Integer
- E: String

Answer: 

## END