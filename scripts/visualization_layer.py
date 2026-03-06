# ===================================== 
# VISUALIZATION LAYER 
# ===================================== 

import os
import matplotlib.pyplot as plt
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# 1. Inisialisasi Spark
spark = SparkSession.builder \
    .appName("VisualizationLayer") \
    .master("local[*]") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

# 2. Load Data
input_path = "data/clean/parquet/"
output_dir = "reports"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

df = spark.read.parquet(input_path)

# 3. Agregasi Data
# Menggunakan alias agar nama kolom di Pandas tidak berantakan (misal: 'sum(total_amount)')
category_df = df.groupBy("category") \
    .agg(F.sum("total_amount").alias("total_revenue")) \
    .orderBy(F.desc("total_revenue")) \
    .toPandas()

# 4. Visualisasi
plt.style.use('ggplot') # Opsional: Memberikan tampilan yang lebih modern
plt.figure(figsize=(10, 6))

# Membuat bar chart
bars = plt.bar(category_df["category"], category_df["total_revenue"], color='skyblue')

# Mempercantik tampilan
plt.title("Revenue per Category", fontsize=14, fontweight='bold')
plt.xlabel("Category", fontsize=12)
plt.ylabel("Total Revenue", fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Memberikan label nilai di atas bar (opsional tapi sangat membantu)
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:,.0f}', 
             va='bottom', ha='center', fontsize=9)

plt.tight_layout()

# 5. Simpan & Tutup
output_file = f"{output_dir}/category_revenue.png"
plt.savefig(output_file)
print(f"✅ Visualization successfully saved to: {output_file}")

spark.stop()