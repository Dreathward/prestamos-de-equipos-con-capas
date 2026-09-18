# Sistema de Préstamos de Equipos - Equipo 1

## Diagrama de Arquitectura en Capas

```mermaid
graph TD
    Main[<b>main.py</b><br>Composición y Ejecución] --> Pres

    subgraph Capas
        Pres[<b>Capa de Presentación</b><br>consola.py<br><i>Solicita/muestra datos</i>] --> App
        App[<b>Capa de Aplicación</b><br>servicio_prestamos.py<br><i>Lógica de negocio (Aprobar/Rechazar)</i>] --> Dat
        Dat[<b>Capa de Datos</b><br>repositorio_inventario.py<br><i>Almacenamiento en memoria</i>]
    end

    style Main fill:#f9f9f9,stroke:#333,stroke-width:2px
    style Pres fill:#d4edda,stroke:#28a745,stroke-width:2px
    style App fill:#cce5ff,stroke:#007bff,stroke-width:2px
    style Dat fill:#fff3cd,stroke:#ffc107,stroke-width:2px
