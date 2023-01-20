############## COMENTARII ##################

# acesta este un comentariu
# acesta este un alt comentariu

"""
acesta
este un
comentariu pe mai multe
linii
"""

######### Functia print() #############
# syntax: print(something)
# functia print afiseaza ceva in consola

print("Hello world")
print('Hello world')
print("lalalla")

# print something with with new line. the chaacter we use is "\n"
print("Hello world/nI am Marcus")  # -> it will print:
# Hello World
# I am Marcus

############## Variabile si tipuri de date ###############
a = 5  # int
b = 6  # int
c = 20  # int
d = "mama"  # string
imi_place_zaharul = True  # bool
i_have_hope = False
pret = 125.50
ENVIRONMENT = "MacOS"  # constanta

# variabile tip string
culoare = "verde"
nume = "Ion"
varsta = "25"
print(varsta)
print(culoare)
print(nume)

############# Functia type()############
# syntaxa: type(argument)
# afiseaza tipul unei variabile

name = "Marina"
price = 35.99
age = 20
hate_mangos = True

print(type(name))
print(type(hate_mangos))
print(type(price))
print(type(age))

############### type casting ###############
# we use for casting the following: int(), float(), str(), bool()
# syntax cast_func(variabila)

s = 25  # int
s = str(s)  # convertim variabila s in string
print("s After conversion:")
print(type(s))

n = 27
n = 50  # override
print(n)
print(type(str(85)))
c = 20
c = str(c)  # override

############ print cu formatare si concatenare ##############
# are syntaxa print(f"something{var}")

fructe = "mere, pere, gutui"
legume = "morcovi, telina"
concat_string = fructe + " " + legume
print(concat_string)
print(fructe + " " + legume)
pret = 10
print(fructe + " " + legume + " la " + str(pret) + " lei")

# print cu formatare
print(f"Azi am cumparat {fructe}, {legume}, toate la {pret} lei")

name = "Maria"
parent = "mama"
age = 46

# mama mea este Maria si are 46 de ani


print(f"{parent} mea este {name} si are {age} de ani")

#### assert ####
invat_Python_acum = False
assert invat_Python_acum == True, "Trebuia sa fiu la curs, dar nu sunt"
print("Sunt la curs")

imi_place_prajitura = True
assert imi_place_prajitura == False, "doar unele prajituri"
print("cele de casa")

nu_mi_place_sa_zbor = True
assert nu_mi_place_sa_zbor == True, "merg in Cipru"
print("merg cu masina")

############ functia input() ###########

name = input("Introduceti numele de familie: ")
surname = input("Introduceti prenumele: ")
print(f"Numele meu este {name} {surname}")

# type casting - int -ex 1
number = input("Introduceti un numar intreg: ")
print(type(int(number)))

# type casting - int - ex 2
number2 = int(input("Introduceti un numar intreg: "))

############## metode string #############

myString = "Astazi am invatat multe la python"
myString2 = "mere"

# printam lungimea stringului
print(len(myString2))
print(len(myString))

string3 = "diamant"
# d i a m a n t e l e
# 0 1 2 3 4 5 6 7 8 9

# vrem sa obtinem dia
new_str = string3[:3]
print(new_str)

# vrem sa obtinem ant
new_str2 = string3[4:]
print(new_str2)

# vrem sa obtinemant
new_str3 = string3[4:7]
print(new_str3)

####### String Methods #######

### .capitalize()####
# modifica stringul astfel incat prima litera va fi mai mare si restul literelor vor fi mici
myStr = "casa mea este miCa"
print(myStr.capitalize())

### .endswith() ####
# verifica daca un string se termina cu litera data ca argument
# syntax: nume_str.endswith("something")
a = "my name is Diana"
print(a.endswith("is Diana"))

#### .find() ####
# cauta un substring si returneaza indexul unde se gaseste
# nu returneaza o eraoare daca ii dam un substring inexistent
# functioneaza numai cu stringuri
# syntax: nume_str.find("substring")

