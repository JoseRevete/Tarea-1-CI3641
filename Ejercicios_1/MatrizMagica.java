public class MatrizMagica {
    // Método que recibe una matriz cuadrada y determina si es una matriz mágica.
    public static String matrizMagica(int[][] n) {
        if (n[0].length != n.length) {throw new IllegalArgumentException("La matriz debe ser cuadrada.");}
        int suma = 0;
        int previo = 0;

        // Se suman las filas y columnas de la matriz y se comparan con el valor de la primera fila.
        for (int i = 0; i < n.length; i++) {
            for (int j = 0; j < n.length; j++) {
                suma += n[i][j];
            }
            if (i == 0) {previo = suma;}
            else if (suma != previo) {return "No es una matriz mágica.";}
            else {previo = suma;}
            suma = 0;
        }
        for (int i = 0; i < n.length; i++) {
            for (int j = 0; j < n.length; j++) {
                suma += n[j][i];
            }
            if (i == 0) {previo = suma;}
            else if (suma != previo) {return "No es una matriz mágica.";}
            else {previo = suma;}
            suma = 0;
        }

        // Se suman las diagonales de la matriz y se comparan con el valor de la primera fila.
        for (int i = 0; i < n.length; i++) {
            suma += n[i][i];
        }
        if (suma != previo) {return "No es una matriz mágica.";}
        suma = 0;
        for (int i = 0; i < n.length; i++) {
            suma += n[i][n.length - i - 1];
        }
        if (suma != previo) {return "No es una matriz mágica.";}
        return "Es una matriz mágica.";
    }

    public static void main(String[] args) {
        System.out.println(matrizMagica(new int[][]{{-1, -1, -1}, {-1, -1, -1}, {-1, -1, -1}}));
    }
}
