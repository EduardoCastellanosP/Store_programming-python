import modules.utils.option as op
import modules.utils.menu1 as mn
import modules.utils.screencontrol as sc
import modules.utils.validationes as vd
import json
import modules.utils.corefiles as cf
from modules.utils.validationes import sololetras as sl, solonumeros as sn

DB_FILE="data/tienda.json"


def stock():
        with open(DB_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        print(""" ""
        _____________________
        Stock Disponible
        _____________________
            
            """)

        for categoria, elementos in data.items():
            for elemento in elementos:
                 print(f"Producto: {elemento['Producto']} - Stock: {elemento['Cantidad Existente']}")
        sc.pausar_pantalla()
        
                    
