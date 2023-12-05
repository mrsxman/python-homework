# 1 

# Kvadratning perimetri
P = 20

# Kvadratning tomonini hisoblash
a = P / 4

# Natijani chop etish
print("Kvadratning tomoni:", a)

# 2 
# Kvadratning tomoni
a = float(input("Kvadratning tomonini kiriting: "))

# Kvadratning yuzasini hisoblash
S = a**2

# Natijani chop etish
print("Kvadratning yuzasi:", S)

# 3

# To'g'ri to'rtburchakning tomonlari
a = float(input("To'g'ri to'rtburchakning birinchi tomonini kiriting: "))
b = float(input("To'g'ri to'rtburchakning ikkinchi tomonini kiriting: "))

# Yuzani va perimeterni hisoblash
S = a * b
P = 2 * (a + b)

# Natijani chop etish
print("To'g'ri to'rtburchakning yuzasi:", S)
print("To'g'ri to'rtburchakning perimetri:", P)


# 4

import math

# Aylana (doira) diametri
d = float(input("Aylana diametrini kiriting: "))

# Aylananing uzunligini hisoblash
L = math.pi * d

# Natijani chop etish
print("Aylananing uzunligi:", L)

# 5

# Kubning yon tomoni
a = float(input("Kubning yon tomonini kiriting: "))

# Kubning hajmini va to'la sirtini hisoblash
V = a**3
S = 6 * a**2

# Natijani chop etish
print("Kubning hajmi:", V)
print("Kubning to'la sirti:", S)

# 6

# Paralelepipedning tomonlari
a = float(input("a tomonini kiriting:"))
b = float(input("b tomonini kiriting:"))
c = float(input("c tomonini kiriting:"))

# Paralelepipedning hajmini va to'la sirtini hisoblash
V = a * b * c
S = 2 * (a*b + b*c + a*c)

# Natijani chop etish
print("Paralelepipedning hajmi:", V)
print("Paralelepipedning to'la sirti:", S)

# 7 

import math

# Doiraning radiusi
r = float(input("Doiraning radiusini kiriting: "))

# Doiraning uzunligi va yuzasini hisoblash
l = 2 * math.pi * r
S = math.pi * r**2

# Natijani chop etish
print("Doiraning uzunligi:", l)
print("Doiraning yuzasi:", S)

# 8

# Ikkta son a va b
a = float(input("a ni kiriting: "))
b = float(input("b ni kiriting: "))

# O'rta arifmetigini hisoblash
ort_arifmetik = (a + b) / 2

# Natijani chop etish
print("Ikta sonning o'rta arifmetigi:", ort_arifmetik)

# 9

import math

# Ikta manfiy bo'lmagan son a va b
a = float(input("a ni kiriting: "))
b = float(input("b ni kiriting: "))

# O'rta geometrigini hisoblash
ort_geometrik = math.sqrt(a * b)

# Natijani chop etish
print("Ikta manfiy bo'lmagan sonning o'rta geometrigi:", ort_geometrik)

# 10

# Ikta son a va b
a = float(input("a ni kiriting: "))
b = float(input("b ni kiriting: "))

# Yig'indini, ko'paytmasini va har bir sonning yig'indisini hisoblash
yigindi = a + b
kopaytma = a * b
birinchi_yigindi = a
ikkinchi_yigindi = b

# Natijani chop etish
print("Yig'indi:", yigindi)
print("Ko'paytma:", kopaytma)
print("Birinchi sonning yig'indisi:", birinchi_yigindi)
print("Ikkinchi sonning yig'indisi:", ikkinchi_yigindi)

# 11

# Ikta son a va b
a = float(input("a ni kiriting: "))
b = float(input("b ni kiriting: "))

# Yig'indini, ko'paytmasini va har bir sonning modulini hisoblash
yigindi = a + b
kopaytma = a * b
birinchi_modul = abs(a)
ikkinchi_modul = abs(b)

# Natijani chop etish
print("Yig'indi:", yigindi)
print("Ko'paytma:", kopaytma)
print("Birinchi sonning moduli:", birinchi_modul)
print("Ikkinchi sonning moduli:", ikkinchi_modul)

# 12

import math

