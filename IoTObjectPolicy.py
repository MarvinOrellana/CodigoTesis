#Politica ya existente de forma predeterminada en el Objeto IoT creado
#El unico cambio que hay que hacer, es agregar el topic sgp2021/solucion

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "iot:*",
        "iot:Publish",
        "iot:Receive",
        "iot:RetainPublish"
      ],
      "Resource": [
        "arn:aws:iot:us-west-1:875385574461:topic/sdk/test/java",
        "arn:aws:iot:us-west-1:875385574461:topic/sdk/test/Python",
        "arn:aws:iot:us-west-1:875385574461:topic/topic_1",
        "arn:aws:iot:us-west-1:875385574461:topic/topic_2",
        "arn:aws:iot:us-west-1:875385574461:topic/sgp2021/solucion"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "iot:Subscribe"
      ],
      "Resource": [
        "arn:aws:iot:us-west-1:875385574461:topicfilter/sdk/test/java",
        "arn:aws:iot:us-west-1:875385574461:topicfilter/sdk/test/Python",
        "arn:aws:iot:us-west-1:875385574461:topicfilter/topic_1",
        "arn:aws:iot:us-west-1:875385574461:topicfilter/topic_2",
        "arn:aws:iot:us-west-1:875385574461:topicfilter/sgp2021/solucion"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "iot:Connect"
      ],
      "Resource": [
        "arn:aws:iot:us-west-1:875385574461:client/sdk-java",
        "arn:aws:iot:us-west-1:875385574461:client/basicPubSub",
        "arn:aws:iot:us-west-1:875385574461:client/sdk-nodejs-*",
        "arn:aws:iot:us-west-1:875385574461:client/sdk/test/Python",
        "arn:aws:iot:us-west-1:875385574461:client/sgp2021/solucion"
      ]
    }
  ]
}