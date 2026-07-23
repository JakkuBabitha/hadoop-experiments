data = [
    ("Hello world Hello Spark",),
    ("Spark is great for big data",),
    ("Hello Python and Spark",)
]

df = spark.createDataFrame(data, ["line"])

from pyspark.sql.functions import explode, split, col, desc

words_df = df.select(explode(split(col("line"), " ")).alias("word"))
word_counts = words_df.groupBy("word").count()
word_counts.orderBy(desc("count")).show()