# find with one parameter
action = "Today I will learn python"
print(action.find("arn"))

# find with 2 parameters
# if you want to search the substring staring with a certain index
# syntax: nume_str("substring", poz)
dislike = "I don't wanna learn anything today"
print(dislike.find("anything", 21))

#### find with 3 parameters
# al treilea argument pointeaza catre indexul unde vrem sa terminam cautarea
# syntax: nume_string("substring", start_poz, end_poz)
love = "castane"
########0123456
print("Substringul 's' se gaseste pe pozitia:", love.find("s", 1, 3))

#### .isalnum() #####
# verifica daca un string contine numai litere si cifre. Returneaza un bool --> True/False
mother = "Cristina10"
father = "Ioan Ciubotaru"
print("mother: ", mother.isalnum())
print("father: ", father.isalnum())

#### .isalpha() #####
# verifica daca un string este format numai din litere si returneaza True/False
# syntax: nume_str.isaplha()
# spatiile nu sunt considerate litere, sunt considerate caractere

a_str = "Am pescarusi"
b_str = "elefant"
print("a_str: ", a_str.isalpha())
print("b_str", b_str.isalpha())

#### isdigit() ####
# verifica daca un string este format numai din numere
# syntax: nume_str.isdigit()
age = "2"
age2 = "mama5444"

print("age ", age.isdigit())
print("age2", age2.isdigit())
print(age.isnumeric())

###### islower() #####
# verifica daca un string este format numai din litere mici si returneaza True/False
# syntax: nume_str.islower()
small_letter = "am plecat in vacanta"
print("small_letter", small_letter.islower())

#### .isspace() ####
# verifica daca stringul este format numai din spatii goale si returneaza True/False
# syntax nume_str.isspace()
spatiu = "am plecat"
spatiu2 = "    "
print("spatiu", spatiu.isspace())
print("spatiu2", spatiu2.isspace())

#### .isupper() ####
# verifica daca un string este format numai din litere mari si returneaza True/False
# syntax: nume_str.isupper()
mama = "CASA"
print("mama", mama.isupper())

###### .lower() ####
# inlocuieste toate literele mari din string cu litere mici
# syntx: str.lower()
mama = "CASA"
print("mama", mama.lower())

#### .upper() ####
# inlocuieste toate literele mici ale stringului cu litere mari
# syntax: nume_str.upper()
home = "here"
print("home", home.upper())

##### replace()####
# returneaza o copie a stringului original in care toate aparitiile primului argument au fost inlocuite cu al doilea argument
# syntax: nume_str.replace(string_to_replace, replace)
action2 = "cainele meu e mic si rau si ma musca"
print(action2.replace("cainele", home.upper()))

# ex
s = "It is either easy or impossible"
s = s.replace('easy', 'hard')
print(s)

s = "It is either easy or impossible"
s = s.replace('i', 'n')
print(s)

#### .strip() ###
# returneaza un string fara leading space
# syntax: str.strip()
n = "mama are"
l = "  mama are"
print(n)
print(n.strip())
print(l)
print(l.strip())

### split() ####
# aceasta metoda considera ca stringurile sunt delimitate de spatii albe
# syntax: str.split()
ex = "bujori trandafiri crini"
print(ex.split())

### exercitiu
# myvar  = input("Introduceti 4 cuvinte separate prin spatiu: ") # ana are multe mere
# x, y, z, w = myvar.split()
# print(x)
# print(y)
# print(z)
# print(w)

##### swapcase() ####
# returneaza un nou string in care tipul de litere este inversat. litere mici --> litere mari, viceversa
s = "i WaS a BAD cat"
print(s.swapcase())

####### LISTE #######

# Lista goala
myList = []
print(myList)

# Lista cu elemente mixte

lst = ["mama", 13, True, 13.5, True, False, "miau"]
print(lst)

# de cate ori apare True in lista
print(lst.count(True))

# aflam elementul de pe pozitia 2
print(lst[2])

