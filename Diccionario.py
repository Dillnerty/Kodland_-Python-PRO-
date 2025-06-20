dic = {
    "LOL" : "Una respuesta a algo gracioso",
    "CRINGE" : "Algo raro o embarazoso",   
    "ROFL" : "Una respuesta a una broma",
    "CREEPY" : "Aterrador, siniestro"
    }

while True:
    question = input("Introduce una palabra 'desconocida' (en mayúsculas): ")
    if question in dic:
        print(dic[question])
    elif question == "FIN":
        break
    else:
        print("Ni nosotros sabemos que significa")
