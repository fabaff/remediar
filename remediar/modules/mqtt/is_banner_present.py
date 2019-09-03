"""Support for getting the service banner of a MQTT broker."""
import time

import paho.mqtt.client as mqtt

from remediar.helper import Check


class CheckMqttIsBannerPresent(Check):
    """Representation of a MQTT broker banner check."""

    def __init__(self, server, **kwargs):
        """Initialize the check."""
        self._server = server
        if kwargs:
            self._port = kwargs['port'] or 1883
        self._name = ""
        self._output = None
        self.run_check()

    @property
    def name(self) -> str:
        """Return the name of the check."""
        return self._name

    @property
    def result(self) -> str:
        """Return the state of the check."""
        if isinstance(self._output, str):
            return True
        elif self._output is False:
            return False
        else:
            return None

    @property
    def output(self) -> str:
        """Return the output of the check."""
        return self._output

    def run_check(self):
        """Run the check."""
        client = mqtt.Client()
        client.on_message = self.on_message

        try:
            client.connect(self._server, self._port, 60)
            client.subscribe("$SYS/broker/version")

            client.loop_start()
            time.sleep(2)
            client.loop_stop()
        except ConnectionRefusedError:
            self._output = None

    def on_message(self, client, userdata, msg):
        """Callback for when a PUBLISH message is received from the server."""
        self._output = msg.payload.decode('utf-8')
