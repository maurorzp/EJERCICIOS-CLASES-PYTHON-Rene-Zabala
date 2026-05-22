# =============================================================================
# TAREA SEMANA 3 - PYTHON
# Autor: Rene Mauricio Zabala Procel
# Tema: Condicionales, bucles for, controles de bucle, while e integrador
# Archivo solicitado: tarea_semana3.py
# =============================================================================


# =============================================================================
# PARTE 1: CONDICIONALES
# =============================================================================

def ejercicio_1_1():
    """Es el protocolo seguro o inseguro?"""
    print("\n--- Ejercicio 1.1: Protocolo seguro ---")

    protocolo = "HTTPS"

    if protocolo == "HTTPS" or protocolo == "SSH" or protocolo == "SFTP" or protocolo == "FTPS":
        print(f"El protocolo {protocolo} es SEGURO")
    elif protocolo == "HTTP" or protocolo == "Telnet" or protocolo == "FTP":
        print(f"El protocolo {protocolo} es INSEGURO")
    else:
        print(f"El protocolo {protocolo} es DESCONOCIDO")


def ejercicio_1_2():
    """Categorizar uso de CPU."""
    print("\n--- Ejercicio 1.2: Uso de CPU ---")

    uso_cpu = 85

    print(f"Uso de CPU: {uso_cpu}%")

    if uso_cpu < 50:
        print("Estado: NORMAL")
    elif uso_cpu < 80:
        print("Estado: ADVERTENCIA - monitorear")
    elif uso_cpu < 95:
        print("Estado: CRITICO - revisar procesos")
    else:
        print("Estado: EMERGENCIA - intervenir YA")


def ejercicio_1_3():
    """Tipo de puerto segun rango TCP/UDP."""
    print("\n--- Ejercicio 1.3: Tipo de puerto ---")

    puerto = 8080

    if puerto < 0 or puerto > 65535:
        print(f"Puerto {puerto}: Puerto INVALIDO")
    elif puerto <= 1023:
        print(f"Puerto {puerto}: Puerto bien conocido")
    elif puerto <= 49151:
        print(f"Puerto {puerto}: Puerto registrado")
    else:
        print(f"Puerto {puerto}: Puerto dinamico/privado")


def ejercicio_1_4():
    """Control de acceso por horario."""
    print("\n--- Ejercicio 1.4: Control de acceso ---")

    rol = "admin"
    hora_actual = 10
    cuenta_bloqueada = False

    if cuenta_bloqueada:
        print("Acceso denegado - cuenta bloqueada")
    elif rol != "admin":
        print("Acceso denegado - rol sin privilegios")
    elif hora_actual < 8 or hora_actual > 18:
        print("Acceso denegado - fuera del horario permitido")
    else:
        print("Acceso permitido")


def ejercicio_1_5():
    """Clase de IP segun primer octeto."""
    print("\n--- Ejercicio 1.5: Clase de IP ---")

    primer_octeto = 192

    if primer_octeto == 127:
        print(f"Octeto {primer_octeto} -> Loopback")
    elif primer_octeto <= 0 or primer_octeto > 255:
        print(f"Octeto {primer_octeto} -> Octeto invalido")
    elif primer_octeto <= 126:
        print(f"Octeto {primer_octeto} -> Clase A")
    elif primer_octeto <= 191:
        print(f"Octeto {primer_octeto} -> Clase B")
    elif primer_octeto <= 223:
        print(f"Octeto {primer_octeto} -> Clase C")
    elif primer_octeto <= 239:
        print(f"Octeto {primer_octeto} -> Clase D (Multicast)")
    else:
        print(f"Octeto {primer_octeto} -> Clase E (Experimental)")


# =============================================================================
# PARTE 2: BUCLE FOR
# =============================================================================

def ejercicio_2_1():
    """Listar IPs de la subred 192.168.1.0/29."""
    print("\n--- Ejercicio 2.1: IPs de una subred ---")

    for host in range(8):
        print(f"192.168.1.{host}")


def ejercicio_2_2():
    """Imprimir cada dispositivo con un guion delante."""
    print("\n--- Ejercicio 2.2: Inventario ---")

    dispositivos = [
        "Router Cisco 2901",
        "Switch HP ProCurve",
        "Firewall Fortinet",
        "Access Point Ubiquiti",
        "Servidor Dell PowerEdge",
    ]

    for dispositivo in dispositivos:
        print(f"- {dispositivo}")


