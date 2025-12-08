# This script is meant to be run from the root level of your font's git repository.

from drawbot_skia.drawbot import *
from fontTools.ttLib import TTFont
from fontTools.misc.fixedTools import floatToFixedToStr

import subprocess
import argparse

# --- Constants -------------------------------------------------------------

WIDTH, HEIGHT, MARGIN = 2048, 1024, 128
FONT_PATH = "fonts/ttf/Allkin-Regular.ttf"
FONT_LICENSE = "OFL v1.1"

AUX_FONT = "Helvetica"
AUX_FONT_SIZE = 48

BIG_FONT_SIZE = 160
BIG_TEXT_SIDE_MARGIN = MARGIN
BIG_TEXT_BOTTOM_MARGIN = MARGIN * 5.45

GRID_VIEW = False

LILAC = (0.5, 0, 0.7)

LINE_ONE = "\uE000\uE001\uE002\uE003\uE004\uE005\uE006\uE007\uE008\uE009\uE00A\uE00B"
LINE_TWO = "\uE00D\uE00E\uE00F\uE010\uE011\uE012\uE013\uE014\uE015\uE016\uE017\uE018"
LINE_THREE = "\uE019\uE01A\uE01B\uE01C\uE01D\uE01E\uE01F\uE020\uE021\uE022\uE023\uE024"
LINE_FOUR = "\uE025\uE026\uE027\uE028\uE029\uE02A\uE02B\uE02C\uE02D\uE02E\uE02F"

# --- Argument parser ------------------------------------------------------

parser = argparse.ArgumentParser()
parser.add_argument("--output", metavar="PNG", help="where to write the PNG file")
args = parser.parse_args()

# --- Font meta info -------------------------------------------------------

ttFont = TTFont(FONT_PATH)
FONT_NAME = ttFont["name"].getDebugName(4)
FONT_VERSION = "v" + floatToFixedToStr(ttFont["head"].fontRevision, 16)

MY_URL = subprocess.check_output("git remote get-url origin", shell=True).decode().strip()
MY_HASH = subprocess.check_output("git rev-parse --short HEAD", shell=True).decode().strip()
URL_AND_HASH = f"{MY_URL} at commit {MY_HASH}"

# --- Drawing functions ----------------------------------------------------

def draw_background():
    newPage(WIDTH, HEIGHT)

    # Background with transitions: white → black → purple → black
    for r, g, b in [
        (1, 1, 1),
        (0, 0, 0),
        (0.5, 0, 0.7),
        (0, 0, 0)
    ]:
        fill(r, g, b)
        rect(-2, -2, WIDTH + 2, HEIGHT + 2)

    if GRID_VIEW:
        draw_grid()


def draw_grid():
    stroke(1, 0, 0, 0.75)
    strokeWidth(2)
    rect(MARGIN, MARGIN, WIDTH - 2*MARGIN, HEIGHT - 2*MARGIN)

    step = MARGIN / 2
    for i in range(29):
        x = MARGIN + i * step
        polygon((x, MARGIN), (x, HEIGHT - MARGIN))

        y = MARGIN + i * step
        polygon((MARGIN, y), (WIDTH - MARGIN, y))


def draw_main_text():
    font(FONT_PATH)
    fontSize(BIG_FONT_SIZE)
    stroke(None)

    fill(*LILAC)

    lines = [LINE_ONE, LINE_TWO, LINE_THREE, LINE_FOUR]
    leading = MARGIN * 1.2

    for i, text_line in enumerate(lines):
        text(text_line, (
            BIG_TEXT_SIDE_MARGIN,
            BIG_TEXT_BOTTOM_MARGIN - i * leading
        ))


def draw_divider_lines():
    stroke(*LILAC)
    strokeWidth(5)
    lineCap("round")

    line((MARGIN, HEIGHT - (MARGIN * 1.5)), (WIDTH - MARGIN, HEIGHT - (MARGIN * 1.5)))
    line((MARGIN, MARGIN + (MARGIN / 2)), (WIDTH - MARGIN, MARGIN + (MARGIN / 2)))

    stroke(None)


def draw_aux_text():
    font(AUX_FONT)
    fontSize(AUX_FONT_SIZE)

    fill(*LILAC)

    text(FONT_NAME, (MARGIN, HEIGHT - MARGIN * 1.25), align="left")
    text(FONT_VERSION, (WIDTH - MARGIN, HEIGHT - MARGIN * 1.25), align="right")
    text(URL_AND_HASH, (MARGIN, MARGIN), align="left")
    text(FONT_LICENSE, (WIDTH - MARGIN * 0.95, MARGIN), align="right")


# --- Build image ----------------------------------------------------------

if __name__ == "__main__":
    draw_background()
    draw_main_text()
    draw_divider_lines()
    draw_aux_text()
    saveImage(args.output)
    print("DrawBot: Done")
