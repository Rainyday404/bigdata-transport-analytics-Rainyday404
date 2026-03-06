# ==============================================================================
# ANALYTICS + SERVING LAYER
# ==============================================================================
import os
import time
from pyspark.sql import SparkSession
from pyspark.sql.functions import sum as _sum, avg, desc

# ============================
# START TIMER
# ============================
start_time = time.time()

print("=" * 40)
print("        ANALYTICS LAYER STARTED        ")
print("=" * 40)

# ============================
# INIT SPARK
# ============================
spark = SparkSession.builder \
    .appName("AnalyticsLayer") \
    .master("local[*]") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

# ============================
# CREATE SERVING FOLDER
# ============================
serving_path = "data/serving"
if not os.path.exists(serving_path):
    os.makedirs(serving_path)

# ============================
# LOAD CLEAN DATA (SILVER)
# ============================
print("Loading Clean Parquet Data...")
df_clean = spark.read.parquet("data/clean/parquet/")

total_records = df_clean.count()
print(f"Total Records: {total_records}")
print("-" * 40)

# ============================
# KPI 1: TOTAL REVENUE
# ============================
print("Calculating Total Revenue...")

total_revenue = df_clean.agg(
    _sum("total_amount").alias("total_revenue")
)
total_revenue.show()

# Save as CSV
total_revenue.write.mode("overwrite") \
    .option("header", True) \
    .csv(f"{serving_path}/total_revenue")

print(f"Total Revenue saved to {serving_path}/total_revenue")
print("-" * 40)

# ============================
# KPI 2: TOP 10 PRODUCTS
# ============================
print("Calculating Top 10 Products...")

top_products = df_clean.groupBy("product") \
    .agg(_sum("quantity").alias("total_quantity")) \
    .orderBy(desc("total_quantity")) \
    .limit(10)

top_products.show()

# Save as CSV
top_products.write.mode("overwrite") \
    .option("header", True) \
    .csv(f"{serving_path}/top_products")

print(f"Top Products saved to {serving_path}/top_products")
print("-" * 40)

# ============================
# KPI 3: REVENUE PER CATEGORY
# ============================
print("Calculating Revenue per Category...")

category_revenue = df_clean.groupBy("category") \
    .agg(_sum("total_amount").alias("category_revenue")) \
    .orderBy(desc("category_revenue"))

category_revenue.show()

# Save as CSV
category_revenue.write.mode("overwrite") \
    .option("header", True) \
    .csv(f"{serving_path}/category_revenue")

print(f"Category Revenue saved to {serving_path}/category_revenue")
print("-" * 40)

# ============================
# KPI 4: AVERAGE TRANSACTION VALUE
# ============================
print("Calculating Average Transaction Value per Customer...")

avg_transaction = df_clean.groupBy("customer_id") \
    .agg(avg("total_amount").alias("avg_transaction_value"))

avg_transaction.show(5)

# Save as CSV
avg_transaction.write.mode("overwrite") \
    .option("header", True) \
    .csv(f"{serving_path}/avg_transaction")

print(f"Average Transaction saved to {serving_path}/avg_transaction")
print("-" * 40)

# ============================
# STOP SPARK
# ============================
spark.stop()

end_time = time.time()
execution_time = round(end_time - start_time, 2)

print("=" * 40)
print("   ANALYTICS LAYER COMPLETED SUCCESS   ")
print(f"   Execution Time: {execution_time} sec")
print("=" * 40)