def ejercicio_2_3():
    """Contar activos vs inactivos."""
    print("\n--- Ejercicio 2.3: Estado de dispositivos ---")

    estados = [
        "activo", "activo", "inactivo", "activo", "inactivo",
        "activo", "activo", "inactivo", "activo", "activo"
    ]

    activos = 0
    inactivos = 0

    for estado in estados:
        if estado == "activo":
            activos += 1
        else:
            inactivos += 1

    print(f"Dispositivos activos: {activos}")
    print(f"Dispositivos inactivos: {inactivos}")
    print(f"Total: {len(estados)}")


def ejercicio_2_4():
    """Listado numerado con enumerate."""
    print("\n--- Ejercicio 2.4: Listado numerado ---")

    hosts = ["servidor-web", "servidor-bd", "servidor-mail", "servidor-dns"]

    for numero, host in enumerate(hosts, start=1):
        print(f"Host {numero}: {host}")


def ejercicio_2_5():
    """Emparejar IP con hostname usando zip."""
    print("\n--- Ejercicio 2.5: Tabla IP-Hostname ---")

    ips = ["10.0.0.1", "10.0.0.2", "10.0.0.3", "10.0.0.4"]
    nombres = ["gateway", "dns", "web", "mail"]

    print("IP Hostname")
    print("-" * 30)

    for ip, nombre in zip(ips, nombres):
        print(f"{ip} {nombre}")


# =============================================================================
# PARTE 3: CONTROLES DE BUCLE
# =============================================================================

def ejercicio_3_1_break():
    """break: detenerse en el primer puerto cerrado."""
    print("\n--- Ejercicio break: Primer puerto cerrado ---")

    puertos = [21, 22, 23, 25, 80, 443]
    estado_puertos = ["abierto", "abierto", "abierto", "cerrado", "abierto", "abierto"]

    for puerto, estado in zip(puertos, estado_puertos):
        if estado == "cerrado":
            print(f"Primer puerto cerrado encontrado: {puerto}")
            print("(deteniendo escaneo)")
            break
        print(f"Puerto {puerto}: {estado}")


def ejercicio_3_2_continue():
    """continue: saltar IPs de la blacklist."""
    print("\n--- Ejercicio continue: Filtrar blacklist ---")

    ips_log = [
        "10.0.0.5", "200.0.0.1", "10.0.0.8", "45.33.32.156",
        "10.0.0.9", "200.0.0.1", "10.0.0.10"
    ]
    ips_blacklist = ["200.0.0.1", "45.33.32.156"]

    procesadas = 0
    saltadas = 0

    for ip in ips_log:
        if ip in ips_blacklist:
            saltadas += 1
            continue

        print(f"Procesando: {ip}")
        procesadas += 1

    print(f"\nIPs procesadas: {procesadas}")
    print(f"IPs saltadas: {saltadas}")


def ejercicio_3_3_else():
    """else del for: reportar no encontrado sin bandera auxiliar."""
    print("\n--- Ejercicio else: Buscar dispositivo ---")

    inventario = [
        "Router-01", "Switch-A", "Firewall-FW1",
        "Switch-B", "Servidor-Web", "Access-Point-1"
    ]
    buscar = "Firewall-FW1"

    for posicion, dispositivo in enumerate(inventario):
        if dispositivo == buscar:
            print(f"Encontrado en posicion {posicion}: {dispositivo}")
            break
    else:
        print("No encontrado en el inventario")


def ejercicio_3_4_pass():
    """pass: placeholder para usuarios que aun no procesaremos."""
    print("\n--- Ejercicio pass: Placeholder ---")

    usuarios = ["admin", "invitado", "root", "soporte"]

    for usuario in usuarios:
        if usuario == "root":
            pass
        else:
            print(f"Usuario procesado: {usuario}")


# =============================================================================
# PARTE 4: BUCLE WHILE
# =============================================================================

def ejercicio_4_1():
    """Cuenta regresiva de apagado."""
    print("\n--- Ejercicio 4.1: Cuenta regresiva ---")

    contador = 5

    while contador >= 1:
        print(f"Apagado en: {contador}")
        contador -= 1

    print("Apagando servidor...")


def ejercicio_4_2():
    """Decremento de bateria IoT."""
    print("\n--- Ejercicio 4.2: Bateria IoT ---")

    bateria = 100
    hora = 0

    while bateria >= 20:
        print(f"Hora {hora}: bateria al {bateria}%")
        bateria -= 15
        hora += 1

    print("ALERTA: bateria por debajo del umbral. Cargar dispositivo.")


