# Operator
# Operator Aritmatika
a = 25
b = 10
c = 50

penjumlahan = a + b + c
sisabagi = c % a
perkalian = a * b * c
pembagian = c / a
pengurangan = c - a
perpangkatan = a ** 2
pembagian_bulat = c // a

print(f"Hasil penjumlahan {a} + {b} + {c} = {penjumlahan}")
print(f"Hasil sisa bagi {c} mod {a} = {sisabagi}")
print(f"Hasil perkalian {a} * {b} * {c} = {perkalian}")
print(f"Hasil pembagian {c} / {a} = {pembagian}")
print(f"Hasil pengurangan {c} - {a} = {pengurangan}")
print(f"Hasil perpangkatan {a} ** 2 = {perpangkatan}")
print(f"Hasil pembagian bulat {c} // {a} = {pembagian_bulat}")

# Operator Assignment
a += 15
a **= 2
print(a)

# Operator Perbandingan
perbandingan = a >= b

x = 100
y = 45
banding = x <= y

print(x != y)
print(banding)

# Operator Logika AND
print("--- Operator Logika ---")

opAnd = a >= b and x <= y and x != y
opOR = perbandingan or banding or x != y
opNOT = not opAnd

print(opAnd)
print(opOR)
print(opNOT)