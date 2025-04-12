# Proyecto de Streaming de Datos Vehiculares con Apache Spark y Kafka

Este proyecto simula el procesamiento en tiempo real de datos de tráfico vehicular usando Apache Kafka y Apache Spark Streaming.

## 📦 Requisitos

- Apache Spark
- Apache Kafka
- Python 3
- Java 8+

## 🛠 Instalación

1. Asegúrate de que Zookeeper y Kafka estén en ejecución:

```bash
/opt/kafka/bin/zookeeper-server-start.sh /opt/kafka/config/zookeeper.properties
/opt/kafka/bin/kafka-server-start.sh /opt/kafka/config/server.properties
```

2. Crea el topic en Kafka:

```bash
/opt/kafka/bin/kafka-topics.sh --create --topic trafico_topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

3. Ejecuta el productor:

```bash
bash productor_kafka.sh
```

4. Ejecuta el consumidor Spark Streaming:

```bash
spark-submit --jars /opt/spark/jars/spark-sql-kafka-0-10_2.12-3.5.0.jar,/opt/spark/jars/kafka-clients-3.5.0.jar,/opt/spark/jars/spark-token-provider-kafka-0-10_2.12-3.5.0.jar,/opt/spark/jars/commons-pool2-2.11.1.jar spark_kafka_streaming.py
```
