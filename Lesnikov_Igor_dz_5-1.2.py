# Генератор нечётных чисел
gen_odd = (i + 2 for i in range(-1, 15, 2))
for odd_number in gen_odd:
    print(f"odd number is: {odd_number}")
