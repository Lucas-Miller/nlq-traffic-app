import faust
import random

app = faust.App(
    'hello-world',
    broker='kafka://localhost:9092',
    value_serializer='raw',
)

image_topic = app.topic('stream')

@app.agent(image_topic)
async def greet(stream):
    async for event in stream:
        print(event)


@app.task
async def on_started():
    print('APP STARTED')

'''
# Send messages
@app.timer(interval=1.0)
async def send_message(app):
    await image_topic.send(value=str(random.randint(0,100)))
'''

if __name__ == '__main__':
    app.main()