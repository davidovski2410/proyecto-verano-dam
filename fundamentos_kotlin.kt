fun main(){
    // 'val' es inmutable (constante), 'var' es mutable
    val alumno: String = "David"
    var curso: String = "1º DAM"
    curso = "2º DAM"

    println("¡Hola! Soy $alumno y paso a $curso")

    // Estructura 'when' (sustituye al 'switch' de Java)
    val nota: Int = 8
    val estado = when (nota) {
        in 9..10 -> "Sobresaliente"
        in 8..7 -> "Notable"
        in 5..6 -> "Aprobado"
        else -> "Suspenso"
    }
    println("Nota: $nota ($estado)")


    // Null Safety : El signo '?' permite nulos, '?:' asigna valor por defecto
    var email: String? = null
    var emailMostrar = email ?: "correo_no_registrado@ejemplo.com"
    println("Email del alumno: $emailMostrar")
}