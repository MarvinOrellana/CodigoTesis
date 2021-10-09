from __future__ import print_function
import boto3
from decimal import Decimal
import json
import urllib
import mysql
import sys
import logging
import rds_config
import pymysql

print('Loading function')

#Conexion Base de Datos
endpoint = 'Punto de acceso base de datos RDS'
username = 'Usuario de IAM'
password = 'Password Usuario IAM'
database_name = 'databasesgp'

connection = pymysql.connect(endpoint, user=username,
            password=password, db=database_name)

rekognition = boto3.client('rekognition')
iot = boto3.client('iot-data')




# --------------- Llamado a la API de Rekognitión ------------------

def compare_faces(bucket, key, key_target, threshold=80):
	response = rekognition.compare_faces(
	    SourceImage={
			"S3Object": {
				"Bucket": bucket,
				"Name": key,
			}
		},
		TargetImage={
			"S3Object": {
				"Bucket": bucket,
				"Name": key_target,
			}
		},
	    SimilarityThreshold=threshold,
	)
	return response['SourceImageFace'], response['FaceMatches']

# --------------- Metodo Lambda para activación del evento ------------------


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key'].encode('utf8'))
    key_target = "target/" + key
    cursor = connection.cursor()
    cursor.execute('SELECT Codigo from Empleado')
    rows = cursor.fetchall()
    for row in rows:
        ln = ('{0}'.format(row[0]))
    if(key_target == ln): 
        response = compare_faces(bucket, key, key_target)
        print(response)
        mypayload = json.dumps(response)
        iotResponse = iot.publish(
            topic="sdk/test/python",
            qos=1,
            payload=mypayload)
        print(iotResponse)
        return iotResponse
    
