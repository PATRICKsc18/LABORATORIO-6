from crud_empleados import *

print("\n--- CREAR EMPLEADO ---")
id_nuevo = crear_empleado("Pedro", "Administrador", 3000)
print("ID creado:", id_nuevo)

print("\n--- LISTAR EMPLEADOS ---")
for emp in listar_empleados():
    print(emp)

print("\n--- ACTUALIZAR EMPLEADO ---")
actualizar_empleado(str(id_nuevo), {"sueldo": 3500})
print(obtener_empleado(str(id_nuevo)))

print("\n--- ELIMINAR EMPLEADO ---")
eliminar_empleado(str(id_nuevo))
print("Empleado eliminado")

print("\n--- EMPLEADOS POR CARGO ---")
for emp in empleados_por_cargo("Administrador"):
    print(emp)

print("\n--- EMPLEADOS CON SUELDO >= 2500 ---")
for emp in empleados_sueldo_minimo(2500):
    print(emp)

print("\n--- EMPLEADOS ORDENADOS POR SUELDO (ASC) ---")
for emp in empleados_ordenados_por_sueldo():
    print(emp)

print("\n--- TOP 3 SUELDOS ---")
for emp in empleados_top_sueldos(3):
    print(emp)
