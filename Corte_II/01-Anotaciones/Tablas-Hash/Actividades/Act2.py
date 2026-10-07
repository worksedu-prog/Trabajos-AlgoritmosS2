# Paso 1: La estructura de datos hash
class TablaHash:
    def __init__(self, capacidad=10):
        self.cap = capacidad
        self.cubetas = [[] for _ in range(self.cap)]
        self.n = 0

    def _hash(self, clave):
        h = 0
        for c in str(clave):
            h = (h * 31 + ord(c)) % self.cap
        return h

    def insertar(self, clave, valor):
        i = self._hash(clave)
        for par in self.cubetas[i]:
            if par[0] == clave:
                par[1] = valor  # ACTUALIZA, no duplica
                return
        self.cubetas[i].append([clave, valor])
        self.n += 1

    def buscar(self, clave):
        i = self._hash(clave)
        for k, v in self.cubetas[i]:  # recorre SOLO esa cubeta
            if k == clave:
                return v
        return None

    def eliminar(self, clave):
        i = self._hash(clave)
        for idx, (k, _) in enumerate(self.cubetas[i]):
            if k == clave:
                self.cubetas[i].pop(idx)
                self.n -= 1
                return True
        return False
    
    def _redimensionar(self):
        viejas = self.cubetas
        #TODO 1: duplicar self.cap
        #TODO 2: crear cubetas vacias nuevas y poner self.n en 0
        #TODO 3: recorrer 'viejas' e insertar cada (clave, valor) otra vez

    # y al final de insertar():
        if self.factor_carga() > 0.75:
            self._redimensionar()


# 1. Cargar estudiantes en la tabla hash
tabla_estudiantes = TablaHash(capacidad=12)

estudiantes = [
    ("EST-2026-0101", "Ana Torres"),
    ("EST-2026-0102", "Carlos Rojas"),
    ("EST-2026-0103", "Diego Pardo"),
    ("EST-2026-0104", "Sofia Mejia"),
    ("EST-2026-0105", "Juan Gomez"),
    ("EST-2026-0106", "Maria Lopez"),
    ("EST-2026-0107", "Pedro Ruiz"),
    ("EST-2026-0108", "Camila Diaz"),
    ("EST-2026-0109", "Luis Herrera"),
    ("EST-2026-0110", "Valentina Cruz"),
    ("EST-2026-0111", "Andres Vega"),
    ("EST-2026-0112", "Laura Castro"),
]

# Cargar los datos de los estudiantes
for codigo, nombre in estudiantes:
    tabla_estudiantes.insertar(codigo, nombre)

# Buscar a "EST-2026-0107"
estudiante_buscar = tabla_estudiantes.buscar("EST-2026-0107")

print(f"Estudiante encontrado: {estudiante_buscar}")