def togri_uchburchak_parametrlari(a, b):
    # Gipotenuza ni hisoblash
    c = math.sqrt(a**2 + b**2)
    
    # Perimeterni hisoblash
    p = a + b + c
    
    return c, p

# Misol uchun a = 3, b = 4
a = 3
b = 4

c, p = togri_uchburchak_parametrlari(a, b)

print(f"Gipotenuza (c): {c}")
print(f"Perimetri (p): {p}")

# 13

import math
 
def aylana_hisoblash(radius):
    # Aylananing yuzasi (S)
    S = math.pi * radius**2
    
    # Aylananing ayirmasi (C)
    C = 2 * math.pi * radius
    
    return S, C

# Misol uchun radius = 5
radius = 5

S, C = aylana_hisoblash(radius)

print(f"Aylananing yuzasi (S): {S}")
print(f"Aylananing ayirmasi (C): {C}")

# 14

import math

def aylana_hisoblash_uzunlik(L):
    # Radiusni hisoblash
    r = L / (2 * math.pi)
    
    # Yuzani hisoblash
    S = math.pi * r**2
    
    return r, S

# Misol uchun uzunlik L = 10
L = 10

r, S = aylana_hisoblash_uzunlik(L)

print(f"Aylananing radiusi (r): {r}")
print(f"Aylananing yuzasi (S): {S}")

# 15

import math

def aylana_hisoblash_yuzasi(S):
    # Radiusni hisoblash
    R = math.sqrt(S / math.pi)
    
    # Diametrni hisoblash
    D = 2 * R
    
    return R, D

# Misol uchun yuzasi S = 15
S = 15

R, D = aylana_hisoblash_yuzasi(S)

print(f"Aylananing radiusi (R): {R}")
print(f"Aylananing diametri (D): {D}")

# 16

import math

def nuqta_masofasi(x1, y1, x2, y2):
    # Nuqta orasidagi masofani hisoblash
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    return d

# Misol uchun nuqtalar (x1, y1) va (x2, y2)
x1, y1 = 1, 2
x2, y2 = 4, 6

masofa = nuqta_masofasi(x1, y1, x2, y2)

print(f"Nuqta orasidagi masofa: {masofa}")

# 17

import math

