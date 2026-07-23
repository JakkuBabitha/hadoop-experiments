from pyspark.sql.functions import explode, split, col, desc

df = spark.read.text("file:///Users/jakkubabitha/Experiment11/sample.txt")

words = df.select(explode(split(col("value"), " ")).alias("word"))
counts = words.groupBy("word").count()

counts.orderBy(desc("count")).show()
