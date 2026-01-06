from clases.pago import registrar_pago, listar_pagos

while True:
    print("""
    1. Crear producto
    2. Listar productos
    3. Crear cliente
    4. Listar clientes
    5. Crear empleado
    6. Listar empleados
    7. Registrar venta
    8. Listar ventas
    9. Registrar pago
    10. Listar pagos
    11. Salir
    """)

    opcion = input("Opción: ").strip()

    if opcion == "9":
        registrar_pago()
    elif opcion == "10":
        listar_pagos()