##### append ###
ls1 = [1, 2, 3, 4]
ls2 = ['n', 'm', 0, True]
# adaugam lista 2 la lista 1

ls1.append(ls2)
print(ls1)

# copiem un elementul de pe poz 1 din lista 2
# adaugam la lista 1
elem = ls2[1]
print(elem)
ls2.remove(elem)
print(ls2)
ls1.append(elem)

print("Lungimea listei ls 2 este ", len(ls1))
print(ls1)

## extend
print("Lista 1 este: ", ls1)
print("Lista 1 este: ", ls2)
ls1.extend(ls2)
print("Noua ls1 este: ", ls1)
print("Lungimea ls1 este: ", len(ls1))

# inlocuim un element din lista
ls1[4] = "new_val"
print("LS1 = ", ls1)

###### tuple ###

# cream o tupla cu string-uri
myT = ("unu", "doi", "trei")
print(type(myT))

# vrem sa aflam elementul de pe pozitia 0
print("Elementul de pe pozitia 0 din tupla myT: ", myT[0])

# verificam daca elementul "trei" este in tupla
print("trei" in myT)

# vrem sa inlocuim elementul de pe pozitia 1
# myT[1] = 7

# avem o lista. sa se afle elementul de pe pozitia 1.
# sa se inlocuiasca elementul de pe pozitia 1 cu "bingo".
# daca elementul de pe pozitia 1(vechi) este in lista, atunci vom afisa "I am here",
# daca nu se afla in lista, afisam "We got rid of it"

lista = ["oua", "zahar", 7]
print(lista[1])
elem = lista[1]
lista[1] = "bingo"
print(lista)

if elem in lista:
    print("I am here")
else:
    print("I got rid of it")

### tupla def2
a = 1, 2, 3, 4, 5
print(type(a))

###### seturi #####

myset = {"iarna", "primavara", "vara", "toamna"}

# afisam lungimea setului
print(len(myset))

# add elements to the set

myset.add("frig")
myset.add("cald")
myset.add(("elem1", "elem2"))
print("Setul are urm valori: ", myset)

# remove element tupla
myset.remove(("elem1", "elem2"))
print("Myset: ", myset)
# remove an element that doesn't exist
# myset.remove("calda")

### discard

myset.discard("frig")
print(" ////////////", myset)
myset.discard("noapte")

# asignam o alta valoare elementului de pe poz 0 --> nu se poate
myset[0] = "True"

######## dictionare #####

dict1 = {"a": 2, "b": 3, "c": 5}

# afisam vaoarea lui b
print("Val cheii b: ", dict1["b"])

dt = {"tip_carte": "roman", "editura": "Corint",
      "Autor": "Agatha Christie", "nr_pg": 250,
      "carti": ["Cu cartile pe fata", "Oglinda", "Crima din Orien Expres"]}

# din cheia carti vrem sa obtinem a doua carte
print(dt["carti"][1])

######### avem lista in lista, cum accesam valorile din lista care este in lista

a = [1, 2, "sapte", [3, 6, 0]]
print(a[3][0])

import time

############ while ########
### endless loop
# endless loop happens when the condition is always true and the loop body doesn't modify the condition
# ex 1

# while True:
#     print("I am stuck inside a loop")

# ex2

while True:
    print("I am stuck here, Help!")
else:
    print("something")

# ex3
# write a program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd
# the program terminates when zero is entered

# What we need?
# var - odd numbers
# var - even numbers

# read the number first
odd_numbers = 0
even_numbers = 0
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates the execution
while number != 0:
    # check if the number is even
    if number % 2 == 0:
        even_numbers += 1
    else:
        # increase the odd numbers
        odd_numbers += 1
    number = int(input("Enter a number or type 0 to stop: "))

print("Too bad, user entered 0!")
print("Odd numbers count: ", odd_numbers)
print("Even numbers count: ", even_numbers)

#### ex 4
# make a counter that counts the last 10 seconds until new year
# after the last second, print "Happy new year!"

