//RETO II  ·  La diagonal secreta   
//Contexto: Un sistema sencillo de verificación usa las diagonales de una matriz cuadrada como código de control.
//Se pide: Dada una matriz cuadrada, calcular la suma de la diagonal principal y la de la diagonal secundaria, y determinar si son iguales. Probar con {{1,2,3},{4,5,6},{7,8,9}}.
//Pista: La diagonal principal son las posiciones donde fila e índice coinciden. Para la secundaria, cuando la fila avanza la columna retrocede: piensen en n-1-i.


#include <iostream>

using namespace std;

int main(){
    
    //Crear y declarar la matriz
    
    int MatrizPrincipal[3][3]={
        {1,2,3},
        {4,5,6},
        {7,8,9},
    };
    
    int sumaPrin=0;
    int sumaSecun=0;
    
    //Recorre las posiciones de la MatrizPrincipal
    
    for (int i = 0; i < 3; i++ ){
        sumaPrin += MatrizPrincipal[i][i];
        sumaSecun += MatrizPrincipal[i][2-i];
    };
    
    //Calculo de las suma de los números en las respectivas diagonales
    
    cout << "--- Suma de diagonales ---" << endl;
    
    cout << "Suma de la diagonal principal = " << sumaPrin << endl;
    cout << "Suma de la diagonal secundaria = " << sumaSecun << endl;
    
    
    //Verficar y afirmar o negar si las diagonales son iguales o no
    
    if (sumaPrin == sumaSecun){
        cout << "La diagonal principal y la secundaria son iguales" << endl;
    }
    else {cout << "La diagonal principal y secundario son distintas" << endl;}
    
    

return 0;}
