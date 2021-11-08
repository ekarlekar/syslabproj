import argparse
import random
import time

from pythonosc import udp_client

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip", default="127.0.0.1")
  parser.add_argument("--port", type=int, default=4357)
  args = parser.parse_args()

  client = udp_client.SimpleUDPClient(args.ip, args.port)

  for x in range(5):
    client.send_message("/base", random.random())
    client.send_message("/base2", random.random())

    # Facial Expressions - Eyes
    client.send_message("/fac/eyeAct/neutral", random.random())
    client.send_message("/fac/eyeAct/lookL", random.random())
    client.send_message("/fac/eyeAct/lookR", random.random())
    client.send_message("/fac/eyeAct/blink", random.random())
    client.send_message("/fac/eyeAct/winkL", random.random())
    client.send_message("/fac/eyeAct/winkR", random.random())

    # Facial Expressions - Upper Face
    client.send_message("/fac/uAct/neutral", random.random())
    client.send_message("/fac/uAct/frown", random.random())
    client.send_message("/fac/uAct/surprise", random.random())

    # Facial Expressions - LowerFace
    client.send_message("/fac/lAct/neutral", random.random())
    client.send_message("/fac/lAct/clench", random.random())
    client.send_message("/fac/lAct/laugh", random.random())
    client.send_message("/fac/lAct/smile", random.random())
    client.send_message("/fac/lAct/smirkLeft", random.random())
    client.send_message("/fac/lAct/smirkRight", random.random())

    # Mental Commands
    client.send_message("/com/neutral", random.random())
    client.send_message("/com/push", random.random())
    client.send_message("/com/pull", random.random())
    client.send_message("/com/left", random.random())
    client.send_message("/com/right", random.random())
    client.send_message("/com/lift", random.random())
    client.send_message("/com/drop", random.random())
    client.send_message("/com/rotateLeft", random.random())
    client.send_message("/com/rotateRight", random.random())
    client.send_message("/com/rotateClockwise", random.random())
    client.send_message("/com/rotateCounterClockwise", random.random())
    client.send_message("/com/rotateForwards", random.random())
    client.send_message("/com/rotateReverse", random.random())
    client.send_message("/com/disappear", random.random())

    # Performance Metrics
    client.send_message("/met/foc", random.random())
    client.send_message("/met/int", random.random())
    client.send_message("/met/rel", random.random())
    client.send_message("/met/str", random.random())
    client.send_message("/met/exc", random.random())
    client.send_message("/met/eng", random.random())
    client.send_message("/met/visualAttention", random.random())
    client.send_message("/met/cognitiveStress", random.random())
    client.send_message("/met/auditoryAttention", random.random())

    time.sleep(10)