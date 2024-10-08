#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (c) 2016 James Myatt <james@jamesmyatt.co.uk>
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Distribution License v1.0
# which accompanies this distribution.
#
# The Eclipse Distribution License is available at
#   http://www.eclipse.org/org/documents/edl-v10.php.
#
# Contributors:
#    James Myatt - initial implementation

# This shows a simple example of standard logging with an MQTT subscriber client.

import logging

import context  # Ensures paho is in PYTHONPATH

import paho.mqtt.client as mqtt


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# If you want to use a specific client id, use
# mqttc = mqtt.Client("client-id")
# but note that the client id must be unique on the broker. Leaving the client
# id parameter empty will generate a random id for you.
mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.enable_logger(logger)

logger.info('fdsfdsfs, mqtt')
mqttc.connect("mqtt.eclipseprojects.io", 1883, 60)
mqttc.subscribe("$SYS/#", 0)

mqttc.loop_forever()
