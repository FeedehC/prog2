def cifrar(texto, desp):
    result = ""
 
    for i in range(len(texto)):
        char = texto[i]
        if (char.isupper()):
            result += chr((ord(char) - ord("A") + desp) % 26 + ord("A"))
        else:
            result += chr((ord(char) - ord("a") + desp) % 26 + ord("a"))
    return result

texto = input("Ingrese una palabra para cifrar: ")
desp = int(input("Ingrese un desplazamiento: "))
print ("Palabra: " + texto)
print ("Desplazamiento: " + str(desp))
print ("Cifrado: " + cifrar(texto, desp))
