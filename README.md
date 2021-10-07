## Sistema de identificación con RFID y Reconocimiento Facial integrando servicios de Amazon Web Services...

### Introducción:
- <p> El proyecto nace con la necesidad de dar una solución que aporte fiabilidad en el proceso de identificación de empleados en la organización. Este sistema aprovecha los servicios que proporciona Amazon en su platafoma cloud. Uno de los servicios que cabe resaltar es el denominado Rekognition, el cual incorpora inteligencia artificial y permite la comparación de rostros con presición.</p>

![diagrama_aws.jpg](https://marvinorellana.s3.us-east-2.amazonaws.com/diagrama_aws.jpg?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLWVhc3QtMiJGMEQCIFA78q91BPnK4wAcZYm7PiZXxjVzKxpBmv1OEk9C0ZooAiBwgMqOmx69NTc4h5A9uC2XWrZIS%2BYZTjr%2FAbirJoZuLyr2Agh%2BEAAaDDg3NTM4NTU3NDQ2MSIMTL3zehWm32RfUBz1KtMCNqJISZvgjXc0AEm8bjeTl0Pl8TB3lX23FMZ4KPKehDrl6nzfh2DDpSuzQuX2l%2FYacQcrEND6F8YM72Y%2BQvoBvYc9Plov%2Ffs3XUPkUL1uh6rLnNp%2BHupYIK2MFYGeMH5d6Pah%2FbjQmJ1d82W294lDlsS68ZN%2F244WYDlMby4jMjXY4VKS7l%2ByEbs8z1yaRu65XFCH0T1EQ5%2FlKrvy02QaYKnWFxkkxZSgIXYgr1cluwJJK06WYCRF9t%2Ft6kcKR1UfRg5g0DuMe0H5X8Ex6mXjE5yH0Xd%2FTnODo6zW%2BA%2Ftx7BWxmJCgs%2FSSHueFt2QthHYnW2NwiQo3Ch6Yrn1CRoPwiBswQZPEBnFKXy2Vz2Tani9hx7MUX0JNn%2B4dYUFv3rFP5PHWACojbNeQ6l93ltS93kkj8uA85chJnoiiuaH9CgZV9ck1O3vHg7jVYRsovJRPIppMO6W%2BIoGOrQCV7ZBCc5HKhTMvRvUCGu%2FT2jndvDlTGVanUZxr6sIUMXymfpDpBW2b8VU4FLYWK3gC%2FMzgeGS7SaOQJaO7h%2FQC1Fh%2B%2BrKhan4qWarsdFIYLG7sfP%2FWmZcX5w5QUdQR%2FJ4B%2FhfYALHu9rtAlA%2BaZOExhCeqnXeFurBXzsQQFF13qdWeR%2BhEfeOH3S32pHyw8VNmR1E%2B0n8RkHV5APTr1AWT5B7WTtBu%2Fn5%2FN8cJyly7u6HJ6q42lTKu1z17PDaZUqkJUPtxTrEcTRUSngUKKtUM2zpBKl%2Bb4DUmscJcBckxzsHOX10MpjKVPAfM5SCgLVBqwB4Hl01twpLLTqA0RqCpba9pMuBsQwLu2csFDWIivUpo%2B%2F31G6f0ti9kDt2xzxOxKN6xaiy1B%2Blul%2BD9KcNE7wXJP8%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20211007T023045Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIA4XUIL2Q6VLY3IQNG%2F20211007%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Signature=e75a2b40da1d4fe58886b59c42e2813d97cf1ee488bdfea2a4f4d7cb5c6742a7 "diagrama_aws.jpg")
<br>
<br>
### Requerimientos esenciales:
- Raspberry Pi 3 B+
- Lector de tarjetas RFID
- Camára para Raspberry Pi
- Cuenta Amazon Web Services

<br>

### Integración del Hardware
<br>

- **Raspberry Pi 3 B+**
<br>

La instalación del hardware inicia con nuestra Raspberry a la cual debemos instalar el sistema operativo Raspbian y posteriormente el SDK proporcionado para el acceso de nuestra micro computadora a los servicios de AWS.

| Configuración | Link |
| ------ | ------ |
| Raspberry Pi | https://youtu.be/u0wmwIORzO0|

<br>

### Integración de Servicios
<br>

- **IoT Core**
<br>
Crear el objeto en la nube es el paso principal en la configuración de servicios. Por medio de el es que se lleva a cabo la comunicación entre el código Phyton úbicado en el archivo .py en el directorio raiz de Raspberry.

| Configuración | Nombre Archivo / Link |
| ------ | ------ |
| Código| PrincipalCodeFunction.py|
| Código| IoTObjectPolicy.py|
| IoT Core | https://youtu.be/TasSkcb5ttg |

![IoT_aws1.jpg](https://marvinorellana.s3.us-east-2.amazonaws.com/IoT_aws1.jpg?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLWVhc3QtMiJGMEQCIFA78q91BPnK4wAcZYm7PiZXxjVzKxpBmv1OEk9C0ZooAiBwgMqOmx69NTc4h5A9uC2XWrZIS%2BYZTjr%2FAbirJoZuLyr2Agh%2BEAAaDDg3NTM4NTU3NDQ2MSIMTL3zehWm32RfUBz1KtMCNqJISZvgjXc0AEm8bjeTl0Pl8TB3lX23FMZ4KPKehDrl6nzfh2DDpSuzQuX2l%2FYacQcrEND6F8YM72Y%2BQvoBvYc9Plov%2Ffs3XUPkUL1uh6rLnNp%2BHupYIK2MFYGeMH5d6Pah%2FbjQmJ1d82W294lDlsS68ZN%2F244WYDlMby4jMjXY4VKS7l%2ByEbs8z1yaRu65XFCH0T1EQ5%2FlKrvy02QaYKnWFxkkxZSgIXYgr1cluwJJK06WYCRF9t%2Ft6kcKR1UfRg5g0DuMe0H5X8Ex6mXjE5yH0Xd%2FTnODo6zW%2BA%2Ftx7BWxmJCgs%2FSSHueFt2QthHYnW2NwiQo3Ch6Yrn1CRoPwiBswQZPEBnFKXy2Vz2Tani9hx7MUX0JNn%2B4dYUFv3rFP5PHWACojbNeQ6l93ltS93kkj8uA85chJnoiiuaH9CgZV9ck1O3vHg7jVYRsovJRPIppMO6W%2BIoGOrQCV7ZBCc5HKhTMvRvUCGu%2FT2jndvDlTGVanUZxr6sIUMXymfpDpBW2b8VU4FLYWK3gC%2FMzgeGS7SaOQJaO7h%2FQC1Fh%2B%2BrKhan4qWarsdFIYLG7sfP%2FWmZcX5w5QUdQR%2FJ4B%2FhfYALHu9rtAlA%2BaZOExhCeqnXeFurBXzsQQFF13qdWeR%2BhEfeOH3S32pHyw8VNmR1E%2B0n8RkHV5APTr1AWT5B7WTtBu%2Fn5%2FN8cJyly7u6HJ6q42lTKu1z17PDaZUqkJUPtxTrEcTRUSngUKKtUM2zpBKl%2Bb4DUmscJcBckxzsHOX10MpjKVPAfM5SCgLVBqwB4Hl01twpLLTqA0RqCpba9pMuBsQwLu2csFDWIivUpo%2B%2F31G6f0ti9kDt2xzxOxKN6xaiy1B%2Blul%2BD9KcNE7wXJP8%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20211007T050449Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIA4XUIL2Q6VLY3IQNG%2F20211007%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Signature=fa9606eb5e07a17d02409c616d3e67c977c24f3aa4a823f1105c96925042d305 "IoT_aws1.jpg")

<br>

- **Bucket S3**
<br>
Se debe crear una carpeta con las fotografías de los perfiles a identificar. Cada imagen debe tener como nombre el código de la tarjeta RFID a asignar. 

| Configuración | Nombre Archivo / Link |
| ------ | ------ |
| Amazon S3 | https://youtu.be/TasSkcb5ttg |
| Código | BucketPrincipalPolicy.py |

![S3_aws.jpg](https://marvinorellana.s3.us-east-2.amazonaws.com/S3_aws.jpg?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLWVhc3QtMiJGMEQCIFA78q91BPnK4wAcZYm7PiZXxjVzKxpBmv1OEk9C0ZooAiBwgMqOmx69NTc4h5A9uC2XWrZIS%2BYZTjr%2FAbirJoZuLyr2Agh%2BEAAaDDg3NTM4NTU3NDQ2MSIMTL3zehWm32RfUBz1KtMCNqJISZvgjXc0AEm8bjeTl0Pl8TB3lX23FMZ4KPKehDrl6nzfh2DDpSuzQuX2l%2FYacQcrEND6F8YM72Y%2BQvoBvYc9Plov%2Ffs3XUPkUL1uh6rLnNp%2BHupYIK2MFYGeMH5d6Pah%2FbjQmJ1d82W294lDlsS68ZN%2F244WYDlMby4jMjXY4VKS7l%2ByEbs8z1yaRu65XFCH0T1EQ5%2FlKrvy02QaYKnWFxkkxZSgIXYgr1cluwJJK06WYCRF9t%2Ft6kcKR1UfRg5g0DuMe0H5X8Ex6mXjE5yH0Xd%2FTnODo6zW%2BA%2Ftx7BWxmJCgs%2FSSHueFt2QthHYnW2NwiQo3Ch6Yrn1CRoPwiBswQZPEBnFKXy2Vz2Tani9hx7MUX0JNn%2B4dYUFv3rFP5PHWACojbNeQ6l93ltS93kkj8uA85chJnoiiuaH9CgZV9ck1O3vHg7jVYRsovJRPIppMO6W%2BIoGOrQCV7ZBCc5HKhTMvRvUCGu%2FT2jndvDlTGVanUZxr6sIUMXymfpDpBW2b8VU4FLYWK3gC%2FMzgeGS7SaOQJaO7h%2FQC1Fh%2B%2BrKhan4qWarsdFIYLG7sfP%2FWmZcX5w5QUdQR%2FJ4B%2FhfYALHu9rtAlA%2BaZOExhCeqnXeFurBXzsQQFF13qdWeR%2BhEfeOH3S32pHyw8VNmR1E%2B0n8RkHV5APTr1AWT5B7WTtBu%2Fn5%2FN8cJyly7u6HJ6q42lTKu1z17PDaZUqkJUPtxTrEcTRUSngUKKtUM2zpBKl%2Bb4DUmscJcBckxzsHOX10MpjKVPAfM5SCgLVBqwB4Hl01twpLLTqA0RqCpba9pMuBsQwLu2csFDWIivUpo%2B%2F31G6f0ti9kDt2xzxOxKN6xaiy1B%2Blul%2BD9KcNE7wXJP8%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20211007T051121Z&X-Amz-SignedHeaders=host&X-Amz-Expires=299&X-Amz-Credential=ASIA4XUIL2Q6VLY3IQNG%2F20211007%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Signature=fcfa22975b660acef67ceacccd0d6e338dadffc0282bfed6ab73404e6933b726 "S3_aws.jpg")

```sh
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
```

<br>

- **Función Lambda**
<br>
Crear la función Lambda es parte fundamental de la integración de servicios, debido a que esta se activa cuando sucede el evento de carga en S3, posteriormente llama y envia datos al resto de servicios (Rekognition y RDS).

| Configuración | Nombre Archivo / Link |
| ------ | ------ |
| Amazon S3 | https://youtu.be/2FLe4vf-6Mc |
| Código | LambdaFunction.py |



- 
