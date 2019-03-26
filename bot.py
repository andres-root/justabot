import os
import tweepy
import requests

# Obtener las llaves de la app de Twitter desde variables de entorno por seguridad
consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')

# Autenticar utilizando estas llaves
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# Configura el access token
auth.set_access_token(access_token, access_token_secret)

# Obtiene objeto de API de consulta de twitter
api = tweepy.API(auth)

# Consulta los datos del sensor en la IP del Wemos
response = requests.get('http://localhost:3000/sensor.json')

# Convierte la respuesta del servidor de Wemos en un diccionario de Python
sensor_data = response.json()

temperature = response['variables']['temperature']

# Envia el tweet en mi cuenta
api.update_status('La temperatura es: {0}'.format(temperature))
