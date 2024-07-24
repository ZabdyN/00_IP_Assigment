import os

#Diccionario de Áreas, Personal e IP's del MAP

coordinaciones = {
    "Atención al Público" : {
        "C. Atención al Público" : "10.45.31.11",
        "Centro de Documentación" : "10.45.31.12",
        "Talleres" : "10.45.31.13",
        "Servicios Educativos" : "10.45.31.14",
        "Aux. de Serv. Educativos" : "10.45.31.15",
        "Taquilla 1" : "10.45.31.21",#revisar
        "Taquilla 2" : "10.45.31.22",#revisar
        "Registro" : "10.45.31.5"
    },
    "Dirección General" : {
        "Director General" : "10.45.31.26",
        "Secretaria Dir. General" : "10.45.31.27",
        "Aux. Secretaria Dir. General" : "10.45.31.28"
    },
    "Administración" : {
        "C. Administración" : "10.45.31.31",
        "Aux. de Administración" : "10.45.31.32",
        "Contador" : "10.45.31.33",
        "Aux. Contabilidad" : "10.45.31.34",
        "Aux. Contabilidad 2" : "10.45.31.35",
        "Abogado" : "10.45.31.36",
        "Presupuestos" : "10.45.31.37",
        "Marco admin" : "10.45.31.40"        
    },
    "Seguridad y Custodia" : {
        "C. Seguridad y Custodia" : "10.45.31.41",
        "Monitores 6" : "10.45.31.44",
        "Monitores 1" : "10.45.31.45",
        "Monitores 2" : "10.45.31.46",
        "Monitores 3" : "10.45.31.47",
        "Monitores 4" : "10.45.31.48",
        "Monitores 5" : "10.45.31.49",
        "Servidor Monitores" : "10.45.31.50"
    },
    "Dirección de Operaciones" : {
        "C. Directora de Operaciones" : "10.45.31.51",
        "Aux. Dirección de Operaciones" : "10.45.31.52",
        "Alebrijes" : "10.45.31.53",
        "OTF MAP" : "10.45.31.54"
    },
    "Exposiciones" : {
        "C. Exposiciones" : "10.45.31.56",
        "Aux. Exposiciones" : "10.45.31.57",
        "Bodega" : "10.45.31.58"
    },
    "Museografía" : {
        "C. Museografía" : "10.45.31.61",
        "Aux. Museografía" : "10.45.31.62",
        "Aux. Museografía 2" : "10.45.31.63",
        "Workstation" : "10.45.31.64",
        "Mac Museografía" : "10.45.31.65"
    },
    "Conservación y Mantenimiento" : {
        "C. Conservación y Mantenimiento" : "10.45.31.71",
        "Jefe de Servicios" : "10.45.31.72",
        "Aux. Mantenimiento" : "10.45.31.73"
    },
    "Comunicación Social" : {
        "C. Comunicación Social" : "10.45.31.76",
        "Aux. Comunicación Social" : "10.45.31.77"
    },
    "Informática y Diseño" : {
        "C. Informática y Diseño" : "10.45.31.81",
        "Aux. Informática y Diseño" : "10.45.31.83",
        "Multimedia" : "10.45.31.84",
        "Diseño 1" : "10.45.31.85",
        "Diseño 2" : "10.45.31.86",
        "Diseño 1 PC" : "10.45.31.87",
        "Diseño 2 PC" : "10.45.31.88",
        
    }
}

#Muestra las coordinaciones enumerando los keys de nuestro directorio y devuelve las areas
def mostrar_areas():
   areas = list(coordinaciones.keys())
   for i, area in enumerate(areas, 1):
       print(f"{i}. {area}")
   return areas

#Muestra los empleados por coordinacion
def mostrar_emp(area):
    empleados = list(coordinaciones[area].keys())
    for i, empleado in enumerate(empleados, 1):
        print(f"{i}. {empleado}")
    return empleados

#Obtiene Ip's
def obtener_ip(area, empleado):
    return coordinaciones[area].get(empleado, "IP no encontrada")

def cambiar_ip(ip_static):
    comando_ip = f'netsh interface ip set address name="Ethernet" static {ip_static} 255.255.255.0 10.45.31.126'
    comando_dns = 'netsh interface ip set dns name="Ethernet" static 1.1.1.1'
    
    os.system(comando_ip)
    os.system(comando_dns)



def main():
    #Mostrar las coordinaciones y selecciona 1
    print("Selecciona la coordinación:\n")
    areas = mostrar_areas()
    area_index = int(input("\nIngresa el número de la coordinación: ")) - 1
    area = areas[area_index]
    #
    # Muestra los empleados y selecciona 1
    #
    print(f"\nSelecciona el empleado de la coordinación {area}: ")
    empleados = mostrar_emp(area)
    empleado_index = int(input("\nIngresa el número de empleado: ")) - 1
    empleado = empleados[empleado_index]
    #
    #Obtiene la IP y ejecuta el código para el cambio
    #
    ip_static = obtener_ip(area,empleado)
    if ip_static != "IP no encontrada":
        #cambiar_ip(ip_static)
        print(f"La IP ha sido cambiada por: {ip_static}")
        
    else: print(ip_static)
    
    
if __name__ == "__main__":
    main()