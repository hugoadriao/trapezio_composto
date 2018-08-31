#include <iostream>

using namespace std;

//Declaracao da equacao a ser utilizada
double func(double x){
    double f = 1/x;
    return f;
}
//Funca de solucao
double trapezios(double a, double b, int n){
    double h = (b-a)/n;
    double x[n];
    double soma = 0;
    double result = 0;
    x[0] = a + h;
    //Insere os valores no vetor e soma os valores na funcao
    for(int i = 1; i < n; i++){
        x[i] = x[i-1]+h;
        soma += func(x[i]);
    }
    result = (h/2)*(func(a)+2*(soma)+func(b));
    cout << result;
}
int main(){
    trapezios(1, 2, 1000);
    return 0;
}