# De ce avem nevoie?
# o variabila counter

counter = 10
while counter != 0:
    print(counter, "seconds left")
    # se scade o secunda
    counter -= 1
    time.sleep(1)
print("Happy new year!!!!", counter)

########### for ##############
# ex 1
# write a for loop that counts to five
# body of the loop - print the loop iteration number and the word "Mississippi"
# use time.sleep(1)
# write a print function with the final message

for second in range(1, 6):
    print(second, "Mississippi")
    time.sleep(1)
print("I will search you and I'll find you!")

## ex 2
# Define a new list with 7 elements
# We want to calculate the sum of all numbers inside the list

# Ce avem nevoie?
# o lista, o var sum
# my_list = [2, 10, 15, 15, 3, 5, 20]
# sum = 0 # we start with a counter that we initialize with 0 (we haven't added any number yet)

for i in my_list:
    print(f"Adding {i} to {sum}")
    sum += i  # as long as we haven't reached the end of the list we will add the current elem to the previous total
    print(f"Current sum is {sum}")
else:
    print("We are done with the sum")

print(f"The sum of the elements in the list is: {sum}")

##### break ####
print("The break instruction ")
for i in range(3, 8):
    if i == 4:
        break
    print("Inside the loop ", i)
print("Outside the loop")

###### continue ######
print("The continue instruction ")
for i in range(3, 8):
    if i == 4:
        continue
    print("Inside the loop ", i)
print("Outside the loop")

### for each ####
#
# avem o lista cu 6 animale
# parcurgem lista cu cele 6 animale si printam "I love this animal"

animals = ["zebra", "tigru", "maimuta", "iepure", "pantera", "panda"]

for animal in animals[::-1]:
    print(f"I love this animal --> {animal}")

############# temaaaaaaaaa #### incercati si pe alte structuri de date

# a junior magician has picked a secret number
# he has hide it in a variable named secret_number
# he wants everyone to run his program to play Guess the secret number
# if the user doesn't guess the number, he will be stuck in the loop
# if he guessed the number, then the magician will let him out

secret_number = 23

print("======= Welcome to my game silly human! =========")
user_nr = int(input("Enter a number between 0 and 30: "))

while user_nr != secret_number:
    print("You are stuck in my loop, ha ha ha, you are mine forever!!!")
    user_nr = int(input("Enter the number again: "))
print(secret_number, "Well done human! You are unfortunately free now!")

#### Turn this snipet into a function
#
print("Enter a value: ")
a = int(input())

print("Enter a value: ")
b = int(input())

print("Enter a value: ")
c = int(input())


### define the function

def get_value():
    print("Enter a value: ")


print("We start here")
get_value()
print("We end here")


####### positional parameter passing

def introduction(first_name, last_name):
    print("Hello, my name is ", first_name, last_name)


# apelam functia
introduction("Luke", "Skywalker")
introduction("Clark", "Kent")
introduction("Jessie", "J")

introduction(first_name="James", last_name="Bond")
introduction(last_name="Cat", first_name="Woman")


### functie cu parametru predefinit
def introduction_a(first_name, last_name="Smith"):
    print("Hello, my name is", first_name, last_name)


introduction_a("Diana")
introduction_a("Laura", "Noris")


#### return fara argumente ####
# happy new year whishes

def happy_new_year(whishes=True):
    print("Three...")
    print("Two...")
    print("One...")
    if not whishes:
        return
    print("Happy new year")


# apelam functia cu whishes True
happy_new_year()

# apelam functia cu whishes False
happy_new_year(False)
print("I am here!!!!!")


#### functie cu un argument gresit


def introduction_b(first_name, last_name):
    print("Hello, my name is ", first_name, last_name)


introduction_b("Luke")


#### functie cu mai multe argumente decat parametrii

def introduction_c(first_name, last_name):
    print("Hello, my name is ", first_name, last_name)


introduction_c("Luke", "Mina", "Dungeon")


