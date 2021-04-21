-Set up a python3 virutal environment and activate it 
    python3 -m venv venvName
    source venvName/bin/activate

-Install Flask through pip with your venv active
-Download models and place in models folder in root of project
-Vision encoder: https://drive.google.com/drive/folders/1Byok0ZCFlqfExe7bfAZ-FTUiJsAxlKdQ?usp=sharing
-Text encoder: https://drive.google.com/drive/folders/1-JqvysxGkAzZC0xLKFB8rpN8lKKeS3ct?usp=sharing

-Download image data set and place in static/image_data
-Image dataset: https://drive.google.com/drive/folders/1OA6NF5IyulbXYZ6cilIS65QB9BJANvI2?usp=sharing

-After Setting up your environment, start your development server

-To run the dev server:
    export FLASK_APP=main
    flask run

- Note: these commands are for bash shell, your commands might be different depending on your shell

-Go to localhost:5000 in your web browser
-For more instructions check out this tutorial: 
    https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3

-To run the data pipeline

Start data pipeline (faust): faust -A stream_processor worker -l info
Start Spark Direct Streaming: python3 spark-direct-kafka.py  


Start Zookeeper: zookeeper-server-start /usr/local/etc/kafka/zookeeper.properties
Start Kafka Server: kafka-server-start /usr/local/etc/kafka/server.properties


Send data to topic via terminal as a test: faust -A stream_processor send @greet "Hello Faust"

Apache Kafka process the data from topics which receives data from a producer (Tesla Cars) and then streams it to Apache Spark which ingests the data from Kafka


Apache Kafka processes all the data as it arrives in real time where Apache Spark then uses a micro batch processing model by splitting the incoming stream from Kafka into small batches for further processing. Our ETL (Extract Transform Load) processing is done on Apache Spark. 
