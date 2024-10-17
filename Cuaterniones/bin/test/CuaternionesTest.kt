import kotlin.test.Test
import kotlin.test.assertEquals

// Clase de pruebas unitarias
class CuaternionesTest {

    @Test // Calcula la suma de dos cuaterniones
    fun testCuaternionAddition() {
        val q1 = Cuaternion(1.0, 2.0, 3.0, 4.0)
        val q2 = Cuaternion(5.0, 6.0, 7.0, 8.0)
        val result = q1 + q2
        assertEquals(Cuaternion(6.0, 8.0, 10.0, 12.0), result)
    }

    @Test // Calcula la suma de un número a un cuaternion
    fun testCuaternionAdditionWithNumber() {
        val q1 = Cuaternion(1.0, 2.0, 3.0, 4.0)
        val result = q1 + 5.0
        assertEquals(Cuaternion(6.0, 2.0, 3.0, 4.0), result)
    }

    @Test // Calcula el producto de dos cuaterniones
    fun testCuaternionMultiplication() {
        val q1 = Cuaternion(1.0, 2.0, 3.0, 4.0)
        val q2 = Cuaternion(5.0, 6.0, 7.0, 8.0)
        val result = q1 * q2
        assertEquals(Cuaternion(-60.0, 12.0, 30.0, 24.0), result)
    }

    @Test // Calcula el producto de un número por un cuaternion
    fun testCuaternionMultiplicationWithNumber() {
        val q1 = Cuaternion(1.0, 2.0, 3.0, 4.0)
        val result = q1 * 2.0
        assertEquals(Cuaternion(2.0, 4.0, 6.0, 8.0), result)
    }

    @Test // Calcula el negativo de un cuaternion
    fun testCuaternionUnaryMinus() {
        val q1 = Cuaternion(1.0, 2.0, 3.0, 4.0)
        val result = -q1
        assertEquals(Cuaternion(1.0, -2.0, -3.0, -4.0), result)
    }

    @Test // Calcula la medida de un cuaternion
    fun testCuaternionNorm() {
        val q1 = Cuaternion(1.0, 2.0, 3.0, 4.0)
        val result = !q1
        assertEquals(Math.sqrt(30.0), result)
    }
}