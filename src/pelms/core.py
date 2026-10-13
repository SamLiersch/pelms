# PELMS Image taking library
from picamera2 import Picamera2, Preview
from libcamera import Transform
from time import sleep


picam2 = Picamera2()


def preview(t: int = 0):
    """Run the preview window for time t so focus of the camera can be adjusted


    Args:
        t: Run for time t, if t = 0, runs forever

    Returns:
        None

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    preview_config = picam2.create_preview_configuration(
        transform=Transform(hflip=1, vflip=1)
    )
    picam2.configure(preview_config)
    picam2.start_preview(Preview.QTGL)
    picam2.start()
    if t == 0:
        while True:
            pass
    else:
        sleep(t)
