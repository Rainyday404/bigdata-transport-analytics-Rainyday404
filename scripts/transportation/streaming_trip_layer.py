from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *

# Inisialisasi Spark Session untuk Streaming
spark = SparkSession.builder.appName("TransportationStreaming").getOrCreate()

# Mendefinisikan skema data agar Spark tahu tipe data tiap kolom
schema = StructType([
    StructField("trip_id", StringType()),
    StructField("vehicle_type", StringType()),
    StructField("location", StringType()),
    StructField("distance", DoubleType()),
    StructField("fare", DoubleType()),
    StructField("timestamp", StringType())
])

# Membaca stream data JSON dari folder sumber
df = spark.readStream.schema(schema).json("stream_data/transportation")

# Mengubah kolom timestamp dari string menjadi tipe data timestamp yang sesungguhnya
df = df.withColumn("timestamp", to_timestamp("timestamp"))

# Menulis stream data ke dalam format Parquet (Serving Layer)
df.writeStream \
    .format("parquet") \
    .option("path", "data/serving/transportation") \
    .option("checkpointLocation", "data/checkpoints/transportation") \
    .start() \
    .awaitTermination()