from pymongo import MongoClient

# PEGA AQUÍ TU CONNECTION STRING
uri = "mongodb+srv://rrromeroc_db_user:x7YMDSsHJGHuxjFa@cluster0.o3g5hpi.mongodb.net/Tienda?appName=Cluster0"

client = MongoClient(uri)

db = client["Tienda"]

print("Colecciones disponibles:")
print(db.list_collection_names())

print("\nDocumentos en empleados:")
for doc in db.empleados.find().limit(10):
    print(doc)