def kesma_uzunligi(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def yigindisi_topuvchi_paradigma(xa, ya, xb, yb, xc, yc):
    uzunlik_AC = kesma_uzunligi(xa, ya, xc, yc)
    uzunlik_BC = kesma_uzunligi(xb, yb, xc, yc)
    
    yigindisi = uzunlik_AC + uzunlik_BC
    
    return uzunlik_AC, uzunlik_BC, yigindisi

# Misol uchun nuqtalar
xa, ya = 1, 2
xb, yb = 4, 6
xc, yc = 7, 8

uzunlik_AC, uzunlik_BC, yigindisi = yigindisi_topuvchi_paradigma(xa, ya, xb, yb, xc, yc)

print(f"AC kesmasining uzunligi: {uzunlik_AC}")
print(f"BC kesmasining uzunligi: {uzunlik_BC}")
print(f"Yig'indisi: {yigindisi}")

# 18

import math

def kesma_uzunligi(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def kopaytma_topuvchi_paradigma(xa, ya, xb, yb, xc, yc):
    uzunlik_AC = kesma_uzunligi(xa, ya, xc, yc)
    uzunlik_BC = kesma_uzunligi(xb, yb, xc, yc)
    
    kopaytma = uzunlik_AC / uzunlik_BC
    
    return kopaytma

# Misol uchun nuqtalar
xa, ya = 1, 2
xb, yb = 4, 6
xc, yc = 2, 4  # C nuqta A va B nuqtalar orasida joylashgan

kopaytma = kopaytma_topuvchi_paradigma(xa, ya, xb, yb, xc, yc)

print(f"AC kesmasining BC kesmasiga nisbat ko'paytmasi: {kopaytma}")

# 19

import math

def tomon_uzunligi(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def tortburchak_perimetri(x1, y1, x2, y2, x3, y3, x4, y4):
    d12 = tomon_uzunligi(x1, y1, x2, y2)
    d23 = tomon_uzunligi(x2, y2, x3, y3)
    d34 = tomon_uzunligi(x3, y3, x4, y4)
    d41 = tomon_uzunligi(x4, y4, x1, y1)

    return d12 + d23 + d34 + d41

def tortburchak_yuza(x1, y1, x2, y2, x3, y3, x4, y4):
    p = tortburchak_perimetri(x1, y1, x2, y2, x3, y3, x4, y4)
    d12 = tomon_uzunligi(x1, y1, x2, y2)
    d23 = tomon_uzunligi(x2, y2, x3, y3)
    d34 = tomon_uzunligi(x3, y3, x4, y4)
    d41 = tomon_uzunligi(x4, y4, x1, y1)

    s = math.sqrt(p * (p - d12) * (p - d23) * (p - d34) * (p - d41))
    return s

# Koordinatalar
x1, y1 = 0, 0
x2, y2 = 0, 4
x3, y3 = 3, 4
x4, y4 = 3, 0

# Tomon uzunliklari, perimetr va yuza
print("Tomon uzunliklari:")
print("d12:", tomon_uzunligi(x1, y1, x2, y2))
print("d23:", tomon_uzunligi(x2, y2, x3, y3))
print("d34:", tomon_uzunligi(x3, y3, x4, y4))
print("d41:", tomon_uzunligi(x4, y4, x1, y1))

print("\nPerimetri:", tortburchak_perimetri(x1, y1, x2, y2, x3, y3, x4, y4))
print("Yuzasi:", tortburchak_yuza(x1, y1, x2, y2, x3, y3, x4, y4))


# 20
import math

def masofa(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Misol uchun koordinatalar
x1, y1 = 1, 2
x2, y2 = 4, 6

# Ikki nuqta orasidagi masofa
distance = masofa(x1, y1, x2, y2)

print(f"Ikki nuqta ({x1}, {y1}) va ({x2}, {y2}) orasidagi masofa: {distance}")

# 21

import math

def tomon_uzunligi(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def uchburchak_perimetri(x1, y1, x2, y2, x3, y3):
    d12 = tomon_uzunligi(x1, y1, x2, y2)
    d23 = tomon_uzunligi(x2, y2, x3, y3)
    d31 = tomon_uzunligi(x3, y3, x1, y1)

    return d12 + d23 + d31

def uchburchak_yuza(x1, y1, x2, y2, x3, y3):
    d12 = tomon_uzunligi(x1, y1, x2, y2)
    d23 = tomon_uzunligi(x2, y2, x3, y3)
    d31 = tomon_uzunligi(x3, y3, x1, y1)

    s = uchburchak_perimetri(x1, y1, x2, y2, x3, y3) / 2
    area = math.sqrt(s * (s - d12) * (s - d23) * (s - d31))

    return area

# Misol uchun koordinatalar
x1, y1 = 1, 2
x2, y2 = 4, 6
x3, y3 = 7, 2

# Uchburchakning tomon uzunliklari, perimetri va yuzasi
print("Tomon uzunliklari:")
print("d12:", tomon_uzunligi(x1, y1, x2, y2))
print("d23:", tomon_uzunligi(x2, y2, x3, y3))
print("d31:", tomon_uzunligi(x3, y3, x1, y1))

print("\nPerimetri:", uchburchak_perimetri(x1, y1, x2, y2, x3, y3))
print("Yuzasi:", uchburchak_yuza(x1, y1, x2, y2, x3, y3))


# 22

# a va b ni o'qitamiz
a = int(input("a ni kiriting: "))
b = int(input("b ni kiriting: "))

# Qiymatlarni almashtiramiz
a, b = b, a

# Yangi     qiymatlarni chiqaramiz
print("Yangi a qiymati:", a)
print("Yangi b qiymati:", b)


# 23

# a, b, va c ni o'qitamiz
a = int(input("a ni kiriting: "))
b = int(input("b ni kiriting: "))
c = int(input("c ni kiriting: "))

# Qiymatlarni almashtiramiz
a, b, c = b, c, a

# Yangi qiymatlarni chiqaramiz
print("Yangi a qiymati:", a)
print("Yangi b qiymati:", b)
print("Yangi c qiymati:", c)


# 24

# a, b, va c ni o'qitamiz
a = int(input("a ni kiriting: "))
b = int(input("b ni kiriting: "))
c = int(input("c ni kiriting: "))

# Qiymatlarni almashtiramiz
a, b, c = c, a, b

# Yangi qiymatlarni chiqaramiz
print("Yangi a qiymati:", a)
print("Yangi b qiymati:", b)
print("Yangi c qiymati:", c)


# 25
def misol_funksiya(x):
    # Sizning funksiya logikangizni joylashtiring
    result = x ** 2 + 3 * x + 5
    return result

# Qiymatni aniqlash uchun x ni tanlang
x_value = 7

# Funksiyani chaqirish va natijani olish
result_value = misol_funksiya(x_value)

# Natijani chiqarish
print(f"Funksiyaning {x_value} qiymati: {result_value}")

# 27

def daraja_hisobla(a, n):
    """a sonini n-darajaga ko'taradigan funksiya"""
    return a ** n

# Misol qiymatlar
a_soni = 2
daraja = 3

# Natijani chiqarish
natija = daraja_hisobla(a_soni, daraja)
print(f"{a_soni} ning {daraja}-darajasi: {natija}")


# 29
import math

def gradusdan_radianga_otkaz(gradus):
    """Berilgan burchakni radianlarga otkazuvchi funksiya"""
    radian = math.radians(gradus)
    return radian

# Misol  qiymat
burchak_gradus = 45

# Burchakni radianlarga otkazish
burchak_radian = gradusdan_radianga_otkaz(burchak_gradus)

# Natijani chiqarish
print(f"{burchak_gradus} gradus {burchak_radian} radian")

# 30

def gradusga_otkaz(gradus, miqyos=1):
    """Berilgan burchakni gradusga otkazuvchi funksiya"""
    burchak_gradus = gradus * miqyos
    return burchak_gradus

# Misol qiymat
burchak_gradus = 45

# Burchakni gradusga otkazish
burchak_gradus_o_tkazilgan = gradusga_otkaz(burchak_gradus)

# Natijani chiqarish
print(f"{burchak_gradus} gradus {burchak_gradus_o_tkazilgan} ga otkazilgan")

# 31

def fahrenheitdan_celsiusga_otkaz(fahrenheit):
    """Fahrenheit temperaturasini Celsiusga otkazuvchi funksiya"""
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

# Misol qiymat
fahrenheit_temperatura = 98.6

# Fahrenheitdan Celsiusga otkazish
celsius_temperatura = fahrenheitdan_celsiusga_otkaz(fahrenheit_temperatura)

# Natijani chiqarish
print(f"{fahrenheit_temperatura} Fahrenheit {celsius_temperatura:.2f} Celsius ga otkazilgan")

# 32

def celsiusdan_fahrenheitga_otkaz(celsius):
    """Celsius temperaturasini Fahrenheitga otkazuvchi funksiya"""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Misol qiymat
celsius_temperatura = 37.5

# Celsiusdan Fahrenheitga otkazish
fahrenheit_temperatura = celsiusdan_fahrenheitga_otkaz(celsius_temperatura)

# Natijani chiqarish
print(f"{celsius_temperatura} Celsius {fahrenheit_temperatura:.2f} Fahrenheit ga otkazilgan")


# 33

# Konfet narxi va miqdori
narx_kofe = 5  # Kofe narxi 1 kg uchun
miqdor_kofe = float(input("Kofe miqdorini kiriting (kg): "))  # Foydalanuvchidan kofe miqdorini so'raymiz

narx_konfet = 8  # Konfet narxi 1 kg uchun
miqdor_konfet = float(input("Konfet miqdorini kiriting (kg): "))  # Foydalanuvchidan konfet miqdorini so'raymiz

# Umumiy narxni hisoblash
umumiy_narx = narx_kofe * miqdor_kofe + narx_konfet * miqdor_konfet

# Natijani chiqarish
print(f"{miqdor_kofe} kg kofe va {miqdor_konfet} kg konfetning umumiy narxi {umumiy_narx} so'm.")

# 34

# Narxlar
narx_shkalat = float(input("1 kg shkalat narxini kiriting (so'm): "))
narx_konfet = float(input("1 kg konfet narxini kiriting (so'm): "))

# Miqdorlar
miqdor_shkalat = float(input("Shkalat miqdorini kiriting (kg): "))
miqdor_konfet = float(input("Konfet miqdorini kiriting (kg): "))

# Umumiy narxni hisoblash
umumiy_narx = narx_shkalat * miqdor_shkalat + narx_konfet * miqdor_konfet

# Natijani chiqarish
print(f"{miqdor_shkalat} kg shkalat va {miqdor_konfet} kg konfetning umumiy narxi {umumiy_narx} so'm.")

# 35

# Qayiqning tezligi (km/soat)
tezlik_qayiq = 100

# Daryo oqimining tezligi (km/soat)
tezlik_daryo = 50

# Qayiqning harakatlanish vaqtini (soat)
vaqt_harakat_qayiq = 4

# Oqimga qarshi harakatlanish vaqtini (soat)
vaqt_harakat_oqim = 3

# Qayiqning yurgan yo'lini hisoblash
masofa_harakat_qayiq = tezlik_qayiq * vaqt_harakat_qayiq
masofa_harakat_oqim = tezlik_daryo * vaqt_harakat_oqim

# Keyingi harakatlanish joyini topish
masofa_keyingi_harakatlanish = masofa_harakat_qayiq - masofa_harakat_oqim

print(f"Qayiq yurgan yo'l: {masofa_harakat_qayiq} km")
print(f"Oqimga qarshi yurgan yo'l: {masofa_harakat_oqim} km")
print(f"Keyingi harakatlanish joyi: {masofa_keyingi_harakatlanish} km")

# 36

# Birinchi avtomobil tezligi (km/soat)
v1 = 50

# Ikkinchi avtomobil tezligi (km/soat)
v2 = 100

# Ular orasidagi masofa (km)
S = float(input("Masofani kiriting (km): "))

# Ular orasidagi uzoqlashish vaqti (soat)
T = S / (v1 + v2)

print(f"Birinchi avtomobil {T} soatdan keyin ikkinchi avtomobil bilan uzoqlashadi.")


# 37

# Birinchi avtomobil tezligi (km/soat)
v1 = 50

# Ikkinchi avtomobil tezligi (km/soat)
v2 = 100

# Ular orasidagi boshlang'ich masofa (km)
S = float(input("Boshlang'ich masofani kiriting (km): "))

# Uzoqlashish vaqti (soat)
T = S / (v1 + v2)

# Keyingi masofa (km)
S_keyingi = T * (v1 + v2)

print(f"Birinchi avtomobil {T} soatdan keyin ikkinchi avtomobil bilan uzoqlashadi.")
print(f"Boshlang'ichdan keyin ular orasidagi masofa {S_keyingi} km bo'ladi.")



# 38

# Koefitsentlarni olish
a = float(input("a ni kiriting: "))
b = float(input("b ni kiriting: "))

# x ni olish
x = float(input("x ni kiriting: "))

# Chiziqli tenglamaning yechimi
y = a * x + b

# Natijani chiqarish
print(f"Chiziqli tenglama {x} qiymatida y = {y}")

# 39

import math  # Complex math kutubxonasini import qilamiz

# Koefitsentlarni olish
a = float(input("a ni kiriting: "))
b = float(input("b ni kiriting: "))
c = float(input("c ni kiriting: "))

# Diskriminantni hisoblash
D = b**2 - 4*a*c

# Diskriminantni tekshirish
if D >= 0:
    # Haqiqiy yechimlar
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print(f"Tenglama haqiqiy yechimlari: x1 = {x1}, x2 = {x2}")
else:
    # Kompleks yechimlar
    real_part = -b / (2*a)
    imag_part = math.sqrt(-D) / (2*a)
    x1 = complex(real_part, imag_part)
    x2 = complex(real_part, -imag_part)
    print(f"Tenglama kompleks yechimlari: x1 = {x1}, x2 = {x2}")


# 40

# Koefitsentlarni olish
a = float(input("a ni kiriting: "))
b = float(input("b ni kiriting: "))
e = float(input("e ni kiriting: "))
c = float(input("c ni kiriting: "))
d = float(input("d ni kiriting: "))
f = float(input("f ni kiriting: "))

# Tenglamalar sistemasi yechimlarini hisoblash
det = a*d - b*c  # Determinant
det_x = e*d - b*f
det_y = a*f - e*c

# Yechimlarni hisoblash
x = det_x / det
y = det_y / det

# Natijani chiqarish
print(f"Tenglamalar sistemasi yechimlari: x = {x}, y = {y}")