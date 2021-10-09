from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import tinys3
import sys
import json
import loguer
import os
from datetime import datetime
import time
import picamera
import getopt
import RPi.GPIO as GPIO
import time


# Certificados de endpoint y aws
endpoint = "xxxxxxxx-ats-east-2.amazonaws.com"
Certificadoroot = "/CertificadoIoT"
Certificadocrt = "/CertificadoIoT.pem.crt"
CertificadoPrivado = "/CertificadoIoT.private.key"
try:
	opts, args = getopt.getopt(sys.argv[1:], "hwe:k:c:r:", ["help", "endpoint=", "key=","cert=","root="])
	if len(opts) == 0:
		raise getopt.GetoptError("Aqui no se ingresan parametros!")
	for sec, arg in opts:
		if sec in ("-h", "--help"):
			print(helpInfo)
			exit(0)
		if sec in ("-e", "--endpoint"):
			endpoint = arg
		if sec in ("-r", "--root"):
			Certificadoroot = arg
		if sec in ("-c", "--cert"):
			Certificadocrt = arg
		if sec in ("-k", "--key"):
			CertificadoPrivado = arg
except getopt.GetoptError:
	print(usageInfo)
	exit(1)

# Coprobación de parametros de credenciales del punto de acceso
MsnConf = False
if not endpoint:
	print("Msn '-e' or '--endpoint'")
	MsnConf = True
if not Certificadoroot:
	print("Msn '-r' or '--rootCA'")
	MsnConf = True
if not Certificadocrt:
    print("Msn '-c' or '--cert'")
    MsnConf = True
if not CertificadoPrivado:
    print("Msn '-k' or '--key'")
    MsnConf = True
if MsnConf:
	exit(2)

# Tamaño de la foto y formato
AnchoPi = 800
AltoPi = 600
ExtensionPi = '.jpg'

# Certificados descargados al crear el perfil de IAM en AWS
id_acceso = 'AKIA4XUIL2Q6XNDZXXX'
id_secret = 'HOLAWmb0Bt4Oc19mMJubtb9EJNTR3u0JWfIcXXXX'
bucket = 'sgp2021'

# Mapeo de caracteres para RFID
hid = { 4: 'a', 5: 'b', 6: 'c', 7: 'd', 8: 'e', 9: 'f', 10: 'g', 11: 'h', 12: 'i', 13: 'j', 14: 'k', 15: 'l', 16: 'm', 17: 'n', 18: 'o', 19: 'p', 20: 'q', 21: 'r', 22: 's', 23: 't', 24: 'u', 25: 'v', 26: 'w', 27: 'x', 28: 'y', 29: 'z', 30: '1', 31: '2', 32: '3', 33: '4', 34: '5', 35: '6', 36: '7', 37: '8', 38: '9', 39: '0', 44: ' ', 45: '-', 46: '=', 47: '[', 48: ']', 49: '\\', 51: ';' , 52: '\'', 53: '~', 54: ',', 55: '.', 56: '/'  }
hid2 = { 4: 'A', 5: 'B', 6: 'C', 7: 'D', 8: 'E', 9: 'F', 10: 'G', 11: 'H', 12: 'I', 13: 'J', 14: 'K', 15: 'L', 16: 'M', 17: 'N', 18: 'O', 19: 'P', 20: 'Q', 21: 'R', 22: 'S', 23: 'T', 24: 'U', 25: 'V', 26: 'W', 27: 'X', 28: 'Y', 29: 'Z', 30: '!', 31: '@', 32: '#', 33: '$', 34: '%', 35: '^', 36: '&', 37: '*', 38: '(', 39: ')', 44: ' ', 45: '_', 46: '+', 47: '{', 48: '}', 49: '|', 51: ':' , 52: '"', 53: '~', 54: '<', 55: '>', 56: '?'  }

