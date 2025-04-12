#!/bin/bash
# Script para simular streaming con el CSV

cat ~/trafico_vehicular.csv | while read linea; do
  echo "$linea" | /opt/kafka/bin/kafka-console-producer.sh --topic trafico_topic --bootstrap-server localhost:9092
  sleep 1
done
