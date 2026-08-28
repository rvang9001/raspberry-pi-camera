from picamera2 import Picamera2


class Camera:
    def __init__(self):
        self.cam = Picamera2()
        self.video_config = self.cam.create_video_configuration(
            main={"size": (2304, 1296)}
        )
        self.configure()

    def configure(self):
        return self.cam.configure(self.video_config)

    def record(self, name, duration):
        self.cam.start_and_record_video(name, duration=duration)

    def close(self):
        self.cam.stop()
        self.cam.close()


if __name__ == '__main__':
    c = Camera()
