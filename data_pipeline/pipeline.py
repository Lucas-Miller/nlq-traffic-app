from pyspark import SparkContext
from pyspark.sql.session import SparkSession

from pyspark.streaming import StreamingContext

# Create a local StreamingContext with two working thread and batch interval of 1 second
# s3://main-image-database/images/
spark = SparkSession.builder \
            .appName("app_name") \
            .getOrCreate()


aws_id = ''
aws_key = ''

spark._jsc.hadoopConfiguration().set("fs.s3n.awsAccessKeyId", aws_id)
spark._jsc.hadoopConfiguration().set("fs.s3n.awsSecretAccessKey", aws_key)
spark._jsc.hadoopConfiguration().set("fs.s3a.impl","org.apache.hadoop.fs.s3a.S3AFileSystem")
spark._jsc.hadoopConfiguration().set("com.amazonaws.services.s3.enableV4", "true")
spark._jsc.hadoopConfiguration().set("fs.s3a.aws.credentials.provider","org.apache.hadoop.fs.s3a.BasicAWSCredentialsProvider")
spark._jsc.hadoopConfiguration().set("fs.s3a.endpoint", "eu-east-3.amazonaws.com")

#ssc = StreamingContext(sc, 1)

# Create a DStream that will connect to hostname:port, like localhost:9999
#stream = ssc.FileStream('s3://main-image-database/images/')

df = spark.read.format("image").option("dropInvalid", True).load("/Users/augmentedmode/Desktop/nlq-traffic-app/image_data/images/*.jpg")

print(df)
#print(stream)

#ssc.start()             # Start the computation
#ssc.awaitTermination()  # Wait for the computation to terminate
