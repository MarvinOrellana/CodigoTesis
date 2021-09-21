#Esta politica es la principal del Bucket, debe ser creada en el ejecutor de politicas de AWS
#Servira para dar permisos de carga de archivos

{
    "Version": "2012-10-17",
    "Id": "Policy1631576198759",
    "Statement": [
        {
            "Sid": "Stmt1631576182257",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::875385574461:user/SGP2021"
            },
            "Action": "s3:PutObject",
            "Resource": "arn:aws:s3:::s3objeto/*"
        }
    ]
}