public class PotenciaModulada {
    // Funcion para calcular el modulo de una potencia
    public static int potenciaModulada(int a, int b, int c) {
        // Chequeo de que a y b >= 0, y c >= 2
        if (a < 0 || b < 0 || c < 2) {throw new IllegalArgumentException("Los parámetros a y b deben ser mayores o iguales a 0. Y c debe ser mayor o igual a 2.");}
        int resultado;
        if (b == 0) {return 1;}
        else {resultado = ( (a%c) * potenciaModulada(a, b - 1, c) ) % c;}
        return resultado;
    }

    public static void main(String[] args) {
        System.out.println(potenciaModulada(72, 5 , 11));
    }
}