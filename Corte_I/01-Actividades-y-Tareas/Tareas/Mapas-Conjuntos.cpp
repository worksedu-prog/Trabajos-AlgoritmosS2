#include <iostream>
#include <map>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <set>
using namespace std;

int main(){
    unordered_set<string> categorias={"papel","lapiz","cuaderno"};
    cout<<categorias.count("papel")<<endl;

    unordered_map<string,int> indice;
    indice["REC-00042"] = 42;
    cout<<indice["REC-00042"]<<endl;

    std::map<string,int> indice2;
    std::set<string> categorias2={"papel","lapiz","cuaderno"};
    
}
