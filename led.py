resultadoFinal = []
A = int(input())
i = 0

def leds_por_numero(numero: str) -> int:
    leds_por_digito = {
        '0': 6, '1': 2, '2': 5, '3': 5, '4': 4,
        '5': 5, '6': 6, '7': 3, '8': 7, '9': 6
    }
    return sum(leds_por_digito[digito] for digito in numero)
while i < A:
    B = input()
    numero = B
    leds = leds_por_numero(B)
    resultadoFinal.append(leds)
    i = i + 1
for i, r in enumerate(resultadoFinal, 1):
    print(f"{r}leds")
    #teste brench 