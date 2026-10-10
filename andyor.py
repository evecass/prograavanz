nombre_db = "" 

nombre_de_usuario = nombre_db or "usuario anonimo"
print (f"{nombre_de_usuario}")



nombre_db = "" 
rol_db = ""

nombre_de_usuario = nombre_db or "usuario anonimo"
rol_final = rol_db or "invitado"
print (f"{nombre_de_usuario}")







nombre_db = "" 
rol_db = ""
nivel_acceso = 1
cuenta_activa =True

nombre_de_usuario = nombre_db or "usuario anonimo"
rol_final = rol_db or "invitado"
acceso_permitido = nivel_acceso >=3 and cuenta_activa
print (f"{acceso_permitido=}")