"""
:author Luis Manuel Torres Trevino
:date 28/01/2020
:description Archivo que contiene un ejemplo del productor de mensajes de kafka
:version 1.0.0
"""

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['10.1.8.40:6667'])
with open('inputfile.txt') as f:
    lines = f.readlines()

for line in lines:
    producer.send('test', line)