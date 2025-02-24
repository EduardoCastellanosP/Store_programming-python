
import modules.utils.option as op
import modules.utils.menu1 as mn
import modules.utils.screencontrol as sc
import modules.utils.validationes as vd
import json
import modules.utils.corefiles as cf
from modules.utils.validationes import sololetras as sl, solonumeros as sn
DB_FILE="data/tienda.json"

def Addproducto():
    while True:
        print(mn.menu)
        sc.pausar_pantalla()
        option=op.opciones()
        match option:
            case 1: 
                while True:
                    addproducto=sn("Ingrese el codigo de barras: ")
                    nameproducto=input("Ingrese el nombre del producto: ")
                    cantidadproducto=sn("Ingrese la cantidad de producto: ")
                    stockminimo=sn("Ingrese el stock minimo")
                    stockmaximo=sn("Ingrese el stock maximo")

                    tienda= {
                        "codigo":addproducto,
                        "Producto":nameproducto,
                        "Cantidad Existente":cantidadproducto,
                        "Stock Min":stockminimo,
                        "Stock Max": stockmaximo
                    }

                    cf.update_json(DB_FILE,tienda, ["Tienda"])
                    sc.borrar_pantalla()
                    otro=sl("desea registrar Otro producto S/N: ").upper()
                    if  otro != 'S':
                        break

                 


                

