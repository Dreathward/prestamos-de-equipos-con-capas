# Conclusión del equipo

Elegimos esta estructura porque el driver o preocupación principal era: separar las responsabilidades del sistema para que la interfaz de usuario no dependiera directamente del almacenamiento de datos. Esto facilita el mantenimiento y nos permitiría reemplazar la consola por una interfaz web en el futuro sin alterar la lógica de negocio ni el inventario.

A cambio, asumimos: la introducción de pasos adicionales, mayor cantidad de archivos y el riesgo de tener capas vacías o clases que actúan como simples intermediarios sin aportar lógica compleja, lo cual aumenta la complejidad inicial del proyecto frente a un código tradicional en un solo archivo.
