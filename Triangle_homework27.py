# 1․ Գրել Triangle class, որը․
#    - __init__() -ում կընդունի եռանկյան կողմերը և կստուգի արդյոք նման կողմերով եռանկյուն գոյություն ունի թե ոչ,
#      եթե կողմերը սխալ են տրված կվերադարձնի Error համապատասխան տեքստով,
#    - կունենա մեթոդ, որը կվերադարձնի եռանկյան կողմերը,
#    - կունենա մեթոդ, որը կվերադարձնի եռանկյան պարագիծը,
#    - կունենա մեթոդ, որը կվերադարձնի եռանկյան մակերեսը,
#    - կունենա մեթոդ, որը կստուգի արդյոք եռանկյունը հավասարակողմ է, հավասարասրուն, թե անկանոն (կողմերը իրար = չեն),
#    - կունենա մեթոդ, որը կստուգի արդյոք եռանկյունը ուղղանկյուն եռանկյուն է, թե ոչ,
#    - կարող եք գրել նաև այլ մեթոդներ, որոնց միջոցով կստանաք տրված եռանկյան վերաբերյալ այլ ինֆորմացիա
#      (օրինակ՝ անկյունները, ներգծած և արտագծած շրջանագծերի շառավղերը և այլն)․ բանաձևերը կարող եք գտնել համացանցում։
#


class Triangle:
    def __init__(self, a, b, c,):
        if a + b > c or a + c > b or c + b > a:
            h = a ** 2 + b ** 2
            h = round(h ** 0.5, 2)
            self.a = a
            self.b = b
            self.c = c
            self.h = h
        else:
            print("Error")

    def __str__(self):
        return f"triangle a - {self.a} b - {self.b} c - {self.c} h - {self.h}"

    def perimetere(self):
        return f"perimetere is  {self.a + self.b + self.c}"

    def area(self):
        return f"area is {(self.h * self.b) / 2}"

    def typo(self):
        if self.a == self.b == self.b:
            print("equilateral triangle")
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            print("equal triangle")
        else:
            print("irregular triangle")

    def rightangle(self):
        if self.a ** 2 + self.b ** 2 == self.c **2 or  self.b ** 2 + self.c ** 2 == self.a **2 or self.a ** 2 + self.c ** 2 == self.b **2:
            print("rightangle triangle ")
        else:
            print("not rightangle triangle")









t = Triangle(9, 12, 15)

print(t)
print(t.perimetere())
print(t.area())
t.typo()
print(t.rightangle())