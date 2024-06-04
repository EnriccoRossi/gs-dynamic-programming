import math

def calcular_distancia(p1, p2):
    #função para calcular a distância euclidiana entre dois pontos p1 e p2
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def calcular_area_recursiva(pontos, i=0):
    #função recursiva para calcular a área de um polígono usando a fórmula de Shoelace
    if i == len(pontos) - 1:  #caso base: se estiver no último ponto, fecha o polígono com o primeiro ponto
        return pontos[i][0] * pontos[0][1] - pontos[i][1] * pontos[0][0]
    else:
        #recursão: soma a área do ponto atual com o próximo ponto e chama a função para o próximo ponto
        return (pontos[i][0] * pontos[i + 1][1] - pontos[i][1] * pontos[i + 1][0]) + calcular_area_recursiva(pontos, i + 1)

def calcular_area(quadrilatero):
    #função para encapsular a chamada recursiva da área e calcular o valor absoluto da área total
    return 0.5 * abs(calcular_area_recursiva(quadrilatero))

#exemplo de uso para calcular a área de um quadrilátero
quadrilatero = [(100, 30), (30, 20), (50, 40), (10, 40)]
area = calcular_area(quadrilatero)
print(f"A área do quadrilátero é: {area}m²")

def calcular_raio_sensor(area_sensor):
    #função para calcular o raio de um sensor dado a área que ele cobre
    return math.sqrt(area_sensor / math.pi)

def distribuir_sensores(quadrilatero, raio_sensor):
    #função para distribuir sensores em uma grade sobre o quadrilátero

    x_coords = [p[0] for p in quadrilatero]  #extrai as coordenadas x dos pontos do quadrilátero
    y_coords = [p[1] for p in quadrilatero]  #extrai as coordenadas y dos pontos do quadrilátero

    min_x, max_x = min(x_coords), max(x_coords)  #determina os limites mínimos e máximos em x
    min_y, max_y = min(y_coords), max(y_coords)  #determina os limites mínimos e máximos em y

    sensores = []
    x = min_x
    while x <= max_x:
        y = min_y
        while y <= max_y:
            #adiciona o sensor na posição arredondada se estiver dentro dos limites
            if (min_x <= x <= max_x) and (min_y <= y <= max_y):
                sensores.append((round(x, 2), round(y, 2)))
            y += 2 * raio_sensor  #move para a próxima posição em y
        x += 2 * raio_sensor  #move para a próxima posição em x

    return sensores

#exemplo de uso para distribuir sensores sobre um quadrilátero
quadrilatero = [(10, 20), (30, 10), (30, 40), (20, 40)]
raio_sensor = calcular_raio_sensor(10)
sensores = distribuir_sensores(quadrilatero, raio_sensor)

print(f"Raio de cada sensor: {raio_sensor:.2f}m²")
print("Posições dos sensores:")
contador = 0
for sensor in sensores:
    print(f"{contador} - {sensor}")
    contador += 1