#### return cu argumente - used

def boring_function():
    a = 345
    return a


x = boring_function()
print("The boring_function has returned its results. It's: ", x)


### retrun - we will not use what it returns


def boring_function_a():
    print("'Boredom Mode' ON.")
    return 123


print("This is quite interesting!")
a = boring_function_a() + 342
print(a)
print("This lesson is boring ...")
print(boring_function_a() + 243)


#### invocam functie cu lista ##
# suma elemntelor din lista

def list_sum(my_list):
    sum = 0

    for num in my_list:
        c = 12
        sum += num + c
    return sum


print("Suma elementelor din lista este: ", list_sum([1, 5, 8, 3]))


#### use function in function
# create a function that returns the sum of 2 numbers multiplicated with the sum from previous function
# return the new value


def multiplication(num1, num2, list):
    sum_num = num1 + num2
    return sum_num * list_sum(list)


print(multiplication(3, 8, [1, 3, 5]))


#### function that returns a list ##########

def my_sweet_list(n):
    sweet_list = []

    for i in range(n):
        sweet_list.insert(0, i)

    return sweet_list[::-1]


print(my_sweet_list(5))


###### functie --> valoarea absoluta a unui numar

def absolute_value(num):
    """
    This function returns the absolute value of the entered number
    :param num: the number
    :return: absolute value
    """
    if num >= 0:
        return num
    else:
        return -num


################ T E M A #######################
# sa se introduca de la tastatura un numar si sa se afle valoarea absoluta
# utilizatorul va introduce ceva daca vrea sa termine "jocul".
while True:
    num_user = int(input("Introdu un numar. Daca vrei sa te opresti baga 0: "))
    if num_user == 0:
        break
    else:
        print(absolute_value(int(input("Introduceti un numar: "))))

print(absolute_value(int(input("Introduceti un numar: "))))


### definim clasa persoana

class Person:
    def __init__(self, first_name, last_name, height, weight, age):
        # scriem atributele
        self.first_name = first_name  # atribut
        self.last_name = last_name  # atribut
        self.height = height  # atribut
        self.weight = weight  # atribut
        self.age = age  # atribut


# cream o noua persoana (o instanta/obiect a clasei Person)


user = Person("Angela", "Bratu", 170, 75, 34)
print(user.last_name)  # ne arata numele userului


# definim clasele Student and Courses

class Student:
    # definim constructorul clasei
    def __init__(self, name, surname, age, year, grade):
        # atributele studentului cu ajutorul carora vom crea un obiect de tip student
        self.name = name
        self.surname = surname
        self.age = age
        self.year = year  # 1 - 4
        self.grade = grade  # 1 - 10

    # definim o metoda
    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students, duration):
        # definim atributele
        self.name = name
        self.max_students = max_students
        self.duration = 2
        self.students = []

    # cream metoda cu care adaugam studenti la curs
    def add_students(self, student):  # studentul va fi o instanta a clasei student
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False


# cream obiect/instanta a clasei Student (Cream un Student)

student1 = Student("Glassworth", "Lina", 19, 1, 8)  # instanta/obiect a clasei student
student2 = Student("Glass", "Diana", 20, 1, 10)  # instanta/obiect a clasei student
student3 = Student("Worth", "Bogdan", 19, 1, 9)  # instanta/obiect a clasei student

# cream obiect/instanta a clasei Curs (cream un curs)
c1 = Course("Analiza matematica", 7, 2)
c2 = Course("Computer science", 2, 2)

# print name of student 2
print(student2.name)
# print year of student 3
print(student3.year)

# adaugam studentul 1 la cursul 1
c1.add_students(student2)
c1.add_students(student1)

# afiseaza numele primului student dinents[0].name)

# adaugam studentii1,2,3 la c2

c2.add_students(student1)
c2.add_students(student2)
c2.add_students(student3)

# printam studentii din c2
print(c2.students[0].name)
print(c2.students[1].name)
print(c2.students[2].name)

