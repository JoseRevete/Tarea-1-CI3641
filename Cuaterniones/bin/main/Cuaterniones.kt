data class Cuaternion(val a: Number, val b: Number, val c: Number, val d: Number) {
    // Sobre carga de operador suma para sumar dos cuaterniones (+)
    operator fun plus(other: Cuaternion): Cuaternion {
        return Cuaternion(
            this.a.toDouble() + other.a.toDouble(),
            this.b.toDouble() + other.b.toDouble(),
            this.c.toDouble() + other.c.toDouble(),
            this.d.toDouble() + other.d.toDouble()
        )
    }

    // Sobre carga de operador suma para sumar un número a un cuaternion (+)
    operator fun plus(other: Number): Cuaternion {
        return Cuaternion(
            this.a.toDouble() + other.toDouble(),
            this.b.toDouble(),
            this.c.toDouble(),
            this.d.toDouble()
        )
    }

    // Sobre carga de operador multiplicación para calcular el producto entre cuaterniones (*)
    operator fun times(other: Cuaternion): Cuaternion {
        val a = this.a.toDouble() * other.a.toDouble() - this.b.toDouble() * other.b.toDouble() - this.c.toDouble() * other.c.toDouble() - this.d.toDouble() * other.d.toDouble()
        val b = this.a.toDouble() * other.b.toDouble() + this.b.toDouble() * other.a.toDouble() + this.c.toDouble() * other.d.toDouble() - this.d.toDouble() * other.c.toDouble()
        val c = this.a.toDouble() * other.c.toDouble() - this.b.toDouble() * other.d.toDouble() + this.c.toDouble() * other.a.toDouble() + this.d.toDouble() * other.b.toDouble()
        val d = this.a.toDouble() * other.d.toDouble() + this.b.toDouble() * other.c.toDouble() - this.c.toDouble() * other.b.toDouble() + this.d.toDouble() * other.a.toDouble()
        return Cuaternion(a, b, c, d)
    }

    // Sobre carga de operador multiplicación para calcular el producto por un número (*)
    operator fun times(other: Number): Cuaternion {
        return Cuaternion(
            this.a.toDouble() * other.toDouble(),
            this.b.toDouble() * other.toDouble(),
            this.c.toDouble() * other.toDouble(),
            this.d.toDouble() * other.toDouble()
        )
    }

    // Sobre carga de operador resta para calcular el negativo (-)
    operator fun unaryMinus(): Cuaternion {
        return Cuaternion(this.a.toDouble(), -this.b.toDouble(), -this.c.toDouble(), -this.d.toDouble())
    }

    // Sobre carga de operador not para calcular la medida(!)
    operator fun not(): Double {
        return Math.sqrt(this.a.toDouble() * this.a.toDouble() + this.b.toDouble() * this.b.toDouble() + this.c.toDouble() * this.c.toDouble() + this.d.toDouble() * this.d.toDouble())
    }
}