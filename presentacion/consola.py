class Consola:
    def __init__(self, servicio):
        # Inyección de la dependencia de la capa de aplicación
        self.servicio = servicio

    def mostrar_inventario(self):
        inventario = self.servicio.obtener_estado_inventario()
        print("\n--- ESTADO DEL INVENTARIO ---")
        for equipo, cantidad in inventario.items():
            print(f"- {equipo}: {cantidad} disponibles")

    def procesar_entrada(self, estudiante, equipo, cantidad):
        print(f"\n[!] Nueva Solicitud: {estudiante} solicita {cantidad} {equipo}.")
        resultado = self.servicio.procesar_solicitud(estudiante, equipo, cantidad)
        print(f">>> Resultado de la solicitud: {resultado}")

    def mostrar_reporte_final(self):
        print("\n" + "="*30)
        print("REPORTE FINAL EJECUTADO")
        print("="*30)
        self.mostrar_inventario()

        print("\n--- SOLICITUDES PROCESADAS ---")
        solicitudes = self.servicio.obtener_historial_solicitudes()
        for s in solicitudes:
            print(f"- Estudiante: {s['estudiante']} | Equipo: {s['cantidad']} {s['equipo']} | Estado: {s['estado']}")
        print("="*30 + "\n")

    def ejecutar_casos_de_prueba(self):
        # Caso 1: Inventario inicial
        self.mostrar_inventario()

        # Caso 2: Solicitud aprobada
        self.procesar_entrada("Ana", "Portátiles", 1)

        # Caso 3: Solicitud rechazada
        self.procesar_entrada("Juan", "Tabletas", 2)

        # Caso 4: Reporte final
        self.mostrar_reporte_final()
