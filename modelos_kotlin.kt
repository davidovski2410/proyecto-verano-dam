// En Kotlin una 'data class' genera automaticamente getters, setters, toString() y equals()
data class Tarea(
val id: Int
val titulo: String,
val completada: Boolean = false

)


fun main(){
//Lista de tareas (listOf es inmutable)
val listaTareas = mutableListOf(
Tarea(1, "Repasar Git y Github", true)
Tarea(2, "Aprender sintaxis de Python", true)
Tarea(3, "Dominar Kotlin para Android", false)
)

println("--- LISTA DE TAREAS PENDIENTES ---")
// Filtrar e iterar en Kotlin es super directo
val pendientes = listaTareas.filter { !it.completada}
for (tarea in pendientes){
    println("[ID ${tarea.id}] ${tarea.titulo}")
}


}