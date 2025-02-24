
import modules.utils.option as op
import modules.utils.menu1 as mn
import modules.utils.screencontrol as sc
import modules.utils.validationes as vd
import json
import modules.utils.corefiles as cf
from modules.utils.validationes import sololetras as sl, solonumeros as sn
DB_FILE="data/tienda.json"

def ventas():
   
            with open(DB_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)

            codigo=sn("Ingrese el codigo de barras del producto que desea comprar: ") # cada vez que se hace una venta se reduce el stock.
            cantidad=sn("Ingrese la cantidad que desea comprar: ")
        
            for categoria, elementos in data.items():
                for elemento in elementos:
                    if elemento['codigo'] == codigo:
                        if elemento['Cantidad Existente']>0:
                            elemento["Cantidad Existente"] -= cantidad
                            
                            with open(DB_FILE, "w", encoding="utf-8") as file: #Guardar cambios en el Json
                                json.dump(data, file, indent=4, ensure_ascii=False)
                            
                            print(f"Stock actualizado: {elemento['Producto']} ahora tiene {elemento['Cantidad Existente']} unidades.")
                            return True  # Indica que se actualizó correctamente
                        else:
                            print(f"No hay stock disponible para {elemento['Producto']}.")
                            return False  # No se pudo disminuir
            print("Código no encontrado.")
            return False  # Si no se encuentra el producto
   


                 

                        



