from datos.repositorio_inventario import RepositorioInventario
from aplicacion.servicio_prestamos import ServicioPrestamos
from presentacion.consola import Consola

def main():
    # 1. Se crea la capa de datos
    repositorio = RepositorioInventario()

    # 2. Se crea la capa de aplicación inyectandole los datos
    servicio = ServicioPrestamos(repositorio)

    # 3. Se crea la capa de presentación inyectándole la de aplicación
    consola = Consola(servicio)

    # 4. Ejecución del programa
    print("Iniciando Sistema de Préstamos - Equipo 1 (Arquitectura en Capas)")
    consola.ejecutar_casos_de_prueba()

if __name__ == "__main__":
    main()
