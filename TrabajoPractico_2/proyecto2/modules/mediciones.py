class Medicion:
    def __init__(self, fecha_dt, temperatura):
        self.fecha = fecha_dt
        self.temperatura = temperatura
    
    def __str__(self):
        return f"{self.fecha.strftime('%d/%m/%Y')}: {self.temperatura} ºC"