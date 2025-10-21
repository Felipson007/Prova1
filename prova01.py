def media_dois_maiores(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Todos os números devem ser positivos"
    menor = min(a, b, c)
    soma_total = a + b + c
    soma_dos_maiores = soma_total - menor
    return soma_dos_maiores / 2
print("Digite três números inteiros positivos:")
num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))
num3 = int(input("Terceiro número: "))
resultado = media_dois_maiores(num1, num2, num3)
print(f"\nA média dos dois maiores valores é: {resultado}")