class RepositorioInventario:
    def __init__(self):
        # Inventario inicial según los datos mínimos requeridos
        self.inventario = {
            "Portátiles": 2,
            "Tabletas": 1
        }
        self.solicitudes = []

    def obtener_inventario(self):
        # Retorna una copia para evitar que otras capas lo modifiquen directamente
        return self.inventario.copy()

    def actualizar_inventario(self, equipo, cantidad):
        if equipo in self.inventario:
            self.inventario[equipo] -= cantidad

    def registrar_solicitud(self, estudiante, equipo, cantidad, estado):
        self.solicitudes.append({
            "estudiante": estudiante,
            "equipo": equipo,
            "cantidad": cantidad,
            "estado": estado
        })
        
    def obtener_solicitudes(self):
        return self.solicitudes
