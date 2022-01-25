from flask import current_app as app
from google.cloud import pubsub_v1
from google.oauth2 import service_account

import json
import os

PROJECT_ID = os.environ.get("PROJECT_ID")


class GCloudPubSub:
    def __init__(self):
        # Define vars
        GOOGLE_APPLICATION_CREDENTIALS = os.environ[
            "GOOGLE_APPLICATION_CREDENTIALS"
        ] = app.config["GS_CREDENTIALS"]
        GOOGLE_APPLICATION_CREDENTIALS = json.loads(GOOGLE_APPLICATION_CREDENTIALS)
        self.credentials = service_account.Credentials.from_service_account_info(
            GOOGLE_APPLICATION_CREDENTIALS
        )

        scoped_credentials = self.credentials.with_scopes(
            ["https://www.googleapis.com/auth/cloud-platform"]
        )
        
        self.project_id = json.loads(app.config["GS_CREDENTIALS"])["project_id"]
        # Init Firebase admin
        try:
            self.client = pubsub_v1.PublisherClient(credentials=scoped_credentials)
        except Exception as e:
            raise e

    def _publish_message(self, message):
        topic_name = "pub_transactions"
        # Init pubsub client
        publisher = GCloudPubSub()
        # Define topic path
        topic = publisher.client.topic_path(publisher.project_id, topic_name)
        # Create message
        message = dict(message)
        # Queue Message
        message_future = publisher.client.publish(
            topic, data=json.dumps(message).encode("UTF-8")
        )

        message_future.add_done_callback(self.callback)

    def callback(self, message_future):
        self.queued = False
        message_future.exception(timeout=10)
        while message_future.running():
            print("running.")
        self.queued = True
