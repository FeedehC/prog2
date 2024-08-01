import datetime
# from datetime import date
# from datetime import datetime

#Día actual
today = datetime.date.today()

#Fecha actual
now = datetime.datetime.now()

anio_nac = int(input("Ingrese su año de nacimiento: "))

edad = now.year - anio_nac
print("Edad: ", edad)