class ServicioPrestamos:
    def __init__(self, repositorio):
        # Inyección de la dependencia de la capa de datos
        self.repositorio = repositorio

    def procesar_solicitud(self, estudiante, equipo, cantidad):
        inventario = self.repositorio.obtener_inventario()

        # Verificar si hay disponibilidad
        if equipo in inventario and inventario[equipo] >= cantidad:
            self.repositorio.actualizar_inventario(equipo, cantidad)
            estado = "Aprobada"
        else:
            estado = "Rechazada"

        self.repositorio.registrar_solicitud(estudiante, equipo, cantidad, estado)
        return estado

    def obtener_estado_inventario(self):
        return self.repositorio.obtener_inventario()

    def obtener_historial_solicitudes(self):
        return self.repositorio.obtener_solicitudes()
