import random

def tirar_dado(numero_de_tiros):
    secuencia_de_tiros = []

    for _ in range(numero_de_tiros):
        tiro = random.choice( [1, 2, 3, 4, 5, 6] )
        secuencia_de_tiros.append(tiro)

    return secuencia_de_tiros


def main(numero_de_tiros, intentos):
    sumas = []

    for _ in range(intentos):
        sec1 = tirar_dado(numero_de_tiros) #[1,2,3,4,5,6] + 
        sec2 = tirar_dado(numero_de_tiros) #[1,2,5,6,3,4] = [2,4,8,10,8,10]
        suma = []
        for i, value1 in enumerate(sec1):
            value2 = sec2[i]
            suma.append(value1 + value2)
        
        sumas.append(suma)
    
    tiros_exitosos = 0
    for suma in sumas:
        if 12 in suma:
            tiros_exitosos += 1

    probabilidad_tiros_con_1 = tiros_exitosos / intentos
    print(f'Probabilidad de obtener por lo menos un 1 en {numero_de_tiros} tiros: {probabilidad_tiros_con_1}')

if __name__=='__main__':
    numero_de_tiros = int(input('Cuantos tiros del dado: '))
    intentos = int(input('Cuantos veces correrá la simulación: '))
    main(numero_de_tiros, intentos)