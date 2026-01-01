from db import db
from bson.objectid import ObjectId


# ===== CREATE =====
def crear_empleado(nombre, cargo, sueldo):
    empleado = {
        "nombre": nombre,
        "cargo": cargo,
        "sueldo": sueldo
    }
    resultado = db.empleados.insert_one(empleado)
    return resultado.inserted_id


# ===== READ =====
def listar_empleados():
    return list(db.empleados.find())


def obtener_empleado(id_empleado):
    return db.empleados.find_one(
        {"_id": ObjectId(id_empleado)}
    )


# ===== UPDATE =====
def actualizar_empleado(id_empleado, nuevos_datos):
    return db.empleados.update_one(
        {"_id": ObjectId(id_empleado)},
        {"$set": nuevos_datos}
    )


# ===== DELETE =====
def eliminar_empleado(id_empleado):
    return db.empleados.delete_one(
        {"_id": ObjectId(id_empleado)}
    )

# ===== CONSULTAS Y FILTROS =====

# Filtrar empleados por cargo
def empleados_por_cargo(cargo):
    return list(
        db.empleados.find({"cargo": cargo})
    )


# Filtrar empleados con sueldo mayor o igual a un valor
def empleados_sueldo_minimo(sueldo_min):
    return list(
        db.empleados.find({"sueldo": {"$gte": sueldo_min}})
    )


# Listar empleados ordenados por sueldo
def empleados_ordenados_por_sueldo(ascendente=True):
    orden = 1 if ascendente else -1
    return list(
        db.empleados.find().sort("sueldo", orden)
    )


# Listar empleados ordenados y con límite
def empleados_top_sueldos(limite=5):
    return list(
        db.empleados.find()
        .sort("sueldo", -1)
        .limit(limite)
    )
