from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, when, col, round
from pyspark.sql import Window

conf = SparkConf().setAppName("adult_data_analytics")
sc = SparkContext(conf=conf)
ctx = SparkSession(sc)

ddf = ctx.read.option("header", True).csv('/tmp/data/adult_data.csv')

# With SQL Syntax
ddf.registerTempTable("USERS")
query = """
    SELECT *, AVG(age) OVER (PARTITION BY `native-country`) AS avg_age
    FROM USERS
    WHERE workclass = 'Private'
"""
ctx.sql(query).show(20)
ctx.sql(query).repartition(1).write.csv('/tmp/data/adult_data_sql_syntax')

# With Pyspark Syntax
window = Window.partitionBy("`native-country`")
result_ddf = ddf.withColumn("avg_age", avg("age").over(window)) \
    .filter(ddf["workclass"] == 'Private') \
    .select("*", round(col('avg_age')))

result_ddf.show(20)
result_ddf.repartition(1).write.csv('/tmp/data/adult_data_pyspark_syntax')
    