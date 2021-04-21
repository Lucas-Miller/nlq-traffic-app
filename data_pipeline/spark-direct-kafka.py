from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split

import os

os.environ['PYSPARK_SUBMIT_ARGS'] = '--jars /Users/augmentedmode/Downloads/spark-streaming-kafka-0-8-assembly_2.11-2.4.6.jar pyspark-shell' 

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils


def handler(timestamp, message):
    records = message.collect()
    print(records)

# Load Spark Context
sc = SparkContext(appName='PyctureStream')
ssc = StreamingContext(sc, 10)  # , 3)

kvs = KafkaUtils.createDirectStream(ssc,
                                            ['stream'],
                                            {'metadata.broker.list': '127.0.0.1:9092'}
                                            )
kvs.foreachRDD(handler)
ssc.start()
ssc.awaitTermination()


