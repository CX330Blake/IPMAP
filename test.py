import time
import sys


def animated_print(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")


# 例子
animated_print("这是一行一行打印的动画效果！", delay=0.1)
animated_print("希望对你有帮助！", delay=0.1)
