from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("exampleApp").getOrCreate()
df_quotes = spark.read.json("dataset/quotes")
df_authors = spark.read.json("dataset/authors")

df_quotes_and_authors = df_quotes.join(
    df_authors, df_quotes["author"] == df_authors["name"], "inner"
)
df_quotes_and_authors.write.format("json").mode("overwrite").save(
    "dataset/quotes_and_authors"
)
