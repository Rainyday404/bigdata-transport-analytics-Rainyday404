from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Inisialisasi Spark Session
spark = SparkSession.builder \
    .appName("StreamingPipeline") \
    .getOrCreate()

# Mengatur log level agar hanya menampilkan error saja di konsol
spark.sparkContext.setLogLevel("ERROR")

# Mendefinisikan schema untuk data JSON yang akan dibaca
schema = """
user_id INT,
product STRING,
price DOUBLE,
city STRING,
timestamp STRING
"""

# Membaca stream dari folder "stream_data"
stream_df = spark.readStream \
    .schema(schema) \
    .option("maxFilesPerTrigger", 1) \
    .json("stream_data")

# Menulis aliran data (stream) ke dalam format Parquet
query = stream_df.writeStream \
    .outputMode("append") \
    .format("parquet") \
    .option("path", "data/serving/stream") \
    .option("checkpointLocation", "logs/stream_checkpoint") \
    .trigger(processingTime="5 seconds") \
    .start()

# Menjaga agar aplikasi tetap berjalan selama proses streaming berlangsung
query.awaitTermination()