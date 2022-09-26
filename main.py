# dispositivo 02
# client_id - d3a03000

from time import sleep
import paho.mqtt.client as mqtt 
from random import choice 
from hal import Hal
from definitions import user, password, client_id, server, port 

hardware =  Hal()

def mensagem(client, userdata, msg):
  print(msg)
  vetor = msg.payload.decode().split(",")
  hardware.aquecedor("on" if vetor[1] == '1' else 'off')
  client.publish('v1/{}/things/{}/response'.format(user,client_id),
  f'ok,{vetor[0]}')
  
client = mqtt.Client(client_id)
client.username_pw_set(user,password)
client.connect(server,port)

client.on_message = mensagem
client.subscribe('v1/{}/things/{}/cmd/2'.format(user,client_id))
client.loop_start()

def main():
  while True:
      iot_1 = 'v1/{}/things/{}/data/0'.format(user,client_id)
      iot_2 = 'v1/{}/things/{}/data/1'.format(user,client_id)
      client.publish(iot_1, hardware.temperature())
      client.publish(iot_2, hardware.umidade())
      print(iot_1, iot_2)
      sleep(2)



if __name__ == "__main__":
     main()
