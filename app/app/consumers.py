# chat/consumers.py
import json
import time

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.core.exceptions import ValidationError
import json




class ProgressBarConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = 'btcusdt'
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type": "send_price",
                "message": {
                    "message": "The cake is ready" # todo change 
                },
            },
        )

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    def send_progress_msg(self, msg):
        self.send(
            text_data=json.dumps(
                {
                    "price": str(msg),
                }
            )
        )

    def send_completed_msg(self, msg):
        self.send(
            text_data=json.dumps(
                {
                    "type": "completed",
                    "message": msg,
                }
            )
        )

    def send_error_msg(self, msg):
        if not isinstance(msg, str):
            msg = (
                msg.args[0] if hasattr(msg, "args") and len(msg.args) > 0 else str(msg)
            )
        self.send(text_data=json.dumps({"type": "error", "message": msg}))

    def send_price(self, event):
        message = event["message"]
        self.send_progress_msg("Gathering Ingredients")

        self.send_progress_msg("Preparing the Batter")

        self.send_progress_msg("Preparing Cake Pans")

        self.send_progress_msg("Baking")

        self.send_progress_msg("Cooling And Frosting")


