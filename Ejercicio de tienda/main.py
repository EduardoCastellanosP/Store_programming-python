import modules.utils.validationes as vd
import modules.utils.option as op
import modules.utils.screencontrol as sc
import modules.utils.menu1 as mn
import modules.controller.addproducto as ad
import modules.controller.ventas as vt
import modules.controller.stock as st
## este ejercico es agregar tarea, modificar tarea, listar tarea, eliminar tarea y si se realizo salga un false y si no un true(todavia disponible)

#OTRO PORGRAMA
#lA IDEA ES REGISTRAR PRODUCTOS POR MEDIO DE CODIGOS DE BARRAS, EL PROGRAMA VA A PERMITIR REGITSRRA EL PRODUCTO CON EL CODIGO DE BARRAS, NOMBRE,M STCOK MINIMO, STOCK MAXIMO Y CANTIDAD ACTUAL
# VAMOS A REGISTRAR COMPRAS Y VENTAS, CUANDO SE REGISTRAR UN PRODUCTO EN UN SISTEMA EL STOCK DEBE ESTAR EN 0 Y 
# CUANDO SE REGISTRE EL PROGRAMA DEBE SER CAPAZ DE CREAR UN INVENTARIO, COMPRAS Y VENTAS, AL MOMENTO DE VENDER DEBE ESCANERAR EL CODIGO DE BARRAS 
# Y MOSTRARLA INFORMACION, DEL STCOK Y MIRAR SI LA CANTIDAD QUE ESTA DISPONIBLE DEBE.

def tienda():
    print(mn.menu)
    option= op.opciones()
    match option:
        case 1:
            sc.borrar_pantalla()
            ad.Addproducto()
            sc.pausar_pantalla()
        case 2:
            sc.borrar_pantalla()
            vt.ventas()
            sc.pausar_pantalla()
        case 3:
            sc.borrar_pantalla()
            st.stock()
            sc.pausar_pantalla()
            


if __name__== "__main__"  :
    tienda()
