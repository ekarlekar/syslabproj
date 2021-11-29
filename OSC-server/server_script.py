import argparse
import math
import sys

from pythonosc import dispatcher
from pythonosc import osc_server
# f = open("output.txt", "a")

def print_volume_handler(unused_addr, args, volume):
  print("[{0}] ~ {1}".format(args[0], volume))

def write_file_neutral(unused_addr, args):
  f = open("output.txt", "a")
  # f.write("\n")
  f.write("neutral")
  f.close()
  print("got")

def write_file_blink(unused_addr, args):
  f = open("output.txt", "a")
  f.write("\n")
  f.write("blink")
  f.close()

def print_compute_handler(unused_addr, args, volume):
  try:
    print("[{0}] ~ {1}".format(args[0], args[1](volume)))
  except ValueError: pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
        default="127.0.0.1", help="The ip to listen on")
    parser.add_argument("--port",
        type=int, default=4357, help="The port to listen on") # originally 5005 for port
    args = parser.parse_args()

    dispatcher = dispatcher.Dispatcher()
    # dispatcher.map("/base", print)
    # dispatcher.map("/base2", print)

    # Facial Expressions - Eyes
    dispatcher.map("/fac/eyeAct/neutral", write_file_neutral)
    # dispatcher.map("/fac/eyeAct/lookL", print)
    # dispatcher.map("/fac/eyeAct/lookR", print)
    dispatcher.map("/fac/eyeAct/blink", write_file_blink)
    # dispatcher.map("/fac/eyeAct/winkL", print)
    # dispatcher.map("/fac/eyeAct/winkR", print)

    # # Facial Expressions - Upper Face
    # dispatcher.map("/fac/uAct/neutral", print)
    # dispatcher.map("/fac/uAct/frown", print)
    # dispatcher.map("/fac/uAct/surprise", print)

    # # Facial Expressions - LowerFace
    # dispatcher.map("/fac/lAct/neutral", print)
    # dispatcher.map("/fac/lAct/clench", print)
    # dispatcher.map("/fac/lAct/laugh", print)
    # dispatcher.map("/fac/lAct/smile", print)
    # dispatcher.map("/fac/lAct/smirkLeft", print)
    # dispatcher.map("/fac/lAct/smirkRight", print)

    # # Mental Commands
    # dispatcher.map("/com/neutral", print)
    # dispatcher.map("/com/push", print)
    # dispatcher.map("/com/pull", print)
    # dispatcher.map("/com/left", print)
    # dispatcher.map("/com/right", print)
    # dispatcher.map("/com/lift", print)
    # dispatcher.map("/com/drop", print)
    # dispatcher.map("/com/rotateLeft", print)
    # dispatcher.map("/com/rotateRight", print)
    # dispatcher.map("/com/rotateClockwise", print)
    # dispatcher.map("/com/rotateCounterClockwise", print)
    # dispatcher.map("/com/rotateForwards", print)
    # dispatcher.map("/com/rotateReverse", print)
    # dispatcher.map("/com/disappear", print)

    # # Performance Metrics
    # dispatcher.map("/met/foc", print)
    # dispatcher.map("/met/int", print)
    # dispatcher.map("/met/rel", print)
    # dispatcher.map("/met/str", print)
    # dispatcher.map("/met/exc", print)
    # dispatcher.map("/met/eng", print)
    # dispatcher.map("/met/visualAttention", print)
    # dispatcher.map("/met/cognitiveStress", print)
    # dispatcher.map("/met/auditoryAttention", print)

    # only for debugging purposes
    # dispatcher.map("/volume", print_volume_handler, "Volume")
    # dispatcher.map("/logvolume", print_compute_handler, "Log volume", math.log)

    server = osc_server.ThreadingOSCUDPServer(
        (args.ip, args.port), dispatcher)
    print("Listening on {}".format(server.server_address))
    server.serve_forever()
