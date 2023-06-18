import sys
import logging
from pyspark.sql import SparkSession
from parsing import parse_author
from models import Author

logging.basicConfig(
    level=logging.INFO if sys.argv[1] == "--verbose" else logging.NOTSET
)
spark = SparkSession.builder.appName("exampleApp").getOrCreate()
df_quotes = spark.read.json("dataset/quotes")
author_names = df_quotes.select("author").collect()
authors: list[Author] = [parse_author(name["author"]) for name in author_names]
df_authors = spark.createDataFrame(authors).dropDuplicates()
df_authors.write.format("json").mode("overwrite").save("dataset/authors")
