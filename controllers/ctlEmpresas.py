from models import mdlEmpresas

def ctlRegistroEmp(name,email,password,imagen,celular,direccion,descripcion):
    print('resgistrar')
    result = validarForm(name,email,password,imagen,celular,direccion,descripcion)
    print(result)
    if(result[0]):
        consulta = mdlEmpresas.registroEmpresa(name,email,password,imagen,celular,direccion,descripcion)
        return consulta
    else:
        return [False, result[1]]
    
def ctlEntrarEmp(email,password):
    result = validarContra(password)
    correo = validarCorreo(email)
    if(result[0] & correo[0]):
        consulta = mdlEmpresas.mdlEntrarEmp(email,password)
        return consulta
    else:
        return [False,correo[1]+"- "+result[1]]
        
def recuperarp(email,password):
    result = validarCorreo(email)
    
    if(result[0]):
        consulta = mdlEmpresas.recperarPASS(email,password)
        
def validarForm(name,email,password,imagen,celular,direccion,descripcion):
    print(name,email,password,imagen,celular,direccion,descripcion) 
    is_valid = True
    fls = ''
    if name =="":
        fls += ("es requerido el nombre")
        is_valid= False
    resEmail = validarCorreo(email)    
    if resEmail[0]==False:
        fls +=resEmail[1]
        is_valid= False
    resPass = validarContra(password)   
    if resPass[0]==False:
        fls +=resPass[1]
        is_valid= False
    
    if imagen =="":
        is_valid= False

    if celular =="":
        fls +=(" -es requerido el telefono")
        is_valid= False 

    if direccion =="":
        fls +=(" -es requerido la direccion")
        is_valid= False  
        
    if descripcion =="":
        fls +=(" -es requerida la descripcion")
        is_valid= False

    """if is_valid == False:
        print(" -los datos no son validos")
        return [is_valid,fls]
    else: """
    return [is_valid,fls]
    
def validarContra(password):
    bandera = True
    fls=''
    if password =="":
        fls= " -es requerido la contraseña"
        bandera = False
        
        
    return([bandera,fls])

def validarCorreo(correo):
    bandera = True
    fls=''
    
    if correo =='':
        fls = (' -Ingrese el correo')
        print("entro")
        bandera = False
    return([bandera,fls])
        