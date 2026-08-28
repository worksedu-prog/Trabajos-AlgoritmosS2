//RETO III  ·  Rotar el plano 90 grados   
//Contexto: Un mapa de zonas de reciclaje está guardado como matriz, pero se necesita imprimirlo girado para que coincida con la orientación real del barrio.
//Se pide: Escribir una función que reciba una matriz de f filas por c columnas y devuelva una nueva matriz rotada 90 grados en sentido horario. Verificar que {{1,2,3},{4,5,6}} produce {{4,1},{5,2},{6,3}}.
//Pista: La matriz resultante tiene c filas y f columnas: las dimensiones se intercambian. El elemento de la posición (i,j) termina en la posición (j, f-1-i).






#include <iostream>

using namespace std;


int main(){
    
    //Crear y declarar la matriz
    
    int MatrizPrincipal[2][3]={
        {1,2,3},
        {4,5,6},
    };
    
    int NuevaMatriz[3][2]; //declarar la nueva matriz
    
    
    //Recorre la matriz MatrizPrincipal
    for(int i = 0; i < 2; i++){
        for (int j = 0; j < 3; j++){
            NuevaMatriz[j][2 - 1-i] = MatrizPrincipal[i][j];
        }
    }
    
    //Recorre NuevaMatriz
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 2; j++){
            cout << NuevaMatriz[i][j] << " "; //Imprime la nueva matriz
        }
        cout<<endl;  //Para tener una parecido más visual a una matriz
    }
    
    
    
return 0;}
