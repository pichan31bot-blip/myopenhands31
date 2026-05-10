"""Streaming module for managing multiple RTSP camera streams."""

import threading
import logging
from typing import List
from camera import Camera

logger = logging.getLogger(__name__)


class StreamManager:
    """Manages multiple camera streams."""

    def __init__(self):
        self.cameras: List[Camera] = []
        self.threads: List[threading.Thread] = []
        self.lock = threading.Lock()

    def add_camera(self, name: str, rtsp_url: str, camera_id: int):
        """Add a camera to the manager."""
        camera = Camera(name, rtsp_url, camera_id)
        with self.lock:
            self.cameras.append(camera)
        logger.info(f"Added camera: {name}")

    def connect_all(self) -> bool:
        """Connect to all cameras."""
        success = True
        for camera in self.cameras:
            if not camera.connect():
                success = False
        return success

    def start_all(self):
        """Start capturing from all cameras."""
        for camera in self.cameras:
            thread = camera.start_capture()
            self.threads.append(thread)
        logger.info(f"Started {len(self.threads)} camera streams")

    def stop_all(self):
        """Stop all camera streams."""
        for camera in self.cameras:
            camera.stop()
        logger.info("Stopped all camera streams")

    def get_camera(self, camera_id: int) -> Camera:
        """Get camera by ID."""
        for camera in self.cameras:
            if camera.camera_id == camera_id:
                return camera
        return None

    def get_all_frames(self):
        """Get frames from all cameras."""
        frames = {}
        for camera in self.cameras:
            frame = camera.get_frame()
            if frame is not None:
                frames[camera.camera_id] = frame
        return frames

    def get_camera_count(self) -> int:
        """Get number of cameras."""
        return len(self.cameras)