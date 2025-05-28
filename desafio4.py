def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

numeros_str = [str(i) for i in range(1, 101)]  

numeros_int = []
for num_str in numeros_str:
    num = int(num_str)
    numeros_int.append(num)
    if is_prime(num):
        print(f"{num} - Número primo")

print("\nNúmeros divisíveis por 2:")
for num in numeros_int:
    if num % 2 == 0:
        print(num, end=" ")
