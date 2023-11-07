## Endpoint
https://g44wk54t0c.execute-api.us-east-1.amazonaws.com/default/gabsFunction

No body devem ser adicionados:<br>
USERNAME = "ponderada_gabs"<br>
    PASSWORD = "12345678"

## Função Lambda
 ```
 import json

def lambda_handler(event, context):

    USERNAME = "ponderada_gabs"
    PASSWORD = "12345678"


    if 'body' in event:
        body = json.loads(event['body'])
        if 'username' in body and 'password' in body:
            username = body['username']
            password = body['password']


            if username == USERNAME and password == PASSWORD:
                return {
                    'statusCode': 200,
                    'body': json.dumps({'message': 'Autenticado com sucesso! GABS'})
                }

    return {
        'statusCode': 401,
        'body': json.dumps({'message': 'Falha na autenticação, gabs'})
    }
```

##
