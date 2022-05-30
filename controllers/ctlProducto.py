from models import mdProductos

def ctlRegProduct(name, descripcion, precio, imagen):
    
    result = validarForm(name, descripcion, precio, imagen)
    if(result[0]):
        mdProductos.creaProd()
    else:
        return [False, result[1]]
    
def validarForm(name, descripcion, precio, imagen):
    is_valid= True
    fls = ""
    
    if name =="":
        fls += ("es requerido el nombre para el registro del producto")
        is_valid= False
        
    if descripcion =="":
        fls += ("es requerido la descripcion para el registro del producto")
        is_valid= False
        
    if precio =="":
        fls += ("es requerido el precio para el registro del producto")
        is_valid= False
    
    if imagen =="":
        is_valid= False

    return [is_valid, fls]