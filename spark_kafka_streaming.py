from pyspark.sql import SparkSession
from pyspark.sql.functions import expr

# Crear sesión de Spark
spark = SparkSession.builder \
    .appName("StreamingTraficoVehicular") \
    .getOrCreate()

# Leer datos desde Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "trafico_topic") \
    .load()

# Convertir valor (binario) a string
df_string = df.selectExpr("CAST(value AS STRING) as linea")

# Mostrar el stream en consola
query = df_string.writeStream \
    .outputMode("append") \
    .format("console") \
    .option("truncate", False) \
    .start()

query.awaitTermination()
