class Profesor:
    def __init__(self, el_nombre, el_email):
        self.nombre = el_nombre
        self.email = el_email

    def dame_tu_nombre(self):
        return self.nombre


class Alumno:
    def __init__(self, el_nombre_del_alumno):
        self.nombre = el_nombre_del_alumno
        self.inasistencias = 0
        self.dieta = ""
        self.mentor = None

    def mentoria(self, profesor):
        self.mentor = profesor

    def falta(self):
        self.inasistencias += 1

    def elegir_dieta_especial(self, la_dieta):
        self.dieta = la_dieta

    def es_vegano(self):
        self.dieta = "vegano"

    def esta_libre(self):
        if self.inasistencias >= 5:
            return "ESTA LIBRE"
        else:
            return "OK"


profe_elio = Profesor("Elio", "elio@gmail.com")
profe_gabi = Profesor("Gabriel", "gabriel@um.edu.ar")

# print(profe_elio.dame_tu_nombre())
# print(profe_gabi.dame_tu_nombre())

alumno_juan = Alumno("Juancito")
alumno_Maria = Alumno("Maria")

alumno_juan.falta()
alumno_juan.falta()
alumno_juan.falta()
alumno_juan.falta()
print(alumno_juan.esta_libre())
alumno_juan.falta()
print(alumno_juan.esta_libre())

alumno_Maria.elegir_dieta_especial("vegetariana")
print(alumno_Maria.dieta)
alumno_juan.es_vegano()
print(alumno_juan.dieta)

alumno_juan.mentoria(profe_elio)

print(alumno_juan.mentor)

import ipdb; ipdb.set_trace()