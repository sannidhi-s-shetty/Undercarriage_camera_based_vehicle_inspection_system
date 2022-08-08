# import curses
# import RPi.GPIO as GPIO
# from time import sleep

# GPIO.setmode(GPIO.BOARD)
# GPIO.setwarnings(False)
#

def controller(char):
    # char = screen.getch()

    if char == "stop":
        # break
        return
    elif char == "up":
        print("up")
        # GPIO.output(7, True)
        # GPIO.output(16, False)
        # GPIO.output(13, True)
        # GPIO.output(15, False)
    elif char == "down":
        print("down")
        # GPIO.output(7, False)
        # GPIO.output(16, True)
        # GPIO.output(13, False)
        # GPIO.output(15, True)
    elif char == "left":
        print("left")
        # GPIO.output(7, False)
        # GPIO.output(16, True)
        # GPIO.output(13, True)
        # GPIO.output(15, False)
    elif char == "right":
        print("right")
        # GPIO.output(7, True)
        # GPIO.output(16, False)
        # GPIO.output(13, False)
        # GPIO.output(15, True)
    else:
        print("stop")
        # GPIO.output(7, False)
        # GPIO.output(16, False)
        # GPIO.output(13, False)
        # GPIO.output(15, False)


if __name__ == '__main__':
    import sys
    char = sys.argv[1]
    # GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
    # GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)
    # GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
    # GPIO.setup(15, GPIO.OUT, initial=GPIO.LOW)
    # GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)
    controller(char)
    # GPIO.cleanup()
    # screen = curses.initscr()
    # curses.noecho()
    # curses.cbreak()
    # screen.keypad(True)
    # curses.halfdelay(3)
    # arg = screen.getch()
    # curses.nocbreak()
    # screen.keypad(False)
    # curses.echo()
    # curses.endwin()
# Streaming command on laptop side: vlc rtsp://192.168.241.5:8554/ --sout="#duplicate{dst=display,dst=std{access=file, mux=ts, dst=sample5.ts}}"
