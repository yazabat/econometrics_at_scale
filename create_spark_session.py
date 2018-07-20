# Import Python modules
import os
import sys

# Set path
os.environ['SPARK_HOME'] = '/usr/lib/spark'
sys.path.append('/usr/lib/spark/python')
sys.path.append('/usr/lib/spark/python/lib/py4j-0.10.4-src.zip')

# Import PySpark modules
from pyspark.sql import SparkSession

def create_spark_session():

    spark_session = SparkSession.builder.appName('spark_parallel_forecasting')\
        .config("spark.dynamicAllocation.enabled", "true")\
        .config("spark.shuffle.service.enabled", "true") \
        .config('maximizeResourceAllocation', "true")\
        .master('yarn').getOrCreate()

    # .config("spark.executor.memory", "5g") \
    # .config("spark.executor.cores", "1") \
    # .config("spark.num.executors", "50") \

    return spark_session