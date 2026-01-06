# Mini Tienda en Consola

Este proyecto es un **mini sistema de tienda** en modo consola desarrollado en **Python**.  
Permite gestionar **productos, clientes, empleados y ventas**, con transacciones y pagos.

---

## Funcionalidades

1. Crear y listar **productos**  
2. Crear y listar **clientes**  
3. Crear y listar **empleados**  
4. Registrar y listar **ventas** (transaccionalidad: productos + clientes + empleados)  
5. Registrar y listar **pagos**  
6. Menú interactivo en consola con colores y validaciones  

---

## Cómo ejecutar

1. Clonar el repositorio:
```bash
git clone https://github.com/isrcastroes-oss/Mini-tienda
cd mini_tienda
```

2. Ejecutar el programa:
```bash
python main.py
```
3. Usar el menú para crear productos, clientes, empleados, registrar ventas y pagos.

Notas
- Todos los datos se manejan como listas de diccionarios en archivos JSON.
- Los IDs se asignan automáticamente usando archivos de contador (*_contador.txt).
- Validaciones de entrada incluidas para evitar errores.
- Menú interactivo con colores y mensajes claros.
