class TablaHash:
    def __init__(self, capacidad=10, tipo_hash="buena"):
        self.cap = capacidad
        self.cubetas = [[] for _ in range(self.cap)]
        self.n = 0
        self.tipo_hash = tipo_hash  # Recibe "buena" o "mala"

    def _hash(self, clave):
        clave_str = str(clave)
        
        # Función Hash Mala
        if self.tipo_hash == "mala":
            return sum(ord(c) for c in clave_str[:4]) % self.cap
        
        # Función Hash Buena
        h = 0
        for c in clave_str:
            h = (h * 31 + ord(c)) % self.cap
        return h

    def factor_carga(self):
        """Calcula el factor de carga actual de la tabla."""
        return self.n / self.cap

    def insertar(self, clave, valor):
        i = self._hash(clave)
        for par in self.cubetas[i]:
            if par[0] == clave:
                par[1] = valor  # ACTUALIZA, no duplica
                return
        self.cubetas[i].append([clave, valor])
        self.n += 1

        # El redimensionamiento va al final de insertar()
        if self.factor_carga() > 0.75:
            self._redimensionar()

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
        # Duplicar self.cap
        self.cap *= 2
        # Crear cubetas vacias nuevas y poner self.n en 0
        self.cubetas = [[] for _ in range(self.cap)]
        self.n = 0
        # Recorrer 'viejas' e insertar cada (clave, valor) otra vez
        for cubeta in viejas:
            for clave, valor in cubeta:
                self.insertar(clave, valor)


# --- PRUEBA CON TUS ESTUDIANTES ---

# Se prueba con la funcion buena que se puede cambiar a mala si se escribe tipo_hash="mala"
tabla_estudiantes = TablaHash(capacidad=12, tipo_hash="buena")

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

# Función para mostrar las métricas solicitadas
def reportar_metricas(tabla, nombre_funcion):
    print(f"=== RESULTADOS CON FUNCIÓN HASH: {nombre_funcion.upper()} ===")
    print(f"Capacidad final: {tabla.cap}")
    
    # Distribución (cantidad de elementos en cada cubeta)
    distribucion = [len(c) for c in tabla.cubetas]
    print(f"Distribución por cubeta: {distribucion}")
    
    print(f"Factor de carga final: {tabla.factor_carga():.2f}")
    
    # Cubeta más llena
    max_llena = max(len(c) for c in tabla.cubetas)
    print(f"Tamaño de la cubeta más llena: {max_llena}")
    
    # Cubetas vacías
    cubetas_vacias = sum(1 for c in tabla.cubetas if len(c) == 0)
    print(f"Número de cubetas vacías: {cubetas_vacias}")
    print("=" * 50 + "\n")


# 1. FUNCIÓN BUENA
tabla_buena = TablaHash(capacidad=12, tipo_hash="buena")
for codigo, nombre in estudiantes:
    tabla_buena.insertar(codigo, nombre)
reportar_metricas(tabla_buena, "buena")

# Buscar a "EST-2026-0107"
estudiante_buscar = tabla_buena.buscar("EST-2026-0107")

print(f"\nEstudiante encontrado con tabla buena: {estudiante_buscar}")


# 2. FUNCIÓN MALA
tabla_mala = TablaHash(capacidad=12, tipo_hash="mala")
for codigo, nombre in estudiantes:
    tabla_mala.insertar(codigo, nombre)
reportar_metricas(tabla_mala, "mala")