import base64
import json
from cypher_base64.libs.pubsub import GCloudPubSub


class CypherService:
    def encode_base64(self, file):
        return base64.b64encode(file.read())

    def get_file_format(self, file):
        return file.filename.rsplit(".", 1)[1].lower()

    def publish_message(self, message):
        data = json.dumps(message).encode("UTF-8")
        publisher = GCloudPubSub()
        topic_name = "neuralmed"
        topic = publisher.client.topic_path(publisher.project_id, topic_name)

        message_future = publisher.client.publish(topic, data=data)
        message_future.add_done_callback(self.callback)

    def callback(self, message_future):
        self.queued = False
        message_future.exception(timeout=10)
        while message_future.running():
            print("running.")
        self.queued = True