# Configuración de logueo del cliente por medio del SDK
login = loguer.getLogger("AWSIoTPythonSDK.core")
login.setLevel(loguer.DEBUG)
strhan = loguer.StreamHandler()
frmat = loguer.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
strhan.setFormatter(frmat)
login.addHandler(strhan)

# Llamada a IoT por protocolo MQTT
ClientAWSMQTTIoT = None

ClientAWSMQTTIoT = AWSIoTMQTTClient("basicPubSub")
ClientAWSMQTTIoT.configureEndpoint(endpoint, 8883)
ClientAWSMQTTIoT.configureCredentials(Certificadoroot, CertificadoPrivado, Certificadocrt)

# Conexion y configuración de MQTT Client
ClientAWSMQTTIoT.configureAutoReconnectBackoffTime(2, 12, 10)
ClientAWSMQTTIoT.configureOfflinePublishQueueing(-1)
ClientAWSMQTTIoT.configureDrainingFrequency(2) 
ClientAWSMQTTIoT.configureConnectDisconnectTimeout(15) 
ClientAWSMQTTIoT.configureMQTTOperationTimeout(10) 

# Apertura de cámara al hacer llamado al metodo
opencam = picamera.PiCamera()
opencam.resolution = (AnchoPi, AltoPi)
opencam.awb_mode = 'auto'

 #Inicio de RFID donde Hidraw es necesario validar el numero 0,1,2,3 en el path
rf = open('/dev/hidraw3', 'rb')

def EsperandoRFID():
    ss = ""
    shift = False
    done = False
    while not done:
       buffer = rf.read(8)
       for c in buffer:
          if ord(c) > 0:
             if int(ord(c)) == 40:
                done = True
                break;
             if shift:
                if int(ord(c)) == 2 :
                   shift = True
                else:
                   ss += hid2[ int(ord(c)) ]
                   shift = False
             else:
                if int(ord(c)) == 2 :
                   shift = True
                else:
                   ss += hid[ int(ord(c)) ]
    return ss

def CargarS3(test):
    dirfile = /PhotosAWS/test + ExtensionPi
    opencam.capture(dirfile)
    conn = tinys3.Connection(id_acceso, id_secret)
    f = open(dirfile, 'rb')
    conn.upload(dirfile, f, bucket,
               headers={
               'x-amz-meta-cache-control': 'max-age=60'
               })
    if os.path.exists(dirfile):
        os.remove(dirfile)

# BCM para activar setear el estado de los pines
GPIO.setmode(GPIO.BCM)
# Poner GPIO 17 como OUTput
GPIO.setup(17, GPIO.OUT)
# Estado inicial pin 17 HIGH
GPIO.output(17, GPIO.HIGH)



# Resultado de la metadata traida por MQTT
def Validacion(client, userdata, message):
    print("Nuevo Mensaje Recibido: ")
    data = json.loads(message.payload)
    try:
        Sml = data[1][0]['Similaridad']
        print("Similaridad: " + str(Sml))
        if(Sml >= 90):
            # Poner pin 17 en LOW 
            GPIO.output(17, GPIO.LOW)
            # Tiempo del pulso
            time.sleep(0.5)
            # Volver a HIGH
            GPIO.output(17, GPIO.HIGH)
            # Limpiar
            GPIO.cleanup()
    except:
        pass
    print("Evento Finalizado.")

def verifRFIDNum(rfidnumber):
    return rfidnumber

# Subscripcion hacia el Objeto IoT creado en AWS
ClientAWSMQTTIoT.connect()
ClientAWSMQTTIoT.subscribe("sgp2021/solucion", 1, Validacion)
time.sleep(10)


# Ejecución del topic, publicado siempre para recibir n caantidad de tarjetas
while True:
    print("Esperando RFID..")
    captura = EsperandoRFID()
    print(captura)
    if(verifRFIDNum(captura)):
        print("RFID Correccto, Validar Foto...")
        CargaS3(captura)
    else:
        print("Acceso Denegado")