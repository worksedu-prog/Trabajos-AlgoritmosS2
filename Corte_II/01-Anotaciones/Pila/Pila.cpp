#include <cassert>  // Para assert(): validación de precondiciones en tiempo de ejecución
#include <memory>   // Para std::unique_ptr: gestión automática de memoria (RAII)
#include <utility>  // Para std::move: semántica de movimiento de recursos

// Clase plantilla (template) para una pila (Stack) basada en un arreglo dinámico
template <class T>
class ArrayStack {
    // std::unique_ptr gestiona la memoria dinámica del arreglo y la libera automáticamente al destruirse.
    std::unique_ptr<T[]> a; 
    
    size_t n = 0;   // Número actual de elementos almacenados en la pila
    size_t cap = 0; // Capacidad máxima del arreglo actual sin reasignar memoria

    // Método privado para redimensionar el arreglo dinámico cuando se llena o queda muy vacío
    void resize(size_t c) {
        // 1. Asigna un nuevo arreglo dinámico en memoria con la nueva capacidad 'c'
        std::unique_ptr<T[]> b(new T[c]);
        
        // 2. Transfiere los elementos del arreglo antiguo al nuevo usando 'std::move' para mayor eficiencia
        for (size_t i = 0; i < n; ++i) {
            b[i] = std::move(a[i]);
        }
        
        // 3. Pasa la propiedad de la nueva memoria al puntero principal 'a' y actualiza la capacidad
        a = std::move(b);
        cap = c;
    }

public:
    // Agrega un elemento en la parte superior de la pila
    void push(const T& x) {
        // Si el arreglo está lleno, duplica su capacidad (o inicia con capacidad 4 si cap == 0)
        if (n == cap) {
            resize(cap ? 2 * cap : 4);
        }
        // Inserta el nuevo elemento e incrementa el contador de elementos 'n'
        a[n++] = x;
    }

    // Elimina el elemento superior de la pila
    void pop() {
        assert(n > 0); // Precondición: la pila no debe estar vacía para poder eliminar
        --n;           // Decrementa la cantidad de elementos
        
        // Optimización de memoria: reduce la capacidad a la mitad si el uso baja al 25% (n <= cap/4)
        // Manteniendo una capacidad mínima de 4 elementos.
        if (cap > 4 && n <= cap / 4) {
            resize(cap / 2);
        }
    }

    // Retorna una referencia al elemento superior de la pila sin eliminarlo
    T& top() { 
        assert(n > 0); // Precondición: la pila no debe estar vacía
        return a[n - 1]; 
    }

    // Retorna 'true' si la pila está vacía, 'false' en caso contrario
    bool empty() const { 
        return n == 0; 
    }

    // Retorna el número actual de elementos en la pila
    size_t size() const { 
        return n; 
    }
};



//Explicación

//<cassert>: Permite usar assert(), que valida condiciones en tiempo de ejecución.
//<memory>: Proporciona std::unique_ptr, un puntero inteligente que gestiona la memoria automática.
//<utility>: Aporta std::move, que se usa para transferir valores en lugar de copiarlos.