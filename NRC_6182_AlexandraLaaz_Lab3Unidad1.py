class Cliente:
    list=[] #lista para los clientes
    def __init__(self,nombre, teléfono, estado):
        self.nombre=nombre
        self.teléfono=teléfono
        self.estado=estado
    #Método para el registro de una cuenta ene el sistema
    def registrarCuenta(self,correo,clave):
        print("REGISTRO DE CUENTA")
        self.nombre=str(input("**Ingrese su nombre : "))
        self.correo=str(input("**Ingrese correo electronico: "))
        self.clave=str(input("**Ingrese una clave: "))
    #Método para iniciar sesion en el sistema
    def Login(self,usuario):
        self.usuario=self.correo
        self.clave=self.nombre
        print("INICIO DE SESIÓN")
        usuario=str(input("Por favor ingrese el usurio: "))

    def registarseEnTienda(self,hora,fecha):
        self.hora=hora
        self.fecha=fecha

    def verHistorialVisitaTienda(self):
       self.hora=""
       self.fecha=""
    def verEstado(self, normal,caso,cercano):
        self.normal=normal
        self.caso=caso
        self.cercano=cercano


class Tienda():
    def __init__(self,Nombre,Telefono,Estado,Gerente):
        self.Nombre=Nombre
        self.Telefono=Telefono
        self.Estado=Estado
        self.Gerente=Gerente

#Reperesentara las caracteristicas de Cliente y Tienda
class Admin(Cliente,Tienda):
    def verCliente(self):
        self.VerCliente=[]
    def verTienda(self):
        self.VerTienda=[]
    def historialVisita(self):
        self.HistorialVisita=[]
    def cambiarEstado(self):    
        if self.estado == self.caso:
            print(Estado =self.caso)
            print(Contacto=self.cercano)