def ejercicio_4_3():
    """Contar pings consecutivos exitosos hasta el primer fallo."""
    print("\n--- Ejercicio 4.3: Pings consecutivos ---")

    respuestas = [1, 1, 1, 1, 1, 1, 0, 1, 1, 0]
    indice = 0
    exitosos = 0

    while indice < len(respuestas) and respuestas[indice] == 1:
        exitosos += 1
        indice += 1

    print(f"Pings consecutivos exitosos: {exitosos}")

    if exitosos >= 5:
        print("Host estable (al menos 5 pings exitosos seguidos)")
    else:
        print("Host inestable")


def ejercicio_4_4():
    """Espera de respuesta con timeout."""
    print("\n--- Ejercicio 4.4: Espera con timeout ---")

    intentos_max = 6
    intento_con_respuesta = 4
    intento = 1
    respuesta_recibida = False

    while intento <= intentos_max and not respuesta_recibida:
        if intento == intento_con_respuesta:
            print(f"Intento {intento}: RESPUESTA RECIBIDA")
            respuesta_recibida = True
        else:
            print(f"Intento {intento}: sin respuesta")
        intento += 1

    if respuesta_recibida:
        print(f"Conexion exitosa en el intento {intento_con_respuesta}")
    else:
        print("Tiempo de espera agotado. No hubo respuesta.")


# =============================================================================
# PARTE 5: INTEGRADOR
# =============================================================================

def ejercicio_5_1():
    """Reporte de uso de ancho de banda."""
    print("\n--- Ejercicio 5.1: Ancho de banda ---")

    mb_por_hora = [
        20, 15, 18, 10, 5, 8,
        25, 60, 120, 150, 180, 200,
        195, 175, 140, 110, 95, 85,
        130, 145, 110, 70, 40, 25,
    ]

    total_mb = 0
    max_mb = 0
    hora_pico = 0
    horas_sobre_100 = 0

    for hora, mb in enumerate(mb_por_hora):
        total_mb += mb

        if mb > max_mb:
            max_mb = mb
            hora_pico = hora

        if mb > 100:
            horas_sobre_100 += 1

    print(f"Total del dia: {total_mb} MB")
    print(f"Hora pico: {hora_pico}:00 con {max_mb} MB")
    print(f"Horas con > 100 MB: {horas_sobre_100}")


def ejercicio_5_2():
    """Verificador simple de fortaleza de contrasena."""
    print("\n--- Ejercicio 5.2: Fortaleza contrasena ---")

    contrasena = "Ister2026"

    tiene_mayuscula = False
    tiene_numero = False

    for caracter in contrasena:
        if caracter.isupper():
            tiene_mayuscula = True
        if caracter.isdigit():
            tiene_numero = True

    if len(contrasena) < 8:
        print("Contrasena debil: longitud insuficiente")
    elif not tiene_mayuscula or not tiene_numero:
        print("Contrasena debil: falta mayuscula o numero")
    else:
        print("Contrasena valida")


def ejercicio_5_3():
    """Mini-escaner de hosts activos en red /29."""
    print("\n--- Ejercicio 5.3: Escaner de hosts ---")

    resultado_ping = [1, 1, 0, 1, 0, 0, 1, 0]

    activos = 0
    inactivos = 0

    for host, estado in enumerate(resultado_ping):
        ip = f"192.168.1.{host}"

        if estado == 1:
            print(f"{ip}: activo")
            activos += 1
        else:
            print(f"{ip}: inactivo")
            inactivos += 1

    total = len(resultado_ping)
    porcentaje_activos = (activos / total) * 100

    print(f"\nHosts activos: {activos} de {total} ({porcentaje_activos:.1f}%)")
    print(f"Hosts inactivos: {inactivos} de {total}")

    if porcentaje_activos < 50:
        print("ALERTA: red degradada")


# =============================================================================
# MENU PRINCIPAL
# =============================================================================

def main():
    print("=" * 70)
    print("TAREA SEMANA 3 - PYTHON")
    print("Condicionales, bucles for, controles, while e integrador")
    print("=" * 70)

    ejercicio_1_1()
    ejercicio_1_2()
    ejercicio_1_3()
    ejercicio_1_4()
    ejercicio_1_5()

    ejercicio_2_1()
    ejercicio_2_2()
    ejercicio_2_3()
    ejercicio_2_4()
    ejercicio_2_5()

    ejercicio_3_1_break()
    ejercicio_3_2_continue()
    ejercicio_3_3_else()
    ejercicio_3_4_pass()

    ejercicio_4_1()
    ejercicio_4_2()
    ejercicio_4_3()
    ejercicio_4_4()

    ejercicio_5_1()
    ejercicio_5_2()
    ejercicio_5_3()

    print("\n" + "=" * 70)
    print("FIN DE LA TAREA SEMANA 3")
    print("=" * 70)


if __name__ == "__main__":
    main()
