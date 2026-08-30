
//Una biblioteca comunitaria presta 3 recursos (computadores, video webcam, sala) durante 5 dias. Se quiere saber cuánto se usó cada recurso y que tan cargado estuvo cada dia



#include <iostream>

using namespace std;

int main(){
    
    int matriz_recursos[3][5] = {
        {3,5,6,7,8},
        {12,3,5,10,5},
        {12,6,4,11,6},
    };
    
    //Declaraciónde variables
    
    int sumaCompu=0;
    int sumaVideoWebCam=0;
    int sumaSala=0;
    
    //Ciclo de recorrido para calcular recursos
    
    for (int i = 0; i < 3; i++){
        for (int j = 0; j < 5; j++){
            if(i == 0){ sumaCompu += matriz_recursos[i][j];}
            else if (i==1) {sumaVideoWebCam += matriz_recursos[i][j];}
            else if (i==2){sumaSala += matriz_recursos[i][j];}
        }
    }
    
    //Ciclo de recorrido para calcular el dia más "pesado"
    
    
    //Ciclo para las COLUMNAS
    for (int j = 0; j < 5; j++) {
        int sumaDia = 0; // Se reinicia en 0 para cada nuevo día

    // Ciclo de adentro para las FILAS
        for (int i = 0; i < 3; i++) {
            sumaDia += matriz_recursos[i][j];
    }

        cout << "Uso total del dia " << j + 1 << ": " << sumaDia << endl;
    }  
    
    
    //Cantidad de recursos usados
    
    cout << "Total Computadores: " << sumaCompu << endl;
    cout << "Total Webcams: " << sumaVideoWebCam << endl;
    cout << "Total Sala: " << sumaSala << endl;
    
  
return 0;}
