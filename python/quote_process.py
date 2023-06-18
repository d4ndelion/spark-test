import sys
import logging
from pyspark.sql import SparkSession
from parsing import parse_quotes
from python.models import Quote

logging.basicConfig(
    level=logging.INFO if sys.argv[1] == "--verbose" else logging.NOTSET
)
spark = SparkSession.builder.appName("exampleApp").getOrCreate()
quotes: list[Quote] = parse_quotes()
df = spark.createDataFrame(quotes)
df.write.format("json").mode("overwrite").save("dataset/quotes")
