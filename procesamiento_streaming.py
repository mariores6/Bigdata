from pyspark.sql import SparkSession
from pyspark.sql.functions import split, col

spark = SparkSession.builder \
    .appName("ProcesamientoStreamingTrafico") \
    .getOrCreate()

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "trafico_topic") \
    .load()

df_string = df.selectExpr("CAST(value AS STRING) as linea")

# Ejemplo: dividir columnas si vienen separadas por coma
df_split = df_string.withColumn("campos", split(col("linea"), ",")) \
    .withColumn("fecha", col("campos")[0]) \
    .withColumn("vehiculos", col("campos")[1].cast("int"))

# Estadísticas: promedio de vehículos por fecha
resultado = df_split.groupBy("fecha").avg("vehiculos")

query = resultado.writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()
