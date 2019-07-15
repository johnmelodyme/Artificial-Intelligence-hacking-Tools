# Run with python .\spotlight.py

from functools import reduce
import ctypes, os, winreg, glob, time
from PIL import Image

SPOTLIGHT_PATH = r"{0}\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets"

# >>>> CONFIGURATION VARIABLES <<<<
CHANGE_TIME_MINUTES = 2.5
MONITOR_COUNT = 2
MONITOR_SIZE = [(1920, 1080), (1920, 1080)]

SPI_SETDESKWALLPAPER    = 0x0014
SPI_SETDESKPATTERN      = 0x0015
SPIF_UPDATEINIFILE      = 0x01
SPIF_SENDWININICHANGE   = 0x02

# Map of wallpaper filenames to the number of times that they have been used
wallpapers = {}

# Next wallpaper in the sequence to be changed
next_change = 0

# Names of the current wallpapers
current_wallpapers = [None] * MONITOR_COUNT

def get_spotlight_path():
    return SPOTLIGHT_PATH.format(os.getenv("APPDATA") + "\\..")

def set_wallpapers(paths):
    # Load all images
    images = list()
    for i, p in enumerate(paths):
        images.append(Image.open(p).resize(MONITOR_SIZE[i], Image.BILINEAR))

    # Concatenate the images end-to-end
    final_image = Image.new("RGB", (reduce(lambda x, y: x + y.width, images, 0), max([x.height for x in images])))
    width = 0
    for i, image in enumerate(images):
        final_image.paste(image, (width, 0))
        width += image.width
    final_image.save(".\\wp.jpg", "JPEG")

    for k, v in {("TileWallpaper", "1"), ("WallpaperStyle", "0")}:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, winreg.KEY_WOW64_32KEY | winreg.KEY_WRITE)
        winreg.SetValueEx(key, k, 0, winreg.REG_SZ, v)
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, os.path.abspath(".\\wp.jpg"), SPIF_SENDWININICHANGE | SPIF_UPDATEINIFILE)

def change():
    global wallpapers, next_change, current_wallpapers

    def setw():
        sp = get_spotlight_path() + "\\"
        set_wallpapers([sp + p for p in current_wallpapers])

    lowest = lambda w: sorted(w.items(), key=lambda x: x[1])[0][0]

    # If no wallpapers have been set yet, then set up the initial wallpapers
    if current_wallpapers[0] is None:
        for x in range(0, MONITOR_COUNT):
            l = lowest(wallpapers)
            wallpapers[l] += 1
            current_wallpapers[x] = l
        setw()
        return

    # Set the current wallpaper for the next monitor to be changed to the
    # wallpaper least used out of the list
    l = lowest(wallpapers)
    wallpapers[l] += 1
    current_wallpapers[next_change] = l
    next_change += 1
    if next_change == MONITOR_COUNT:
        next_change = 0

    setw()

# Poll for new wallpapers and update the wallpaper table
def update():
    size_max = (max([x[0] for x in MONITOR_SIZE]), max([x[1] for x in MONITOR_SIZE]))
    for wp in glob.glob(get_spotlight_path() + "\\*"):
        name = os.path.basename(wp) 
        if not name in wallpapers:
            try:
                with Image.open(wp) as image:
                    if image.width < size_max[0] or image.height < size_max[1]:
                        continue
            except:
                continue
            wallpapers[name] = 0

if __name__ == "__main__":
    while True:
        update()
        change()
        time.sleep(CHANGE_TIME_MINUTES * 60)
