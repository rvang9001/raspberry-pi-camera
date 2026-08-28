import Camera
from datetime import datetime
import time


class CameraSystem:
    def __init__(self):
        self.cam = Camera.Camera()

    def record(self, name, duration):
        self.cam.record(name, duration=duration)


if __name__ == '__main__':
    cam_system = CameraSystem()

    # Target time (Year, Month, Day, Hour, Minute, Second)
    target_time = datetime(2026, 8, 27, 19, 24, 0)

    while datetime.now() < target_time:
        time_now = datetime.now().replace(second=0, microsecond=0)
        print(time_now)
        time.sleep(1)

    try:
        while True:
            cam_system.record(datetime.now(), duration=3600)

    except KeyboardInterrupt:
        print("Stopping camera system...")
        cam_system.cam.close()
