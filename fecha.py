from datetime import datetime

def current_date_format(date):
    months = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    days = date.day
    semana = now.strftime('%A')
    if semana == "Monday":
     semana = "Lunes"
    elif semana == "Tuesday":
     semana = "Martes"
    elif semana == "Wednesday":
     semana = "Miercoles"
    elif semana == "Thursday ":
     semana = "Jueves"
    elif semana == "Friday ":
     semana = "viernes"
    elif semana == "Saturday":
     semana = "Sabado"
    elif semana == "Sunday":
     semana = "Domingo"
    month = months[date.month - 1]
    year = date.year
    messsage = "{} {} de {} del {}".format(semana,days, month, year)

    return messsage

now = datetime.now()
print(current_date_format(now))
d =datetime.now()
print(d.strftime("          "'%H:%M:%S'))
#dias = ("Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo")

