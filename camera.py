"""Camera module for RTSP stream management."""

import cv2
import threading
import logging

logger = logging.getLogger(__name__)

GROUP_7 = "camera_group_7"


class Camera:
    """Represents a single RTSP camera stream."""

    def __init__(self, name: str, rtsp_url: str, camera_id: int):
        self.name = name
        self.rtsp_url = rtsp_url
        self.camera_id = camera_id
        self.capture = None
        self.is_connected = False
        self.frame = None
        self.lock = threading.Lock()
        self.stop_event = threading.Event()

    def connect(self) -> bool:
        """Connect to the RTSP stream."""
        try:
            self.capture = cv2.VideoCapture(self.rtsp_url)
            if self.capture.isOpened():
                self.is_connected = True
                logger.info(f"Camera {self.name} connected successfully")
                return True
            else:
                logger.error(f"Failed to open camera {self.name}")
                return False
        except Exception as e:
            logger.error(f"Error connecting to camera {self.name}: {e}")
            return False

    def disconnect(self):
        """Disconnect from the camera stream."""
        with self.lock:
            self.is_connected = False
            if self.capture:
                self.capture.release()
                self.capture = None
        logger.info(f"Camera {self.name} disconnected")

    def read_frame(self) -> bool:
        """Read a frame from the camera."""
        if not self.is_connected or not self.capture:
            return False

        with self.lock:
            ret, frame = self.capture.read()
            if ret:
                self.frame = frame
            return ret

    def get_frame(self):
        """Get the current frame."""
        with self.lock:
            return self.frame

    def start_capture(self):
        """Start continuous capture in a separate thread."""
        thread = threading.Thread(target=self._capture_loop, daemon=True)
        thread.start()
        return thread

    def _capture_loop(self):
        """Internal capture loop."""
        while not self.stop_event.is_set():
            if not self.read_frame():
                logger.warning(f"Failed to read frame from {self.name}")
                break
            threading.Event().wait(0.03)  # ~30 FPS

    def stop(self):
        """Stop the capture."""
        self.stop_event.set()
        self.disconnect()

    def __repr__(self):
        return f"Camera(name={self.name}, id={self.camera_id})"