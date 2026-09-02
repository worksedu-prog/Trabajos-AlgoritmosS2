# ============================================================
#  Cívica Software  ·  TCK-5512  ·  Severidad P0  ·  PRODUCCION CAIDA
#  Sistema: TurnoJusto  —  El historial de atenciones esta corrupto.
#
#  Reportes de soporte:
#   - "Registre la primera atencion del dia y el sistema se cayo."
#   - "Deshice la ultima atencion y se borro todo el historial."
#   - "Busco un turno que si existe y me dice que no esta."
# ============================================================

class Nodo:
    def __init__(self, turno, modulo):
        self.turno = turno
        self.modulo = modulo
        self.siguiente = None


class Historial:
    def __init__(self):
        self.cabeza = None

    def registrar(self, turno, modulo):
        """Agrega una atencion al FINAL del historial.
           BUG: se cae cuando el historial esta vacio."""
        nuevo = Nodo(turno, modulo)
        actual = self.cabeza                  # <-- ¿que pasa si no hay cabeza? (SI NO HAY CABEZA, actual es None y el while falla)
        if actual is None:
            self.cabeza = nuevo
            return
        while actual.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = nuevo

    def deshacer_ultima(self):
        """Elimina la ULTIMA atencion registrada.
           Devuelve True si elimino algo, False si el historial estaba vacio.
           BUG: borra todo el historial."""
        if self.cabeza is None:
            return False
        if self.cabeza.siguiente is None:
            self.cabeza = None
            return True
        actual = self.cabeza
        while actual.siguiente.siguiente is not None:
            actual = actual.siguiente
        actual.siguiente = None #(SE AGREGA UNA LINEA PARA ELIMINAR EL ULTIMO NODO)
        return True

    def buscar(self, turno):
        """Devuelve el modulo que atendio ese turno, o None si no existe.
           PENDIENTE: implementar."""
        actual = self.cabeza
        while actual is not None:
            if actual.turno == turno:
                return actual.modulo
            actual = actual.siguiente  #(SE CREA UN MODULO PARA RECORRER LA LISTA)
        return None

    def cuantas(self):
        n = 0
        actual = self.cabeza
        while actual is not None:
            n += 1
            actual = actual.siguiente
        return n

    def listar(self):
        r = []
        actual = self.cabeza
        while actual is not None:
            r.append(actual.turno)
            actual = actual.siguiente
        return r
